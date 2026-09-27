---
title: Sanctions screening for x402 payments
description: Use Privy policies and condition sets to deny x402 payments to sanctioned recipient addresses on Base, Tempo, and Solana before anything is signed.
product: Amazon Bedrock AgentCore
section: References / docs.privy.io
source_url: https://docs.privy.io/recipes/agent-integrations/x402-sanctions-screening
fetched: '2026-09-26'
tags:
- agentcore
- docs-privy-io
- reference
- related
referenced_by:
- payments-security-best-practices.md
conversion: native-md
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.privy.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Sanctions screening for x402 payments

> Use Privy policies and condition sets to deny x402 payments to sanctioned recipient addresses on Base, Tempo, and Solana before anything is signed.

# Block x402 payments to sanctioned addresses

This recipe shows how an app can prevent x402 payments to addresses on a sanctions list, enforced by Privy's policy engine before anything is signed. It covers Base and Tempo (EVM) and Solana.

<Info>
  Privy is infrastructure, not a compliance program. Each app determines its own compliance
  obligations and layers the tooling it sees fit on top of Privy. A denylist blocks known addresses.
  It does not screen for indirect exposure, nested services, or newly generated addresses. Pair it
  with a screening provider such as Chainalysis, TRM, or Blockaid for risk scoring. Nothing in this
  guide constitutes compliance or legal advice. Validate the approach with legal and compliance
  teams, and keep the source data and review process current.
</Info>

## Where to screen an x402 payment

x402 payments are not ordinary transactions, so screening `eth_sendTransaction` alone does not catch them.

