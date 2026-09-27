---
title: AWS AgentCore SDK - Privy Frontend
description: privy-io / **aws-agentcore-sdk** Public
product: Amazon Bedrock AgentCore
section: References / github.com
source_url: https://github.com/privy-io/aws-agentcore-sdk
fetched: '2026-09-26'
tags:
- agentcore
- github-com
- reference
- related
referenced_by:
- payments-fund-wallet.md
conversion: pandoc
---

[privy-io](/privy-io) / **[aws-agentcore-sdk](/privy-io/aws-agentcore-sdk)** Public

- [Notifications](/login?return_to=%2Fprivy-io%2Faws-agentcore-sdk) You must be signed in to change notification settings

- [Fork 1](/login?return_to=%2Fprivy-io%2Faws-agentcore-sdk)

- [ Star 5](/login?return_to=%2Fprivy-io%2Faws-agentcore-sdk)

[](/privy-io/aws-agentcore-sdk)

main

[Branches](/privy-io/aws-agentcore-sdk/branches)[Tags](/privy-io/aws-agentcore-sdk/tags)

[](/privy-io/aws-agentcore-sdk/branches)[](/privy-io/aws-agentcore-sdk/tags)

Go to file

Code

Open more actions menu

## Latest commit

 

## History

[1 Commit](/privy-io/aws-agentcore-sdk/commits/main/)

[](/privy-io/aws-agentcore-sdk/commits/main/)1 Commit

## Folders and files

[TABLE]

## Repository files navigation

# AWS AgentCore SDK - Privy Frontend

