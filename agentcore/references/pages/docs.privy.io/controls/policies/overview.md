---
title: Overview
description: Overview of Privy policies for restricting wallet actions like transfers, swaps, and signing.
product: Amazon Bedrock AgentCore
section: References / docs.privy.io
source_url: https://docs.privy.io/controls/policies/overview
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

# Overview

> Overview of Privy policies for restricting wallet actions like transfers, swaps, and signing.

Privy’s policy engine gives your application programmable control over how every wallet can be used.

Instead of relying on ad-hoc checks in your code, you can define enforceable rules at the key level that govern what actions a wallet may take.

With policies, you can configure:

* Transfer limits
* Time-bound signers
* Allowlists and denylists of transfer recipients
* Allowlists and denylists of smart contracts and programs
* Allowlists and denylists of networks
* Allowed time window for key export
* Granular constraints around calldata and parameters that can be passed to smart contracts
* Restrictions around signatures needed for transactions, such as EVM typed data (EIP712)

This allows teams to define security, compliance, and behavioral rules that are applied consistently across all wallets in production.

<img src="https://mintcdn.com/privy-c2af3412/IQmti1WCL7AzN0e1/images/policy-splash.png?fit=max&auto=format&n=IQmti1WCL7AzN0e1&q=85&s=c9541babbe140c284d1b52318038ded5" alt="Managing policies in the Privy Dashboard" width="3686" height="2633" data-path="images/policy-splash.png" />

# Concepts

Privy's policy engine is defined by three core primitives: **policies**, **rules**, and **conditions**; and is designed to give developers precise control over wallets behavior.

At a high-level:

* A **policy** is the complete set of constraints that govern a wallet. It is a list of rules that define the total set of actions that are allowed or denied for a wallet.
* A **rule** describes when an action should be allowed or denied. Each rule is composed of one or more conditions. When a request satisfies all of the conditions, the policy engine executes the action (`ALLOW` or `DENY`) prescribed by the rule.
* A **condition** is a Boolean expression that the policy engine evaluates against an incoming RPC request.

This structure makes Privy’s policy engine flexible enough for complex workflows and predictable enough for production environments.

