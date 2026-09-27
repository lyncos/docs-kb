---
title: Embedded wallets
description: Self-custodial wallets built into your app for Ethereum, Solana, and other chains — powered by secure hardware (TEEs)
product: Amazon Bedrock AgentCore
section: References / docs.privy.io
source_url: https://docs.privy.io/wallets/overview/embedded
fetched: '2026-09-26'
tags:
- agentcore
- docs-privy-io
- reference
- related
referenced_by:
- payments-concepts.md
conversion: native-md
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.privy.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Embedded wallets

> Self-custodial wallets built into your app for Ethereum, Solana, and other chains — powered by secure hardware (TEEs)

Privy's embedded wallet system lets you build wallets directly into your app whether you're building non-custodial wallets for your users or a wallet fleet you control.

Privy's wallet infrastructure ensures only the appropriate party controls the wallet. This means you can set up wallets for any user, customer, business, or agent under a range of custody options. Embedded wallets can be configured as [non-custodial](/wallets/overview/embedded) or [custodial](/wallets/custodial-wallets/overview).

Privy surfaces both user-centric abstractions enabling you to authenticate users and generate wallets for them, as well as wallet-centric abstractions whereby you can create wallets with assigned authorization keys to control them.

<img src="https://mintcdn.com/privy-c2af3412/IQmti1WCL7AzN0e1/images/embedded-wallets-splash.png?fit=max&auto=format&n=IQmti1WCL7AzN0e1&q=85&s=6a3d0548d716f4899efe6e4f9d7bc192" alt="images/embedded-wallets-splash.png" width="3686" height="2633" data-path="images/embedded-wallets-splash.png" />

## Features

Privy's wallet infrastructure gives you the flexibility to manage key signing directly or integrate onchain infrastructure like smart accounts out of the box. Wallets ship with:

* **Cross-chain usage**: Create and manage wallets on all EVM- and SVM-compatible blockchains, including Ethereum, Solana, Tempo, Base, Arbitrum, HyperEVM, and Eclipse. Privy also supports [many other chains](/wallets/overview/chains), such as Bitcoin, Spark, TRON, Stellar, and more.
* **Robust transaction controls**: Execute arbitrary transactions with wallets, such as transferring funds and interactions with smart contracts. Make transactions idempotent to ensure that they are only submitted once in case of a retry.
* **Onchain indexing**: Broadcast transactions onchain and register event listeners (via [webhooks](/wallets/gas-and-asset-management/assets/transaction-event-webhooks)) on transaction status, deposits, and withdrawals.
* **Powerful policy engine**: Enforce granular policies what actions a wallet can take, set allowlisted contracts or recipients, maximum amounts to be transferred, restrictions on smart contract calldata, and more. Enforce MFA on transactions, require approval signatures from a quorum of parties, and more. [Learn more](/controls/overview)
* **Authorization controls**: Cryptographically enforce a chain of required approvals on wallets from `m-of-n` parties to execute certain wallet actions.
* **Automated gas sponsorship**: Never worry about topping up a wallet. Keep wallets loaded to pay for transactions at all times. [Learn more](/wallets/gas-and-asset-management/overview)
* **Rich onchain integrations**: Leverage features like Privy's wallet UI components, RainbowKit connector, transaction and balance webhooks, or automated gas management to streamline your integration with the blockchain.

## Common use cases

View some common use cases for Privy.

### User wallets

You can generate non-custodial wallets for your users for a wallet experience that is directly embedded in your application—no separate wallet client, like a browser extension or a mobile app, required.

This means users have full custody of their wallets without needing to manage secret keys. Neither Privy nor your application ever sees the user's keys; secrets are only ever reconstituted in a secure environment under the user's control so they can sign messages or transactions.

Users can manage their embedded wallet seamlessly with their account; they never need to handle any unnecessary technical complexity. Your application can even [pregenerate wallets](/recipes/pregenerate-wallets) for an account, like an email address or phone number, before the user logs in. Users can also [export the key](/wallets/wallets/export) for their embedded wallet, providing an escape hatch to leave Privy at any time.

Your application can easily guide users to use their wallet with simple abstractions to prompt users to fund, transact, and sign with their wallet.

Learn more about support for [user wallets](/wallets/overview/solutions/user-wallets).

### Organization wallets

Set up a fleet of non-custodial and/or custodial wallets wallets to enable secure asset management for organizations and businesses. Multiple members of an organization can be provisioned access to the same wallet. Secure funds via quorums of pre-approved signers and policies with granular approval workflows.

Register webhooks to automate events based on onchain actions, assign specific policies to wallet signers to manage risk, and more.

Wallets leverage secure enclaves and key splitting to ensure secure key reconstitution and appropriate custody for all use cases.

Learn more about support for [organization wallets](/wallets/overview/solutions/organization-wallets).

### Treasury

Set up non-custodial or custodial wallets to manage your organization's treasury. Configure granular approval workflows to assign specific permissions to users over transactions, policy updates, workflow updates, and more. Initiate actions programmatically via the Privy API or manually via the Dashboard.

Learn more about support for [treasury](/wallets/overview/solutions/treasury-wallets).

### Agentic wallets

Privy enables you to securely provision wallets for agents. Agents can execute actions on users' behalf, like payments or trades, via natural language prompts from users or asynchronously while the user is offline. Users can configure granular policies to restrict agent spend and ensure that transactions are aligned with user preferences and intent.

Learn more about support for [agent wallets](/wallets/overview/solutions/agent-wallets).

## Get started

<CardGroup>
  <Card title="Create a wallet" icon="rocket" href="/wallets/wallets/create/create-a-wallet">
    Create a wallet
  </Card>

  <Card title="Connect external wallets" icon="screwdriver-wrench" href="/wallets/connectors/usage/connecting-external-wallets">
    Connect external wallets to your app like MetaMask or Phantom
  </Card>

  <Card title="Provision signers" icon="code" href="/wallets/using-wallets/signers/overview">
    Take actions on behalf of your users by adding signers
  </Card>
</CardGroup>