* **Base and Tempo (EVM)**: an x402 payment is an [EIP-3009](https://eips.ethereum.org/EIPS/eip-3009) `transferWithAuthorization` authorization. The client signs an EIP-712 typed-data message over `eth_signTypedData_v4`, and a facilitator submits it onchain and pays gas. The recipient to screen is the `to` field inside the `TransferWithAuthorization` message.
* **Solana**: the payment is a USDC (SPL) transfer signed via `signTransaction` or `signAndSendTransaction`. The x402 library builds it as a `TransferChecked` instruction, so the recipient to screen is `TransferChecked.destination`. The policy below also covers `Transfer.destination` in case the client emits a plain `Transfer`.

The policy below enforces that the payment recipient is not on the sanctions list at the moment Privy signs, inside the secure enclave, so a modified client cannot bypass it.

```
User initiates an x402 request
  -> Client builds the payment authorization
  -> Privy policy engine extracts the recipient from the signing request
  -> Recipient checked against the current condition set
  -> No match: sign; facilitator settles
  -> Match: DENY, nothing is signed
```

## Why the policy engine is the enforcement point

* **DENY takes precedence.** If any rule evaluates to DENY, the policy engine denies the request even if another rule would allow it. A denylist can therefore extend an existing policy without reworking its allow rules.
* **Unmatched methods default to DENY.** If no rule returns an action for a requested method, the policy engine denies the request. Pair the denylist with ALLOW rules for the methods the app legitimately uses.
* **Condition sets update independently of the policy.** Addresses live in a condition set referenced by ID, so new designations sync without redeploying or re-signing the policy.
* **Privy enforces policies per wallet.** A policy applies only to the wallets that list it in `policy_ids`. Every wallet the app creates must carry the policy from creation.

An app-side pre-check can improve the user experience, but clients can be modified and server paths can be bypassed. Keep the Privy policy as the authoritative control and treat any pre-check as advisory.

## 1. Define the authoritative list and its owner

Use a sanctions-data source approved by the compliance team, for example the U.S. Treasury OFAC SDN list, and establish:

* the team responsible for reviewing and approving list updates
* the refresh cadence, at least daily and more often if the risk posture requires it
* an audit trail recording source, fetch time, version or hash, and addresses added or removed
* an escalation path for potential matches and false positives

Store the chain family alongside every address. An address should never be treated as globally sanctioned without chain context.

Create an [owner](/controls/authorization-keys/using-owners/overview) for the condition set and the policy. Condition sets require an owner, and updates to both require an [authorization signature](/api-reference/authorization-signatures#usage). Without an owner, the app secret alone can modify the denylist.

## 2. Create the condition set

Create one condition set per chain family, one for EVM and one for Solana. Each policy targets a single `chain_type`, and separate sets keep the audit trail per chain clean and allow independent refreshes.

```shell theme={"system"}
curl -X POST https://api.privy.io/v1/condition_sets \
  -u "<your-privy-app-id>:<your-privy-app-secret>" \
  -H "privy-app-id: <your-privy-app-id>" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "OFAC sanctioned addresses (EVM)",
    "owner_id": "<your-owner-id>"
  }'
```

```json theme={"system"}
{
  "id": "qvah5m2hmp9abqlxdmfiht95",
  "name": "OFAC sanctioned addresses (EVM)",
  "owner_id": "<your-owner-id>",
  "created_at": 1761271537642
}
```

Keep the returned `id`. The policy references the denylist by ID, not by name.

## 3. Load the addresses into the condition set

Fetching and batching the addresses is general code, so it is not reproduced here. At a high level:

* Pull digital-currency addresses from the machine-readable [SDN enhanced XML export](https://sanctionslistservice.ofac.treas.gov/api/PublicationPreview/exports/SDN_ENHANCED.XML) on a schedule.
* Branch on address format, not on the asset label. USDC and USDT appear on multiple chains, and one address can carry several asset labels. EVM addresses start with `0x`, and Solana addresses are base58.
* POST them to the condition set in batches of up to 100 items per request.

The only Privy-specific call is adding items:

```shell theme={"system"}
curl -X POST https://api.privy.io/v1/condition_sets/qvah5m2hmp9abqlxdmfiht95/condition_set_items \
  -u "<your-privy-app-id>:<your-privy-app-secret>" \
  -H "privy-app-id: <your-privy-app-id>" \
  -H "privy-authorization-signature: <authorization-signature-for-request>" \
  -H "Content-Type: application/json" \
  -d '[
    { "value": "<first-designated-address>" },
    { "value": "<second-designated-address>" }
  ]'
```

<Tip>
  For the signing conditions in this guide, the policy engine compares EVM addresses
  case-insensitively, so each address needs a single entry in either checksummed or lowercase form.
  Solana base58 addresses are matched exactly, so store those verbatim. The high-level `transfer`
  action is also matched exactly, even for EVM addresses. See [the transfer
  action](#the-transfer-action).
</Tip>

## 4. Create the policy

### Base and Tempo (EVM)

The x402 signing path is `eth_signTypedData_v4`. Screen the `to` field of the `TransferWithAuthorization` message against the condition set.

<Warning>
  An `ethereum_typed_data_message` condition only evaluates when the `types` map declared in the
  policy matches the `types` map in the signing request **exactly**, including every type the client
  sends and the field order within each type. On a mismatch the condition evaluates to `false`,
  which means a DENY rule never fires and a permissive ALLOW rule signs the request anyway.
</Warning>

#### Determine the types map the client sends

The x402 library defines only `TransferWithAuthorization`. Whether `EIP712Domain` also reaches Privy
depends on how the wallet is wired up:

| Client                                                                                                                                                                                                   | `types` in the signing request                     |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------- |
| `createX402Client` from `@privy-io/node`                                                                                                                                                                 | `TransferWithAuthorization` only                   |
| `useX402Fetch` from `@privy-io/react-auth`                                                                                                                                                               | `TransferWithAuthorization` only                   |
| A viem `WalletClient` wired to Privy directly, or any integration that builds the `eth_signTypedData_v4` call itself, including a platform that signs on a developer's behalf such as AgentCore Payments | `EIP712Domain` **and** `TransferWithAuthorization` |

Both Privy clients hand x402 a viem `LocalAccount`, which x402 calls directly, so its types map is
forwarded untouched. A `WalletClient` instead routes through viem's `signTypedData` action, which
inserts an `EIP712Domain` entry derived from the domain fields.

The example below uses the shape both Privy clients produce. To screen requests that carry
`EIP712Domain`, add it to the same `types` map, listing only the domain fields the client actually
sends, in the order `name`, `version`, `chainId`, `verifyingContract`:

```ts {skip-check} theme={"system"}
EIP712Domain: [
  {name: 'name', type: 'string'},
  {name: 'version', type: 'string'},
  {name: 'chainId', type: 'uint256'},
  {name: 'verifyingContract', type: 'address'}
],
```

If an app signs through more than one of these paths, give each shape its own DENY rule. A rule only
screens requests whose `types` map it matches exactly, so one rule cannot cover both.

<Warning>
  Confirm the shape against a real request rather than inferring it. Send one payment and inspect
  the `typed_data.types` the app submits, then mirror it exactly. If the policy declares a map the
  client does not send, both rules stop matching and the request is denied by default, so the
  symptom is every payment failing rather than a sanctioned payment slipping through. `EIP712Domain`
  also lists only the domain fields actually present, so a client that omits `name` or `version`
  produces a different map again.
</Warning>

```ts {skip-check} theme={"system"}
const SANCTIONS_SET_ID = 'qvah5m2hmp9abqlxdmfiht95';

// The types map the Privy x402 clients send for an EIP-3009 authorization.
// This must match the signing request exactly, including field order. Add an
// EIP712Domain entry here if the app wires up its own viem WalletClient.
const transferWithAuthorization = {
  types: {
    TransferWithAuthorization: [
      {name: 'from', type: 'address'},
      {name: 'to', type: 'address'},
      {name: 'value', type: 'uint256'},
      {name: 'validAfter', type: 'uint256'},
      {name: 'validBefore', type: 'uint256'},
      {name: 'nonce', type: 'bytes32'}
    ]
  },
  primary_type: 'TransferWithAuthorization'
};

const policy = await privy.policies().create({
  version: '1.0',
  name: 'OFAC sanctions denylist (x402)',
  chain_type: 'ethereum',
  owner_id: '<your-owner-id>',
  rules: [
    // Deny x402 payments whose recipient is on the denylist.
    {
      name: 'Deny sanctioned x402 recipients',
      method: 'eth_signTypedData_v4',
      action: 'DENY',
      conditions: [
        {
          field_source: 'ethereum_typed_data_message',
          typed_data: transferWithAuthorization,
          field: 'to',
          operator: 'in_condition_set',
          value: SANCTIONS_SET_ID
        }
      ]
    },

    // Allow x402 authorizations that clear the denylist. Pinning the same types map here
    // means a client-side schema change fails closed: both rules stop matching, no rule
    // returns an action, and the request is denied by default.
    {
      name: 'Allow x402 authorizations on Base',
      method: 'eth_signTypedData_v4',
      action: 'ALLOW',
      conditions: [
        {
          field_source: 'ethereum_typed_data_domain',
          field: 'chainId',
          operator: 'eq',
          value: '8453'
        },
        {
          field_source: 'ethereum_typed_data_domain',
          field: 'verifyingContract',
          operator: 'eq',
          // The USDC contract on the target chain, as sent in the EIP-712 domain.
          value: '<usdc-contract-address>'
        },
        // Trivially true. Present so the rule is bound to the same message schema
        // as the DENY rule above.
        {
          field_source: 'ethereum_typed_data_message',
          typed_data: transferWithAuthorization,
          field: 'value',
          operator: 'gte',
          value: '0'
        }
      ]
    }
  ]
});

await privy.wallets().update('<wallet-id>', {policy_ids: [policy.id]});
```

Add one ALLOW rule per typed-data message shape the app signs. A rule pinned to `TransferWithAuthorization` denies every other message type, which is the intended behavior for a payments-only wallet but breaks apps that also sign permits or logins.

For Tempo, keep the same rule shape and set the domain conditions to Tempo's chain ID and USDC contract. If the app also moves value through ordinary transactions, add matching DENY rules on `eth_sendTransaction` and `eth_signTransaction` that screen `ethereum_transaction.to` for native transfers and the decoded calldata recipient for ERC-20 `transfer` and `transferFrom`.

### Solana

```ts {skip-check} theme={"system"}
const SANCTIONS_SET_ID = '<your-solana-condition-set-id>';
const SIGNING_METHODS = ['signTransaction', 'signAndSendTransaction'];

const policy = await privy.policies().create({
  version: '1.0',
  name: 'OFAC sanctions denylist (x402)',
  chain_type: 'solana',
  owner_id: '<your-owner-id>',
  rules: [
    // Deny SPL (USDC) transfers to sanctioned destinations. Rule names must be
    // 50 characters or fewer, so keep generated names short.
    ...SIGNING_METHODS.flatMap((method) =>
      ['Transfer.destination', 'TransferChecked.destination'].map((field) => ({
        name: `Deny sanctioned ${field}`,
        method,
        action: 'DENY',
        conditions: [
          {
            field_source: 'solana_token_program_instruction',
            field,
            operator: 'in_condition_set',
            value: SANCTIONS_SET_ID
          }
        ]
      }))
    ),

    // Allow the rest of the app's legitimate signing. Both signing methods need an ALLOW
    // rule: a method with no rule that returns an action is denied by default. Solana
    // rules must declare at least one condition, so this uses a trivially true one.
    ...SIGNING_METHODS.map((method) => ({
      name: 'Allow other instructions',
      method,
      action: 'ALLOW',
      conditions: [
        {
          field_source: 'system',
          field: 'current_unix_timestamp',
          operator: 'gte',
          value: '0'
        }
      ]
    }))
  ]
});
```

<Warning>
  Solana evaluation requires **every** instruction in the transaction to be allowed by at least one
  rule. An x402 payment usually carries more than the token transfer, such as a compute budget
  instruction, so narrowing the ALLOW rule to `instructionName in ['Transfer', 'TransferChecked']`
  rejects the whole transaction. Narrow the ALLOW rule only after confirming which instructions the
  x402 client actually emits.
</Warning>

The policy engine evaluates every instruction in a Solana transaction, so a DENY on any single instruction rejects the whole transaction.

### The transfer action

Rules are scoped to a method, so the rules above only screen the signing methods they name. An app
that also moves funds through the high-level [transfer](/wallets/actions/transfer/policies) action
needs its own rules, screening `destination.address` from the request body.

```ts {skip-check} theme={"system"}
const rules = [
  {
    name: 'Deny sanctioned transfer destinations',
    method: 'transfer',
    action: 'DENY',
    conditions: [
      {
        field_source: 'action_request_body',
        field: 'destination.address',
        operator: 'in_condition_set',
        value: SANCTIONS_SET_ID
      }
    ]
  },
  {
    name: 'Allow USDC transfers on Base',
    method: 'transfer',
    action: 'ALLOW',
    conditions: [
      {field_source: 'action_request_body', field: 'source.asset', operator: 'eq', value: 'usdc'},
      {field_source: 'action_request_body', field: 'source.chain', operator: 'eq', value: 'base'}
    ]
  }
];
```

<Warning>
  Unlike the signing conditions above, `action_request_body` comparisons are **exact**. A denylist
  holding a checksummed address does not match the same address sent in lowercase, and the DENY rule
  silently fails to fire. Normalize destination addresses to a single form before calling
  `transfer`, or store both forms in the condition set.
</Warning>

A policy that omits `transfer` rules entirely does not leave transfers unscreened: an unmatched
method is denied by default, so every `transfer` call fails until a rule allows it.

## 5. Attach the policy to wallets

Attach the policy at creation so no wallet ever exists without the denylist:

```shell theme={"system"}
curl -X POST https://api.privy.io/v1/wallets \
  -u "<your-privy-app-id>:<your-privy-app-secret>" \
  -H "privy-app-id: <your-privy-app-id>" \
  -H "Content-Type: application/json" \
  -d '{
    "chain_type": "ethereum",
    "policy_ids": ["<your-policy-id>"]
  }'
```

For existing wallets, patch them. If the wallet has an `owner_id`, the update must be authorized by that owner:

```shell theme={"system"}
curl -X PATCH https://api.privy.io/v1/wallets/<wallet-id> \
  -u "<your-privy-app-id>:<your-privy-app-secret>" \
  -H "privy-app-id: <your-privy-app-id>" \
  -H "privy-authorization-signature: <authorization-signature-for-request>" \
  -H "Content-Type: application/json" \
  -d '{ "policy_ids": ["<your-policy-id>"] }'
```

To apply different denylists to different signers on the same wallet, attach the policy as an override policy on the signer instead. See [conditional signer policies](/recipes/wallets/conditional-signer-policies).

<Tip>
  When a third party creates wallets on an app's behalf, the policy ID must reach that integration.
  Pass it alongside the app ID, app secret, and authorization key so wallets are created with
  `policy_ids` already set.
</Tip>

## 6. Reject consistently and safely

When the policy denies a request, Privy does not sign it and returns a `policy_violation` error. Map it to a stable, client-safe response:

* return a consistent 4xx, either 403 or 422
* use a generic message that does not reveal screening details
* record an internal audit event with policy version, matched address, chain, timestamp, and request identifier
* route the event to the compliance or risk-review workflow

```json theme={"system"}
{
  "error": "transaction_blocked_by_policy",
  "message": "This payment cannot be completed under your organization's transfer policy."
}
```

Do not echo the matched address, condition set ID, or rule name to end users. Detailed rejection reasons let a caller enumerate the denylist by probing.

## 7. Decide behavior when the sanctions source is unavailable

Enforcement does not depend on the sanctions source being reachable at signing time, because the condition set is the versioned local cache. What the app must decide is how the sync job behaves when the source is unavailable, and how stale a list it tolerates. Document one of:

* **Fail closed**: if the list cannot be refreshed within the maximum tolerated age, tighten the policy to deny the affected methods.
* **Fail open with alerting**: keep enforcing against the last known-good set and alert immediately.
* **Recommended**: enforce continuously against the condition set, refresh asynchronously, and continue on the last known-good contents up to a defined maximum age, then apply the chosen fail mode.

Refresh the list in place. The policy never changes, so this requires no redeploy and no re-signature:

```shell theme={"system"}
curl -X PUT https://api.privy.io/v1/condition_sets/qvah5m2hmp9abqlxdmfiht95/condition_set_items \
  -u "<your-privy-app-id>:<your-privy-app-secret>" \
  -H "privy-app-id: <your-privy-app-id>" \
  -H "privy-authorization-signature: <authorization-signature-for-request>" \
  -H "Content-Type: application/json" \
  -d '[{ "value": "0x..." }, { "value": "0x..." }]'
```

<Warning>
  If a condition set is deleted, every condition referencing it evaluates to `false`. The denylist
  silently stops blocking while ALLOW rules keep passing traffic. Give the set an owner, and alert
  on an unexpectedly empty, shrunken, or missing set.
</Warning>

## 8. Test before enabling

Cover at least these cases in a non-production environment:

| Case                                                                | Expected                               |
| :------------------------------------------------------------------ | :------------------------------------- |
| x402 payment (`eth_signTypedData_v4`) to an unlisted recipient      | Allowed                                |
| x402 payment to a listed recipient (`to` in the message)            | Rejected                               |
| Listed EVM address submitted in the opposite casing (signing paths) | Rejected                               |
| `transfer` to a listed `destination.address`, exact casing          | Rejected                               |
| `transfer` to that address in the opposite casing                   | Rejected only if both forms are stored |
| Request whose `types` map differs from the policy's                 | Rejected by default DENY               |
| Solana SPL transfer to a listed destination                         | Rejected                               |
| Stale list or sync outage                                           | Follows the documented fail mode       |
| Every rejection                                                     | Auditable, exposes no internal detail  |

Run the allowed and rejected cases against the same wallet and policy. A DENY rule that never fires looks identical to a correctly configured policy until a listed address is tested explicitly.

## Limitations

* **Direct recipients only.** The engine screens the recipient in the signing request. Funds routed through a bridge, mixer, or intermediary that later reach a sanctioned address are not caught. Use a screening provider for indirect exposure.
* **Typed-data screening needs the schema.** An `ethereum_typed_data_message` condition only matches messages whose `types` map matches the declared one exactly. Screen every message type the app signs over.
* **Solana SPL destinations are token accounts.** `TransferChecked.destination` is an associated token account, not the owner's wallet address. To screen owners, derive and store the associated token accounts for each sanctioned address and each supported mint.
* **Solana address lookup tables.** Policy evaluation cannot resolve addresses stored in an address lookup table. Keep screened addresses in the transaction's static account keys.
* **Wallets without the policy are unprotected.** Enforcement is per wallet. Audit that every wallet carries the policy.

## Further reading

* [Policies overview](/controls/policies/overview)
* [Condition sets](/controls/policies/condition-sets)
* [Ethereum policy examples](/controls/policies/example-policies/ethereum)
* [Solana policy examples](/controls/policies/example-policies/solana)
* [Using x402 payments with Privy](/recipes/agent-integrations/x402)
* [EIP-3009 standard](https://eips.ethereum.org/EIPS/eip-3009)
* [OFAC SDN list](https://sanctionslist.ofac.treas.gov/Home/SdnList) and the [machine-readable SDN enhanced XML export](https://sanctionslistservice.ofac.treas.gov/api/PublicationPreview/exports/SDN_ENHANCED.XML)
