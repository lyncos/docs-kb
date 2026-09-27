---
title: Pricing
description: Pay-as-you-go pricing for CDP non-custodial wallets.
product: Amazon Bedrock AgentCore
section: References / docs.cdp.coinbase.com
source_url: https://docs.cdp.coinbase.com/wallets/pricing
fetched: '2026-09-26'
tags:
- agentcore
- docs-cdp-coinbase-com
- reference
- related
referenced_by:
- payments-create-manager.md
conversion: native-md
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.cdp.coinbase.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Pricing

> Pay-as-you-go pricing for CDP non-custodial wallets.

CDP non-custodial wallets use a pay-as-you-go model with no contracts or minimum commitments.

Pricing is consistent across wallet types. The primary implementation difference is your authentication mode:

* **User authentication:** User wallet flows where users authenticate directly in your app.
* **API key authentication:** Backend-authorized wallet flows using API keys and Wallet Secrets.

For architecture and auth guidance, see [Authentication Methods](/wallets/authentication/overview).

Wallet usage is billed in `wallet operations`. A wallet operation is consumed by write actions such as wallet creation, message signing, transaction signing, transaction broadcasting, and policy evaluation.

Read operations are not billed.

| Wallet action                              | Wallet operations |
| ------------------------------------------ | ----------------- |
| Create EVM/Solana account                  | 1                 |
| Create EVM smart account                   | 1                 |
| Sign a message or payload                  | 1                 |
| Send a transaction (sign + broadcast)      | 2                 |
| Create EIP-7702 delegation                 | 2                 |
| Policy evaluation (API key auth workflows) | 1                 |

Each wallet operation costs **\$0.005**.

### Free tier

The first **5,000 wallet operations per month** are free.

### Billing

Usage is billed at the beginning of each calendar month for the previous month. Invoices are available in the Billing tab in [CDP Portal](https://portal.cdp.coinbase.com/).
