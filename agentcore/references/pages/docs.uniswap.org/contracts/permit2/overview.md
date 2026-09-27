---
title: Permit2 Overview
description: '[](/)'
product: Amazon Bedrock AgentCore
section: References / docs.uniswap.org
source_url: https://docs.uniswap.org/contracts/permit2/overview
fetched: '2026-09-26'
tags:
- agentcore
- docs-uniswap-org
- reference
- related
referenced_by:
- payments-process-payment.md
conversion: pandoc
---

[](/)

Search/

Get Started

[Quick Start](/docs/get-started/quickstart)

Concepts

Swapping

[Overview](/docs/trading/overview)

Uniswap API

[Custom Linking](/docs/trading/custom-interface-links)[Embed the Uniswap App](/docs/trading/embed-app)

Liquidity

[Overview](/docs/liquidity/overview)

Liquidity Provisioning

Liquidity Launchpad

UniswapX

Protocols

[Overview](/docs/protocols/overview)[Deployments](/deployments)

Uniswap v4

Uniswap Labs Hooks

Uniswap v3

Uniswap v2

Smart Wallet

The Compact

Permit2

[Overview](/docs/protocols/permit2/overview)

Concepts

Universal Router

Protocol Fee

SDKs

[Overview](/docs/sdks/overview)

Uniswap v4

Uniswap v3

Uniswap v2

Uniswap AI

[Overview](/docs/uniswap-ai/overview)[Uniswap Skills](/docs/uniswap-ai/skills)[Contributions](/docs/uniswap-ai/contributions)

Unichain

[Overview](/docs/unichain)

Get Started

Guides

Technical Information

Tools

Ecosystem

Builder Support

Governance

Subgraphs

[Research](/docs/ecosystem/research)

Copy Markdown

Open in...

# Permit2 Overview

Learn how Uniswap Permit2 combines signature-based transfers and time-bound allowances for token spending.

[Permit2](https://github.com/Uniswap/permit2) is a unification of 2 contracts, `SignatureTransfer` and `AllowanceTransfer`. The `SignatureTransfer` contract handles all signature-based transfers, meaning that an allowance on the token is bypassed and permissions to the spender only last for the duration of the transaction that the one-time signature is spent. The `AllowanceTransfer` contract handles setting allowances on tokens, giving permissions to spenders on a specified amount for a specified duration of time. Any transfers that then happen through the `AllowanceTransfer` contract will only succeed if the proper permissions have been set.

## [Resources](#resources)

An external [explanation](https://github.com/dragonfly-xyz/useful-solidity-patterns/tree/main/patterns/permit2) of Permit2 contract patterns and example usage.

## [Approving Permit2](#approving-permit2)

Before integrating contracts can request users’ tokens through Permit2, users must approve the Permit2 contract through the specific token contract by calling something like:

``` min-w-full
USDC.approve(permit2Address, totalAmount);
```

To maximize Permit2 utility, users can choose a max approval on the contract where:

``` min-w-full
totalAmount = type(uint256).max;
```

## [FAQ](#faq)

What is the difference between AllowanceTransfer and SignatureTransfer?

Permit2 exposes two independent modules:

- **[AllowanceTransfer](/docs/protocols/permit2/concepts/allowance-transfer)** stores a standing, time-bound allowance inside the Permit2 contract. You set an amount and an expiration for a spender, and that spender can call `transferFrom` repeatedly until the allowance is exhausted or expires. This suits recurring flows such as repeated swaps or subscriptions.
- **[SignatureTransfer](/docs/protocols/permit2/concepts/signature-transfer)** authorizes a single, nonce-scoped transfer through one signature. The permission does not persist after the transaction, so it leaves no standing allowance. Use it when a contract needs tokens infrequently and you want to avoid lingering approvals.

Do I still need a per-token approval to use Permit2?

Yes, but only once per token. Before Permit2 can move a token on a user's behalf, the user makes a one-time standard ERC-20 approval of the Permit2 contract on that token, commonly for the maximum `uint256` amount:

``` min-w-full
USDC.approve(permit2Address, type(uint256).max);
```

After that, Permit2 manages granular, per-spender, time-bound permissions through signatures or its own `approve` function, so integrators no longer trigger a separate onchain approval for every spender.

How is Permit2 different from an EIP-2612 permit?

[EIP-2612](https://eips.ethereum.org/EIPS/eip-2612) adds a `permit` function to a token itself, so it only works for tokens that implement it. Permit2 is a separate contract that works with any ERC-20, including tokens that will never add EIP-2612 support. After the one-time approval of the Permit2 contract, users get signature-based approvals for every such token, plus batching, expirations, and unordered nonces that a bare EIP-2612 permit does not provide.

How do Permit2 nonces and expiration work?

The two modules use different nonce schemes:

- **AllowanceTransfer** packs an incrementing nonce per owner, token, and spender alongside the amount and an expiration timestamp. Two permits with the same nonce do not cancel each other as long as the token or spender differ.
- **SignatureTransfer** uses unordered nonces tracked in a bitmap, so signatures can be spent in any order and each nonce is single-use.

Both carry a signature deadline, and AllowanceTransfer allowances also carry their own `expiration` after which the permission is invalid.

What is the Permit2 contract address, and has it been audited?

Permit2 is deployed at the same address on every chain Uniswap supports **except** zkSync: `0x000000000022D473030F116dDEE9F6B43aC78BA3`.

On zkSync it is `0x0000000000225e31D15943971F47aD3022F714Fa`.

The contracts are open source in the [Uniswap/permit2](https://github.com/Uniswap/permit2) repository, which also publishes the third-party audit reports.

## [Where to Go Next](#where-to-go-next)

- Learn allowance flows in [Allowance Transfer](/docs/protocols/permit2/concepts/allowance-transfer)
- Learn signature flows in [Signature Transfer](/docs/protocols/permit2/concepts/signature-transfer)

[](/docs/protocols/the-compact/resources)

Resources

[](/docs/protocols/permit2/concepts/allowance-transfer)

Allowance Transfer

### On this page

[Resources](#resources)[Approving Permit2](#approving-permit2)[FAQ](#faq)[Where to Go Next](#where-to-go-next)
