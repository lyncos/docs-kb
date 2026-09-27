---
title: CDP × AWS AgentCore - Quickstart Template
description: coinbase / **cdp-agentcore-template** Public
product: Amazon Bedrock AgentCore
section: References / github.com
source_url: https://github.com/coinbase/cdp-agentcore-template
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

[coinbase](/coinbase) / **[cdp-agentcore-template](/coinbase/cdp-agentcore-template)** Public

- [Notifications](/login?return_to=%2Fcoinbase%2Fcdp-agentcore-template) You must be signed in to change notification settings

- [Fork 3](/login?return_to=%2Fcoinbase%2Fcdp-agentcore-template)

- [ Star 3](/login?return_to=%2Fcoinbase%2Fcdp-agentcore-template)

[](/coinbase/cdp-agentcore-template)

main

[Branches](/coinbase/cdp-agentcore-template/branches)[Tags](/coinbase/cdp-agentcore-template/tags)

[](/coinbase/cdp-agentcore-template/branches)[](/coinbase/cdp-agentcore-template/tags)

Go to file

Code

Open more actions menu

## Latest commit

 

## History

[2 Commits](/coinbase/cdp-agentcore-template/commits/main/)

[](/coinbase/cdp-agentcore-template/commits/main/)2 Commits

## Folders and files

[TABLE]

## Repository files navigation

# CDP × AWS AgentCore - Quickstart Template