[](#aws-agentcore-sdk---privy-frontend)

A reference frontend for agent developers integrating [AWS AgentCore SDK](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html) with [Privy](https://privy.io) as the embedded wallet provider.

> **Note:** This is an open source repository jointly maintained by the [Privy](https://privy.io) team and the AWS AgentCore Bedrock team. It is a representative example of an integration flow intended to help agent developers with their integration. It is **not** a fully productionized codebase.

## Overview

[](#overview)

This app is the user-facing frontend that agent developers can deploy alongside their AgentCore-powered application. Users arrive here to:

1.  **Log in** - authenticate via Privy (email, social, or wallet)
2.  **View their wallets** - see USDC balances on Base and Solana
3.  **Delegate access to the agent** - grant your agent application permission to sign transactions on their behalf
4.  **Fund their wallets** - add USDC via card (Stripe hosted onramp), receiving funds (QR code), or transfer from an external wallet

- **Framework:** Next.js 15.5.x (App Router, Turbopack)
- **Language:** TypeScript
- **Styling:** Tailwind CSS v4
- **Auth + Wallets:** `@privy-io/react-auth`
- **Balance data:** Direct on-chain queries (viem for Base, `@solana/web3.js` for Solana)
- **Package manager:** `pnpm`

------------------------------------------------------------------------

## Prerequisites

[](#prerequisites)

Before starting development on this frontend, please begin onboarding to the [AWS AgentCore SDK](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html). In that onboarding flow, you will be asked to provide the credentials created in the flow below.

## Getting Your Privy Credentials

[](#getting-your-privy-credentials)

### 1. App ID and App Secret

[](#1-app-id-and-app-secret)

1.  Go to the [Privy Dashboard](https://dashboard.privy.io)
2.  Select your app (or create one)
3.  Navigate to **Settings → API keys**
4.  Copy the **App ID** → `NEXT_PUBLIC_PRIVY_APP_ID`
5.  Copy the **App secret** → `PRIVY_APP_SECRET` (treat this like a password - never expose it client-side)

### 2. Authorization Key (Signer ID)

[](#2-authorization-key-signer-id)

The signer ID is the ID of an [**authorization key**](https://docs.privy.io/controls/authorization-keys/keys/create/key#authorization-keys) you create in the Privy dashboard. This is used to grant an agent permission to sign transactions on behalf of a user's wallet.

1.  In the Privy Dashboard, go to **Wallet infrastructure → Authorization**
2.  Click **New key**
3.  Give it a name (e.g. `aws-agent`)
4.  Copy the **Key ID** that is generated → `NEXT_PUBLIC_PRIVY_SIGNER_ID`

> The key ID looks like `zr17anh9dpiqno1iaref9jpx`. It is safe to expose publicly -it is just an identifier, not a secret.

## Paste the `App ID`, `App Secret` and `Signer ID` into the environment file created below.

[](#paste-the-app-id-app-secret-and-signer-id-into-the-environment-file-created-below)

## Environment Variables

[](#environment-variables)

Create a `.env.local` file in the project root with the following:

    # Privy
    NEXT_PUBLIC_PRIVY_APP_ID=        # Your Privy app ID (public)
    PRIVY_APP_SECRET=                # Your Privy app secret (server-only)
    NEXT_PUBLIC_PRIVY_SIGNER_ID=     # Authorization key ID from Privy dashboard (public)

    # Network mode — optional. One of: mainnet | testnet. Defaults to mainnet.
    NEXT_PUBLIC_NETWORK_MODE=testnet

### Network mode (`NEXT_PUBLIC_NETWORK_MODE`)

[](#network-mode-next_public_network_mode)

Controls which chains the app reads balances from, which chains external-wallet transfers target, and whether card funding is enabled. Defaults to `mainnet` if unset, so upgrading without changing your env leaves behavior unchanged.

| Value | Base | Solana | Card funding (Stripe) |
|:---|:---|:---|:---|
| `mainnet` (default) | Base (chain id 8453) | Solana mainnet-beta | ✅ enabled |
| `testnet` | Base Sepolia (chain id 84532) | Solana Devnet | ❌ disabled (Stripe onramp is mainnet-only) |

Start in `testnet` to develop against faucet USDC. See [Running in testnet](#running-in-testnet) below for faucet links. Switch to `mainnet` for production deployments.

------------------------------------------------------------------------

## Funding Wallets

[](#funding-wallets)

This frontend includes flows for allowing the user to add funds to their Ethereum and Solana wallets. At the moment, the flow only reads the balance of USDC on Base in their Ehtereum wallet and USDC on Solana in their Solana wallet. The onramp methods below only support funding with USDC on these chains.

The "Add funds" flow supports three methods:

### Pay with card (Stripe hosted onramp)

[](#pay-with-card-stripe-hosted-onramp)

Clicking "Pay with card" opens [Stripe's hosted onramp](https://docs.stripe.com/crypto/onramp/stripe-hosted) in a new tab. The user selects their destination currency (USDC) and network (Base or Solana) directly in the Stripe UI.

The hosted onramp requires no server-side secret key -it accepts `destination_currency` and `destination_network` as URL query parameters. See the [Stripe hosted onramp docs](https://docs.stripe.com/crypto/onramp/stripe-hosted) for available parameters and customization options.

### Receive (QR code)

[](#receive-qr-code)

Displays a QR code and copyable address for the selected wallet. The QR value uses [EIP-681](https://eips.ethereum.org/EIPS/eip-681) format for Base and the [Solana Pay](https://docs.solanapay.com) SPL token format for Solana.

### Transfer from external wallet

[](#transfer-from-external-wallet)

Connects an external wallet (MetaMask, Phantom, etc.) via Privy's `useConnectWallet` hook and executes a USDC transfer programmatically -ERC-20 `transfer` on Base, SPL token transfer on Solana.

------------------------------------------------------------------------

## Login Methods

[](#login-methods)

Currently, the default login option is email. The full list of login methods can be found [here](https://docs.privy.io/basics/get-started/dashboard/configure-login-methods#configure-login-methods). Some login methods such as SMS and Google Auth need to be explicitly enabled in your Privy Dashboard by going to **User management → Authentication**.

## Setup

[](#setup)

    pnpm install
    pnpm dev

Open [http://localhost:3000](http://localhost:3000).

------------------------------------------------------------------------

## Running in testnet

[](#running-in-testnet)

Set `NEXT_PUBLIC_NETWORK_MODE=testnet` in `.env.local` (the default in `.env.example`) and use these faucets to fund wallets:

| Asset | Network | Faucet |
|:---|:---|:---|
| USDC | Base Sepolia | [Circle Faucet](https://faucet.circle.com) → select "Base Sepolia" |
| USDC | Solana Devnet | [Circle Faucet](https://faucet.circle.com) → select "Solana Devnet" |
| ETH (gas on Base) | Base Sepolia | [Alchemy](https://www.alchemy.com/faucets/base-sepolia), [QuickNode](https://faucet.quicknode.com/base/sepolia) |
| SOL (rent/fees on Solana) | Solana Devnet | [Solana Faucet](https://faucet.solana.com), [Sol Faucet](https://solfaucet.com) |

Base Sepolia gas is microscopic (~0.01 ETH is plenty); Solana rent needs a fraction of a SOL per active account. Funding takes ~30 seconds end to end.

The "Pay with card" option in Add Funds is disabled in testnet — Stripe's hosted onramp only deals in real mainnet USDC. Use the "Transfer from wallet" or "Receive funds" options instead.

------------------------------------------------------------------------

## Available Commands

[](#available-commands)

    pnpm dev      # Start dev server with Turbopack
    pnpm build    # Production build
    pnpm lint     # ESLint

------------------------------------------------------------------------

## Maintainers

[](#maintainers)

This repository is jointly maintained by the [Privy](https://privy.io) team and the AWS AgentCore Bedrock team. See [MAINTAINERS.md](/privy-io/aws-agentcore-sdk/blob/main/MAINTAINERS.md) for the full list of maintainers and contact information.

## Contributions

[](#contributions)

This repository is not currently open to external contributions.

Please submit an Issue and fill out the issue with as much information as possible if you have found a bug in need of fixing.

You can also submit an Issue to request new features, or to suggest changes to existing features.

## License

[](#license)

Apache-2.0. See [LICENSE.md](/privy-io/aws-agentcore-sdk/blob/main/LICENSE.md).

## About

A template frontend for Agent Developers integrating AWS AgentCore SDK with Privy to allow users to login, connect agents, and onramp funds

### Resources

[Readme](#readme-ov-file)

[Apache-2.0 license](#Apache-2.0-1-ov-file)

[Activity](/privy-io/aws-agentcore-sdk/activity)

[Custom properties](/privy-io/aws-agentcore-sdk/custom-properties)

### Stars

**5** stars

### Watchers

**0** watching

### Forks

[**1** fork](/privy-io/aws-agentcore-sdk/forks)

[Report repository](/contact/report-content?content_url=https%3A%2F%2Fgithub.com%2Fprivy-io%2Faws-agentcore-sdk&report=privy-io+%28user%29)

## Releases

## Packages

## Contributors

## Languages