You can create and manage policies through the [Privy Dashboard](https://dashboard.privy.io), `nodeJS` [SDK](/controls/policies/create-a-policy), or via the [REST API](/controls/policies/create-a-policy).

## Policies

A **policy** is composed from a **list of rules for each RPC method that a wallet can execute** that define what actions are allowed or denied for the wallet. `DENY` actions take precedence over `ALLOW` actions. If no rules resolve, the policy will default to `DENY`.

### Allowlisted RPCs and wallet actions

If a wallet's policy **does not** include a rule for a given RPC method or wallet action API, **usage of that RPC method or API will be denied.** If a policy is set on a wallet, the policy **must** include a rule for any RPC methods or wallet action APIs that the wallet intends to use.

Policy objects have the following properties:

<Expandable title="child attributes" defaultOpen="true">
  <ResponseField name="version" type="'1.0'">
    Version of the policy. Currently, 1.0 is the only version.
  </ResponseField>

  <ResponseField name="name" type="string">
    Name to assign to policy.
  </ResponseField>

  <ResponseField name="chain_type" type="'ethereum' | 'solana' | 'tron' | 'sui'">
    Chain type for wallets that the policy will be applied to.
  </ResponseField>

  <ResponseField name="rules" type="Rule[]">
    A list of `Rule` objects describing what rules to apply to each RPC method (e.g.
    `'eth_sendTransaction'`) that the wallet can take.
  </ResponseField>
</Expandable>

### Policy evaluation

By default, the trusted execution environment (secure enclave) enforces policies for wallet actions. These actions include signature requests, transactions, and key export. The enclave evaluates all policy rules in a tamper-proof environment before signing or exporting key material. Depending on the chain, method, and app configuration, separate compliance screening or transaction simulation may run outside the enclave. These checks are not policy enforcement.

<Info>
  For operations where Privy both signs and broadcasts a transaction, transaction simulation runs
  before policy evaluation. If simulation fails — for example, because the wallet has insufficient
  funds or the contract call would revert — Privy returns the simulation error and does not evaluate
  the policy.

  If a request would both fail simulation and violate a policy, the response reflects the simulation
  failure rather than a policy violation. Privy does not sign or broadcast the transaction in this
  case.
</Info>

When your application makes an RPC request on a wallet that has a policy, the policy engine evaluates the `rules` that are associated with the requested RPC method.

For instance, if your application makes an `'eth_signTransaction'` request, the policy engine will only evaluate rules associated with the `'eth_signTransaction'` method in the policy.

The rules are evaluated as follows:

1. If **any** rule evaluates to a `DENY` action, the policy engine will `DENY` the request.
2. If **any** rule evaluates to an `ALLOW` action, and **no** rules evaluate to `DENY`, then the policy engine will `ALLOW` the request.

If the request does not satisfy *any* of the rules for the policy, the policy engine defaults to `DENY` the request.

This also applies to Solana transactions such that every Instruction in a Solana transaction is evaluated against the rules of the policy. Every instruction must evaluate to an `ALLOW` action for the transaction to be allowed.

<Info>
  If your application makes a request to a wallet with RPC method `X`, and the policy's `rules`
  contains no entry with a `method` corresponding to `X`, the engine will deny the request by
  default. If you'd like the policy engine to instead allow requests for RPC method `X` by default,
  we recommend setting up an "Allow all" `Rule` for that RPC method [like
  so](/controls/policies/example-policies/ethereum#allow-all-requests-for-a-given-rpc-method).
</Info>

## Rules

The nested `Rule` object within the policy's `rules` array. A **rule** is composed of an set of boolean **conditions** and an **action** (`ALLOW` or `DENY`) that is taken if an RPC request satisfies all of the conditions in the rule.
Rule objects have the following fields:

<Expandable title="child attributes" defaultOpen="true">
  <ResponseField name="name" type="string">
    Name to assign to the rule.
  </ResponseField>

  <ResponseField name="method" type="'eth_sendTransaction' | 'eth_signTransaction' | 'eth_signUserOperation' | 'eth_signTypedData_v4' | 'personal_sign' | 'eth_sign7702Authorization' | 'wallet_sendCalls' | 'signTransaction' | 'signAndSendTransaction' | 'signMessage' | 'exportPrivateKey' | 'exportSeedPhrase' | 'signRawMessageBytes' | 'signTransactionBytes' | 'tron_signTransaction' | 'tron_sendTransaction' | 'earn_deposit' | 'earn_withdraw' | 'transfer' | '*'">
    Method to apply the `conditions` to. If an RPC method, must correspond to the `chain_type` of the
    parent policy. Methods `signRawMessageBytes` and `signTransactionBytes` are applicable to Tron and
    Sui only. Use `signRawMessageBytes` for unparsed raw signing requests. Use `signTransactionBytes`
    for parsed transaction bytes that use Tron or Sui transaction field sources.
  </ResponseField>

  <ResponseField name="conditions" type="Condition[]">
    A set of boolean conditions that define the action the rule allows or denies. For
    `exportPrivateKey`, leave `conditions` empty.
  </ResponseField>

  <ResponseField name="action" type="'ALLOW' | 'DENY'">
    Whether the rule should allow or deny a wallet request if it satisfies all of the rule's
    `conditions`.
  </ResponseField>
</Expandable>

Each rule corresponds to an individual action that should be allowed or denied by a wallet. For example, you might configure rules for a policy to:

* `ALLOW` transfers of the native token to a set of allowlisted recipient addresses
* `DENY` interactions with specific Ethereum smart contracts or Solana programs

## Conditions

A **condition** is a boolean statement about a wallet request. When evaluating a wallet request against a rule, the policy engine checks whether the wallet request satisfies each of the boolean conditions in the rule. If all of the conditions are satisfied, the engine executes the action associated with the rule.

Conditions allow you to define specific action types that should be allowed or denied for a wallet.

<Expandable title="child attributes" defaultOpen="true">
  <ResponseField name="field_source" type="'ethereum_transaction' | 'ethereum_calldata' | 'ethereum_typed_data_domain' | 'ethereum_typed_data_message' | 'ethereum_7702_authorization' | 'solana_program_instruction' | 'solana_system_program_instruction' | 'solana_token_program_instruction' | 'tron_transaction' | 'tron_trigger_smart_contract_data' | 'sui_transaction_command' | 'sui_transfer_objects_command' | 'tempo_transaction' | 'message' | 'action_request_body' | 'system' | 'reference'">
    Data source from which to derive the `field` for the condition.
  </ResponseField>

  <ResponseField name="field" type="string">
    The attribute to evaluate for a wallet request. As an example, the field for the recipient of an
    EVM transaction is `'to'`.
  </ResponseField>

  <ResponseField name="abi" type="JSON">
    Contract ABI to decode Ethereum or Tron calldata against. Should only be set for
    `'ethereum_calldata'` or `'tron_trigger_smart_contract_data'` policies. Must strictly be formatted
    as JSON.
  </ResponseField>

  <ResponseField name="operator" type="'eq' | 'neq' | 'lt' | 'lte' | 'gt' | 'gte' | 'in' | 'in_condition_set' | 'contains' | 'starts_with' | 'ends_with'">
    Boolean operator used to compare a `field` with a `value`
  </ResponseField>

  <ResponseField name="value" type="string | number | string[]">
    Static value to compare a `field` to.
  </ResponseField>
</Expandable>

Conditions for certain sources may have additional parameters. For instance, `ethereum_calldata` and `tron_trigger_smart_contract_data` conditions also require an `abi` parameter used to decode the calldata, and `ethereum_typed_data_message` conditions require a `typed_data` parameter to define the schema for the typed data message.

### Field

**Fields** are attributes of a wallet request that can be parsed or interpreted from the wallet request. Examples of fields include the `to` parameter of an EVM transaction, the `fee_payer` parameter of a Solana transaction, or an `spl_transfer_recipient` field that is populated when the policy engine interprets a transaction.

Fields are derived from **field sources**, which surface data from the wallet request. Possible field sources are listed below.

<Tip>
  The policy engine evaluates numerical data exactly as passed in the request body—no conversion is
  applied. For example, ETH values will be evaluated in wei, SOL in lamports, and OUSD in
  microdollars.
</Tip>

| Field source                          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Example fields                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `'ethereum_transaction'`              | The verbatim Ethereum transaction object in an `eth_signTransaction`, `eth_sendTransaction`, `eth_signUserOperation`, or `wallet_sendCalls` request.                                                                                                                                                                                                                                                                                                                                                                                               | `to`, `value`, `chain_id`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `'ethereum_calldata'`                 | The decoded calldata in a smart contract interaction, with fields representing both the function name and, if applicable, function arguments. Note: `'ethereum_calldata'` conditions must always include an `abi` parameter with the contract's JSON ABI—even for functions with no input parameters (such as `deposit()`). The value of `field` can be just the function name (e.g., `function_name`) to match any call to a given function, or the function name plus argument (e.g., `function_name.param_name`) to match a specific parameter. | `function_name` (e.g., allow any call to `deposit()`), `function_name._to`, `function_name._value` (for ERC20 and similar interactions)                                                                                                                                                                                                                                                                                                                                                                                          |
| `'ethereum_typed_data_domain'`        | Attributes from the signing domain that will verify the signature.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | `chainId`, `verifyingContract`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `'ethereum_typed_data_message'`       | `types` and `primary_type` attributes of the TypedData JSON object defined in [EIP-712](https://eips.ethereum.org/EIPS/eip-712#specification-of-the-eth_signtypeddata-json-rpc).                                                                                                                                                                                                                                                                                                                                                                   | dot-separated path to value in `message` object, i.e. `to.wallet`                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `'ethereum_7702_authorization'`       | EIP-7702 authorization data from an `eth_sign7702Authorization` request.                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | `contract`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `'solana_program_instruction'`        | Solana program instruction from a `signTransaction` or `signAndSendTransaction` request.                                                                                                                                                                                                                                                                                                                                                                                                                                                           | `programId`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `'solana_system_program_instruction'` | Fields relevant to the Solana System Program and its Transfer instruction.                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | `instructionName`, `Transfer.to`, `Transfer.from`, `Transfer.lamports`                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `'solana_token_program_instruction'`  | Fields relevant to the SPL Token Program and its supported instructions: Transfer, TransferChecked, Burn, MintTo, CloseAccount, and InitializeAccount3.                                                                                                                                                                                                                                                                                                                                                                                            | `instructionName`, `Transfer.source`, `Transfer.destination`, `Transfer.authority`, `Transfer.amount`, `TransferChecked.source`, `TransferChecked.destination`, `TransferChecked.authority`, `TransferChecked.amount`, `Burn.account`, `Burn.mint`, `Burn.authority`, `Burn.amount`, `MintTo.mint`, `MintTo.account`, `MintTo.authority`, `MintTo.amount`, `CloseAccount.account`, `CloseAccount.destination`, `CloseAccount.authority`, `InitializeAccount3.account`, `InitializeAccount3.mint`, `InitializeAccount3.authority` |
| `'tron_transaction'`                  | The Tron transaction object in a `signTransactionBytes` raw signing request or a `tron_signTransaction`/`tron_sendTransaction` RPC policy rule.                                                                                                                                                                                                                                                                                                                                                                                                    | `TransferContract.to_address`, `TransferContract.amount`, `TriggerSmartContract.contract_address`, `TriggerSmartContract.call_value`, `TriggerSmartContract.token_id`, `TriggerSmartContract.call_token_value`                                                                                                                                                                                                                                                                                                                   |
| `'tron_trigger_smart_contract_data'`  | The decoded calldata in a smart contract interaction as the smart contract method's parameters. Applies to `signTransactionBytes` raw signing requests and `tron_signTransaction`/`tron_sendTransaction` RPC policy rules. Note that `'tron_trigger_smart_contract_data'` conditions must contain an `abi` parameter with the JSON ABI of the smart contract.                                                                                                                                                                                      | `function_name`, `_to`, `_value` (for a TRC20 interaction)                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `'sui_transaction_command'`           | Commands in a Sui transaction in an `signTransactionBytes` request.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | `TransferObjects`, `SplitCoins`, `MergeCoins`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `'sui_transfer_objects_command'`      | The Sui TransferObjects command in an `signTransactionBytes` request. Sends one or more objects to a specified address.                                                                                                                                                                                                                                                                                                                                                                                                                            | `amount`, `recipient`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `'message'`                           | The decoded message content in a message signing request. Applicable to `personal_sign` (Ethereum), `signMessage` (Solana), and `signRawMessageBytes` (Sui). Supports string operators (`eq`, `contains`, `starts_with`, `ends_with`, `in`, `in_condition_set`) on the `content` field, and numeric operators (`eq`, `gt`, `gte`, `lt`, `lte`) on the `byte_length` field.                                                                                                                                                                         | `content`, `byte_length`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `'tempo_transaction'`                 | Tempo transaction specific fields from an `eth_signTransaction` or `eth_sendTransaction` request. Kept separate from `'ethereum_transaction'` so existing EVM rules are unaffected. See [Tempo policy examples](/controls/policies/example-policies/tempo) for usage.                                                                                                                                                                                                                                                                              | `fee_token` (address), `fee_payer_signature` (presence), `nonce_key` (bigint), `valid_before` (bigint, Unix seconds), `valid_after` (bigint, Unix seconds), `aa_authorization_list` (presence), `access_list` (presence)                                                                                                                                                                                                                                                                                                         |
| `'action_request_body'`               | Fields from the original wallet action request body. For wallet action APIs (e.g. [Transfer](/wallets/actions/transfer/policies), [Earn](/wallets/actions/earn/policies)), policy evaluation runs against the request body sent to the API before Privy prepares the underlying transactions.                                                                                                                                                                                                                                                      | Transfer: `source.asset`, `source.asset_address`, `source.amount`, `source.chain`, `destination.address`, `destination.asset`, `destination.chain`; Earn: `vault_id`, `amount`, `raw_amount`                                                                                                                                                                                                                                                                                                                                     |
| `'system'`                            | Chain-agnostic system fields, such as the current timestamp at the time of the request.                                                                                                                                                                                                                                                                                                                                                                                                                                                            | `current_unix_timestamp`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `'reference'`                         | A reference to an Aggregation for [stateful policies](/controls/policies/stateful-policies). Allows a condition to evaluate against historical data such as cumulative transaction values over a time window. Each condition can reference one Aggregation. Only supported for Ethereum methods (`eth_signTransaction`, `eth_signUserOperation`).                                                                                                                                                                                                  | `aggregation.{aggregation_id}` (e.g., `aggregation.abc123def456ghi789`)                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

### Operator

**Operators** are boolean operators used to compare fields and values. Operators include `eq`, `neq`, `lt`, `lte`, `gt`, `gte`, `in`, `in_condition_set`, `contains`, `starts_with`, and `ends_with`.

All string comparisons are case-sensitive.

<Tip>
  The `in` operator can be configured with up to 100 values. Consider `in_condition_set` operator if
  you need more.
</Tip>

### Values

A condition compares a field using its boolean operator to a static **value**. As an example, if a condition determines whether an Ethereum transaction has specific recipient address `X`, the value for the condition is `X`.