[](#cdp--aws-agentcore---quickstart-template)

A reference frontend for agent developers integrating [AWS AgentCore](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html) with [Coinbase Developer Platform (CDP)](https://docs.cdp.coinbase.com/) embedded wallets.

> **Note:** This is a reference implementation, not a production-ready codebase. It is an example integration agent developers can clone and adapt.

------------------------------------------------------------------------

## Overview

[](#overview)

AWS AgentCore lets AI agents execute transactions on behalf of users. This app is the user-facing frontend that gives users control over that relationship: they sign in, wallets are created automatically, and they explicitly grant (or revoke) permission for an agent to sign on their behalf.

### Demo

[](#demo)

AgentCore.demo.mp4

Users arrive here to:

1.  **Sign in** - authenticate with email or social login. One CDP embedded EOA wallet (Base) + one Solana wallet are created automatically on first login. No seed phrases or browser extensions required.
2.  **Create additional wallets** - add up to 10 Base EOAs and 10 Solana accounts per user, e.g. one per purpose (savings, agent spending, etc.).
3.  **View balances** - see ETH and USDC on Base, SOL and USDC on Solana for every wallet, with live polling.
4.  **Grant agent access per wallet** - multi-select wallets and authorize an AWS AgentCore agent via [CDP account-scoped delegation](https://docs.cdp.coinbase.com/wallets/using-wallets/delegated-signing). The agent can then sign transactions on each granted wallet without the user being online.
5.  **Test the delegation** - verify the agent can sign on the user's behalf with a live cryptographic proof, per granted wallet.
6.  **Fund wallets** - buy via Coinbase onramp (card, bank transfer, or Coinbase balance), receive via QR, or transfer in from an external wallet (MetaMask, Phantom, Coinbase Wallet, Base Account).
7.  **Transfer out** - send crypto to an external wallet, or sell via Coinbase offramp (payout to bank or Coinbase balance).
8.  **Revoke access** - remove agent permission per wallet at any time.

------------------------------------------------------------------------

## Stack

[](#stack)

|  |  |
|----|----|
| Framework | Next.js 16 (App Router, Turbopack) |
| UI | [`@coinbase/cds-web`](https://www.npmjs.com/package/@coinbase/cds-web) - public Coinbase Design System |
| Auth + wallets | `@coinbase/cdp-react`, `@coinbase/cdp-hooks`, `@coinbase/cdp-core` |
| Server SDK | `@coinbase/cdp-sdk` (`CdpClient`) |
| EVM transfers | `viem` |
| Solana transfers | `@solana/web3.js`, `@solana/spl-token` |
| Onramp / Offramp | CDP FundModal + Coinbase Onramp/Offramp API |
| External wallets | EIP-6963, `@base-org/account` |

------------------------------------------------------------------------

## How it works

[](#how-it-works)

### Delegation flow

[](#delegation-flow)

The core concept: the user grants a time-bound delegation per wallet from the browser, and your agent server can then sign transactions for each granted wallet using only its CDP API credentials - no user session required.

```
sequenceDiagram
    actor User
    participant App as CDP AgentCore App
    participant CDP as CDP
    participant Agent as AWS AgentCore Agent

    User->>App: Sign in (email / social)
    App->>CDP: Auto-create 1 EOA (Base) + 1 Solana account
    CDP-->>App: Wallet addresses
    App-->>User: Dashboard - balances visible

    User->>App: (Optional) Create more wallets
    App->>CDP: createEvmEoaAccount / createSolanaAccount
    CDP-->>App: New wallet address

    User->>App: Multi-select wallets, pick expiry, grant
    loop For each selected wallet
        App->>CDP: createDelegationForAccount({ address, expiresAt })
    end
    Note over CDP: One account-scoped grant<br/>per wallet address
    CDP-->>App: Delegations recorded
    App-->>User: ✓ Per-wallet status updated

    Note over User,Agent: User is now offline - agent acts autonomously

    Agent->>CDP: signEvmMessage / sendEvmTransaction (per address)<br/>(API key + Wallet Secret + active delegation)
    CDP->>CDP: Validate per-address delegation is active and not expired
    CDP-->>Agent: Signature / Transaction hash

    Note over User,Agent: Revoke any time, per wallet

    alt End user revokes one wallet
        User->>App: Revoke (wallet row)
        App->>CDP: revokeDelegationForAccount({ address })
    else Developer revokes
        Agent->>CDP: revokeDelegationForEndUserAccount({ address })
    end
    CDP-->>App: Delegation revoked
```

Loading

### Architecture

[](#architecture)

```
graph TB
    subgraph Browser["User Browser"]
        UI[React UI / CDS components]
        SDK["@coinbase/cdp-react · cdp-hooks · cdp-core"]
        UI --> SDK
    end

    subgraph Server["Next.js Server Routes"]
        Auth[withAuth - CDP JWT verification]
        R1["/api/balances"]
        R2["/api/onramp/*"]
        R3["/api/offramp/*"]
        R4["/api/test-delegation"]
        Auth --> R1 & R2 & R3 & R4
    end

    subgraph CDP["Coinbase Developer Platform"]
        EW[Embedded Wallet API]
        ON[Onramp / Offramp API]
        DS[Delegated Signing]
    end

    subgraph Agent["AWS AgentCore Agent"]
        AG[Agent server - CDP API key auth]
    end

    SDK -->|CDP auth token| Auth
    R1 -->|CdpClient| EW
    R2 & R3 --> ON
    R4 -->|cdp.endUser.signEvmMessage| DS
    AG -->|API key + delegation grant| DS
```

Loading

------------------------------------------------------------------------

## Prerequisites

[](#prerequisites)

- **Node.js 18+**
- A **CDP project** at [portal.cdp.coinbase.com](https://portal.cdp.coinbase.com/)

A couple of one-time Portal toggles are also needed (delegated signing, offramp domain allowlist) — see [Portal setup](#portal-setup) below for the step-by-step.

------------------------------------------------------------------------

## Quickstart

[](#quickstart)

    git clone <this-repo>
    cd cdp-agentcore-demo
    pnpm install
    cp .env.example .env.local
    # fill in .env.local - see Environment variables below
    pnpm dev

Open [http://localhost:3000](http://localhost:3000).

------------------------------------------------------------------------

## Environment variables

[](#environment-variables)

| Variable | Required | Description |
|----|----|----|
| `NEXT_PUBLIC_CDP_PROJECT_ID` | ✅ | CDP project ID - safe to expose client-side |
| `CDP_API_KEY_ID` | ✅ | API key ID - server-side only |
| `CDP_API_KEY_SECRET` | ✅ | API key secret - server-side only |
| `CDP_WALLET_SECRET` | ✅ | Wallet secret - server-side only. Required for delegated signing. |
| `NEXT_PUBLIC_NETWORK_MODE` | optional | `testnet` (default) or `mainnet` |

### Getting your credentials

[](#getting-your-credentials)

1.  Go to [portal.cdp.coinbase.com](https://portal.cdp.coinbase.com/) and open your project
2.  Navigate to **API Keys** and create a new key
3.  Copy the following into `.env.local`:
    - **Project ID** → `NEXT_PUBLIC_CDP_PROJECT_ID`
    - **API key ID** → `CDP_API_KEY_ID`
    - **API key secret** → `CDP_API_KEY_SECRET`
    - **Wallet secret** → `CDP_WALLET_SECRET` ([where to find it](https://docs.cdp.coinbase.com/api-reference/v2/authentication#wallet-secret))

------------------------------------------------------------------------

## Portal setup

[](#portal-setup)

Three one-time configurations in CDP Portal that the app needs to work end-to-end.

### Adding allowed origins (required for sign-in)

[](#adding-allowed-origins-required-for-sign-in)

CDP rejects auth requests from any origin not on your project's allowlist with a `Network Error`. Add the URL you'll be running the app from before the first sign-in attempt.

1.  In CDP Portal, open your project
2.  Go to **Wallets → Embedded Wallets → Security**
3.  Add the origin(s) you'll use:
    - Local dev: `http://localhost:3000` (or whichever port you run on)
    - Production: your deployed URL (e.g. `https://your-app.com`)

### Enabling delegated signing

[](#enabling-delegated-signing)

Delegated signing must be explicitly enabled per project before the agent test (or any backend signing on behalf of an end user) will work.

1.  In CDP Portal, open your project
2.  Go to **Embedded Wallets → Settings**
3.  Enable the **Delegated Signing** toggle

If the call fails with a "delegation not enabled" error, see the [troubleshooting note in the docs](https://docs.cdp.coinbase.com/api-reference/payment-apis/errors#delegation-not-enabled).

### Adding your domain to the Offramp allowlist

[](#adding-your-domain-to-the-offramp-allowlist)

The **Sell (offramp)** flow opens a Coinbase popup that redirects back to `/offramp-complete` on your domain to signal completion. CDP rejects sell-quote requests with an error if the redirect domain isn't allowlisted.

1.  In CDP Portal, open your project
2.  Go to **Onramp & Offramp → Domain allowlist**
3.  Add the domain(s) you'll use:
    - Local dev: `http://localhost:3000`
    - Production: your deployed URL (e.g. `https://your-app.com`)

Skip this step if you're not using the offramp flow.

------------------------------------------------------------------------

## Network mode

[](#network-mode)

`NEXT_PUBLIC_NETWORK_MODE` controls which chains the app targets. Users can toggle this in the UI - the env var sets the default for first-time visitors.

| Value | Base | Solana | Onramp / Offramp |
|----|----|----|----|
| `testnet` (default) | Base Sepolia (84532) | Solana Devnet | Disabled |
| `mainnet` | Base (8453) | Solana mainnet-beta | Enabled |

For testnet funds, use the [CDP Faucet](https://portal.cdp.coinbase.com/products/faucet).

------------------------------------------------------------------------

## Features

[](#features)

### Authentication and wallets

[](#authentication-and-wallets)

Email OTP or social login (Google, Apple). On first login CDP automatically creates:

- **1 EVM EOA** - for ETH and USDC transfers on Base
- **1 Solana account** - for SOL and USDC on Solana

The template is **EOA-only by design** to match the current AgentCore product surface. Because of this, **every Base transaction pays gas in ETH** - including USDC transfers. The wallet needs a small amount of ETH to send anything. On Base mainnet that's typically less than a cent per transfer; on Base Sepolia it's free testnet ETH from the [CDP Faucet](https://portal.cdp.coinbase.com/products/faucet).

Users can create additional EOAs and Solana accounts from the UI - up to 10 of each per the CDP per-user limit. Each wallet has its own delegation grant, so users can scope agent access per wallet (e.g. one wallet for the agent, others kept off-limits).

Powered by [CDP Embedded Wallets](https://docs.cdp.coinbase.com/wallets/non-custodial-wallets/overview) - no seed phrases, no browser extensions.

### Agent permissions (account-scoped delegation)

[](#agent-permissions-account-scoped-delegation)

The core AWS AgentCore integration point. Each wallet gets its own time-bound delegation grant. Multi-select wallets to grant in bulk with a single expiry, or revoke per wallet.

- Multi-select grant: pick one or more wallets, choose an expiry, click Grant - one delegation is created per address
- Per-row Revoke: tear down any grant individually without touching the others
- The **Test agent signing** section proves the active grants work: the server signs a timestamped message per granted wallet using the developer API key and returns the signature

See [CDP delegated signing - account scope](https://docs.cdp.coinbase.com/wallets/using-wallets/delegated-signing).

### Funding

[](#funding)

| Method | Description |
|----|----|
| **Coinbase onramp** | Card or bank via CDP FundModal - mainnet only |
| **QR receive** | Address + QR code for incoming transfers |
| **External wallet** | MetaMask, Phantom, Coinbase Wallet, Base Account (Base); Phantom (Solana) |

### Transfer out

[](#transfer-out)

| Method | Assets | Notes |
|----|----|----|
| **Send to wallet** | ETH, USDC (Base), SOL, USDC (Solana) | Any external address |
| **Sell / offramp** | ETH, USDC on Base; SOL, USDC on Solana | Coinbase fiat payout - mainnet only |

External wallet support by network:

| Wallet | Base | Solana |
|----|----|----|
| MetaMask | ✅ EIP-6963 | ❌ |
| Phantom | ✅ EIP-6963 | ✅ `window.phantom.solana` |
| Coinbase Wallet extension | ✅ EIP-6963 | ❌ |
| Base Account | ✅ `@base-org/account` | ❌ |

------------------------------------------------------------------------

## Testing

[](#testing)

The **Sign test message(s)** button under Agent permissions is the primary integration test. It calls `POST /api/test-delegation` once per granted wallet, which uses `cdp.endUser.signEvmMessage()` or `signSolanaMessage()` with the developer API key. CDP validates each per-address delegation grant and returns a signature - cryptographic proof the agent flow is wired up correctly.

------------------------------------------------------------------------

## Project structure

[](#project-structure)

``` notranslate
src/
├── app/
│   ├── page.tsx                         # Dashboard
│   ├── offramp-complete/page.tsx        # Offramp popup redirect handler
│   └── api/
│       ├── balances/route.ts            # GET token balances (EVM + Solana)
│       ├── onramp/buy-options/          # Available payment methods
│       ├── onramp/buy-quote/            # Onramp session URL
│       ├── offramp/sell-options/        # Available cashout methods
│       ├── offramp/sell-quote/          # Offramp session URL
│       ├── offramp/transactions/        # Offramp transaction status
│       ├── test-delegation/route.ts     # Per-wallet agent signing proof
│       └── solana-rpc/route.ts          # Solana RPC proxy (avoids browser 403s)
│
├── components/
│   ├── balances/BalancesSection.tsx     # Per-wallet cards + Add wallet (per network)
│   ├── permissions/
│   │   ├── PermissionsSection.tsx       # Multi-wallet checklist + multi-select grant
│   │   ├── GrantPermission.tsx          # Expiry picker + bulk grant
│   │   ├── RevokePermission.tsx         # Per-wallet revoke (inline)
│   │   └── AgentTester.tsx              # Per-wallet signing proof
│   ├── funding/
│   │   ├── ExternalWalletFund.tsx       # MetaMask / Phantom transfer
│   │   └── ReceiveModal.tsx             # QR code receive
│   ├── transfer/
│   │   ├── SendToWalletModal.tsx        # Wallet-to-wallet send
│   │   ├── SellModal.tsx                # Offramp flow
│   │   └── OfframpSendModal.tsx         # On-chain send to Coinbase address
│   └── layout/
│       ├── Header.tsx                   # Coinbase × AWS branding + controls
│       └── TestnetBanner.tsx
│
├── hooks/
│   ├── useDelegation.ts                 # Account-scoped delegation (with user-scope fallback)
│   ├── useBalances.ts                   # Balance polling per address
│   ├── useOnramp.ts                     # Buy options + quote
│   ├── useSendAsset.ts                  # Routes sends: EOA (Base) / Solana
│   └── useEip6963Wallets.ts             # External wallet discovery
│
├── lib/
│   ├── network.ts                       # NEXT_PUBLIC_NETWORK_MODE - all chain refs
│   ├── evm-transfer.ts                  # ERC-20 USDC transfer via viem
│   └── solana-transfer.ts              # SPL USDC transfer via @solana/web3.js
│
└── server/
    ├── with-auth.ts                     # CDP JWT middleware for all API routes
    ├── verify-user-token.ts             # JWKS-based JWT verification
    └── cdp-credentials.ts              # Developer JWT for CDP API calls
```

------------------------------------------------------------------------

## Available commands

[](#available-commands)

    pnpm dev         # Dev server with Turbopack
    pnpm build       # Production build + type check
    pnpm lint        # ESLint

------------------------------------------------------------------------

## Related

[](#related)

- [CDP Embedded Wallets](https://docs.cdp.coinbase.com/wallets/non-custodial-wallets/overview)
- [CDP Delegated Signing](https://docs.cdp.coinbase.com/wallets/using-wallets/delegated-signing)
- [CDP Onramp](https://docs.cdp.coinbase.com/onramp-&-offramp/onramp-apis/)
- [CDP Offramp](https://docs.cdp.coinbase.com/onramp/offramp/offramp-integration-guide)
- [AWS AgentCore docs](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html)
- [CDP Portal](https://portal.cdp.coinbase.com/)

------------------------------------------------------------------------

## License

[](#license)

Apache-2.0.

## About

CDP × AWS AgentCore - Next.js starter template that gives AgentCore developers a ready-to-fork wallet UI with Coinbase Developer Platform embedded wallets and account-scoped delegated signing.

### Topics

[agentcore](/topics/agentcore)[aws](/topics/aws)[cdp](/topics/cdp)[coinbase](/topics/coinbase)[delegated-signing](/topics/delegated-signing)[embedded-wallets](/topics/embedded-wallets)[nextjs](/topics/nextjs)[quickstart](/topics/quickstart)[sample-app](/topics/sample-app)[template](/topics/template)

### Resources

[Readme](#readme-ov-file)

[Apache-2.0 license](#Apache-2.0-1-ov-file)

### Contributing

[Contributing](#contributing-ov-file)

### Security policy

[Security policy](#security-ov-file)

[Activity](/coinbase/cdp-agentcore-template/activity)

[Custom properties](/coinbase/cdp-agentcore-template/custom-properties)

### Stars

**3** stars

### Watchers

**0** watching

### Forks

[**3** forks](/coinbase/cdp-agentcore-template/forks)

[Report repository](/contact/report-content?content_url=https%3A%2F%2Fgithub.com%2Fcoinbase%2Fcdp-agentcore-template&report=coinbase+%28user%29)

## Releases

## Packages

## Used by

## Contributors

## Languages
