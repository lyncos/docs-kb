---
title: Overview
description: Understand how Privy authenticates wallet access using user authentication and API authentication.
product: Amazon Bedrock AgentCore
section: References / docs.privy.io
source_url: https://docs.privy.io/authentication/overview
fetched: '2026-09-26'
tags:
- agentcore
- docs-privy-io
- reference
- related
referenced_by:
- payments-prerequisites.md
- payments-troubleshooting.md
conversion: native-md
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.privy.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Overview

> Understand how Privy authenticates wallet access using user authentication and API authentication.

Privy's wallet system supports granular controls on who can access wallets and what actions different users can perform.

To enforce these controls, Privy's API must verify the identity of the party requesting a wallet action, ensuring that only authorized actions are executed by the system. This process is known as **authentication**.

Privy authenticates individual users to provision access to wallets.

<img src="https://mintcdn.com/privy-c2af3412/TvBDVAWEhg0sbEJZ/images/auth-splash.png?fit=max&auto=format&n=TvBDVAWEhg0sbEJZ&q=85&s=ecebe674810255c6542035f2c60ef015" alt="images/auth-splash.png" width="3686" height="2633" data-path="images/auth-splash.png" />

***

## Individual user authentication

Privy is a powerful toolkit for progressive authentication of individual end users. Fine-grained control over onboarding flows and wallet connections helps improve conversion and craft better UX.

Your app can authenticate users across web2 and web3 accounts, using either an existing authentication provider or Privy's authentication system.

### Using Privy as the authentication provider

If your app doesn't have an existing authentication provider, or needs a single provider for authentication and embedded wallets, your app can use Privy's authentication system, which supports both web2 and web3 accounts.

Privy's client-side SDKs offers a variety of authentication methods, including email, SMS, passkey, socials (Google, Apple, Twitter, Farcaster, etc.), any OAuth system, and Ethereum and Solana wallets.

### Using an existing authentication provider

If your app already has an authentication provider, Privy integrates with your app's [existing authentication system](/authentication/user-authentication/jwt-based-auth/overview). This includes any OIDC compliant authentication system, including OAuth 2.0, Auth0, Firebase, AWS Cognito, and more.

Your app can integrate an existing authentication provider with Privy via the REST API or any of Privy's client-side SDKs.

## Authentication security levels

Privy's login methods fall into two categories based on their trust model:

### Delegated authentication

A third party controls the credential. Account access depends on that provider remaining available and cooperative.

Examples: Google, Apple, Twitter, Discord, Telegram, email OTP, SMS

### Direct authentication

The user owns the credential outright. No third party can revoke or suspend access.

Examples: passkeys (WebAuthn), hardware keys (YubiKey), TOTP authenticator apps

<Warning>
  Account access is wallet access. If your app uses a delegated login method as the primary
  authenticator, Privy recommends requiring MFA with either a passkey or authenticator app. [Set up
  MFA →](/authentication/user-authentication/mfa/overview) | [Security checklist
  →](/security/implementation-guide/security-checklist)
</Warning>

***

## Get started

<CardGroup>
  <Card title="Login users with their email" icon="envelope" href="/authentication/user-authentication/login-methods/email">
    Authenticate users using just their email address and a one-time passcode.
  </Card>

  <Card title="Login with metamask" icon="wallet" href="/authentication/user-authentication/login-methods/wallet">
    Authenticate users with their externally owned Ethereum or Solana wallets.
  </Card>

  <Card title="Set up MFA" icon="fingerprint" href="/authentication/user-authentication/mfa/overview">
    Require passkey or authenticator app MFA to protect delegated logins.
  </Card>

  <Card title="Seamless Farcaster Mini App login" icon="frame" href="/recipes/farcaster/mini-apps">
    Allow your users to sign into your Farcaster Mini App seamlessly with Privy.
  </Card>
</CardGroup>
