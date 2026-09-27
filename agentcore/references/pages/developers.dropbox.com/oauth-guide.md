---
title: oauth-guide
description: Dropbox API
product: Amazon Bedrock AgentCore
section: References / developers.dropbox.com
source_url: https://developers.dropbox.com/oauth-guide
fetched: '2026-09-26'
tags:
- agentcore
- developers-dropbox-com
- reference
- related
referenced_by:
- identity-idp-dropbox.md
conversion: pandoc
---

Dropbox API

Dropbox API

Files, sharing, and sync

[Login](/dropbox-api/docs/oauth)

[Documentation](/dropbox-api/docs/get-started/welcome)[API Reference](/dropbox-api/api-reference/overview)

- Get Started

  - [Welcome](/dropbox-api/docs/get-started/welcome)

  - [Quick Start](/dropbox-api/docs/get-started/quick-start)

  - [Authorization](/dropbox-api/docs/get-started/authorization)

  - Tutorial

- Guides

  - [Overview](/dropbox-api/docs/overview)
  - [OAuth](/dropbox-api/docs/oauth)
  - [Authentication Types](/dropbox-api/docs/auth-types)
  - [OpenID Connect](/dropbox-api/docs/oidc)
  - [File Access](/dropbox-api/docs/file-access)
  - [Sharing](/dropbox-api/docs/sharing)
  - [Team Files](/dropbox-api/docs/team-files)
  - [Team Administration](/dropbox-api/docs/team-administration)
  - [Error Handling](/dropbox-api/docs/error-handling)
  - [Performance](/dropbox-api/docs/performance)
  - [Webhooks](/dropbox-api/docs/webhooks)
  - [Detecting Changes](/dropbox-api/docs/detecting-changes)
  - [Extensions](/dropbox-api/docs/extensions)
  - [Paper Migration](/dropbox-api/docs/paper-migration)

- Pre-built Components

  - [Overview](/dropbox-api/docs/pre-built-components/overview)
  - [Chooser](/dropbox-api/docs/pre-built-components/chooser)
  - [Saver](/dropbox-api/docs/pre-built-components/saver)
  - [Embedder](/dropbox-api/docs/pre-built-components/embedder)

- SDKs

  - [Overview](/dropbox-api/docs/sdks/overview)
  - [Swift](/dropbox-api/docs/sdks/swift)
  - [Objective-C](/dropbox-api/docs/sdks/objective-c)
  - [Python](/dropbox-api/docs/sdks/python)
  - [.NET](/dropbox-api/docs/sdks/dotnet)
  - [Java](/dropbox-api/docs/sdks/java)
  - [JavaScript](/dropbox-api/docs/sdks/javascript)
  - [Community SDKs](/dropbox-api/docs/sdks/community-sdks)

- Technical Reference

  - [Encoding for JSON Arguments](/dropbox-api/docs/technical-reference/json-encoding)
  - [Data transport limit](/dropbox-api/docs/technical-reference/data-transport-limit)
  - [Content Hash](/dropbox-api/docs/technical-reference/content-hash)
  - [Request and response formats](/dropbox-api/docs/technical-reference/request-response-formats)
  - [Path Root Header Modes](/dropbox-api/docs/technical-reference/path-root-header-modes)

- Developer Resources

  - [DBX Platform developer guide](/dropbox-api/docs/developer-resources/developer-guide)
  - [Developer branding guide](/dropbox-api/docs/developer-resources/branding-guide)
  - [Dropbox Developer Terms and Conditions](https://www.dropbox.com/developers/reference/tos)

[Community & Support](https://www.dropbox.com/developers/support)[App Console](https://www.dropbox.com/developers/apps)[Dropbox Web](https://www.dropbox.com/)

System

On this page

- [Overview](#overview)
- [Diagram](#diagram)
- [Dropbox API Permissions](#dropbox-api-permissions)
- [Scopes](#scopes)
- [Legacy App Types](#legacy-app-types)
- [Content Access](#content-access)
- [Minimal Access](#minimal-access)
- [Implementing OAuth](#implementing-oauth)
- [Setting up your app](#setting-up-your-app)
- [Testing with a generated token](#testing-with-a-generated-token)
- [SDK Support](#sdk-support)
- [Implementing Code Flow](#implementing-code-flow)
- [Implementing PKCE](#implementing-pkce)
- [Implicit Grant](#implicit-grant)
- [Using User and Team Tokens](#using-user-and-team-tokens)
- [Using Refresh Tokens](#using-refresh-tokens)
- [Summary](#summary)

Scroll to top

On this page

## Overview

When working with the Dropbox APIs, your app will access Dropbox on behalf of your users. You’ll need to have each user of your app sign into dropbox.com to grant your app permission to access their data on Dropbox.

Dropbox uses [OAuth 2.0](http://oauth.net/2/), an open specification, to authorize access to a user’s data. Once completed by a user, the OAuth flow returns an access token to your app. This access token can be used by your app in subsequent API calls for that user. It should be passed with the `Authorization` HTTP header value of `Bearer <oauth2-access-token>`

Note that pre-built components (the [Chooser](/dropbox-api/docs/pre-built-components/chooser), [Saver](/dropbox-api/docs/pre-built-components/saver), and [Embedder](/dropbox-api/docs/pre-built-components/embedder)) are built into the Dropbox web site, and rely on the end-user’s own Dropbox web session, so they don’t require an OAuth flow (or an access token).

### Diagram

Here’s a diagram of an OAuth flow:

![Dropbox OAuth 2 diagram](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/dropbox-api.docs.buildwithfern.com/97133dabaf78517251add2e1b9c1760d1a287044cfa089c6eff08ee9371871ff/docs/assets/migrated/oauth/1b6710839c.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260926%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260926T182223Z&X-Amz-Expires=604800&X-Amz-Signature=cc09f9f06d1ed15ab4193ff9bd9439a9e49716459202242a43f68a47aef9ec64&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Dropbox OAuth 2 diagram

In this flow:

- The user will be redirected to Dropbox to authorize your app to access their Dropbox data.
- After the user has approved your app, they’ll be sent back to your app with an authorization code
- Your application exchanges the authorization code for an access token that can be used to make secure calls to the Dropbox API (not shown)

Your application may then securely store the token for future use. Authorizations may be [revoked](https://help.dropbox.com/installs-integrations/third-party/third-party-apps) by the user, whereas apps may [revoke tokens](/dropbox-api/api-reference/user-endpoints/auth/token-revoke) they receive.

## Dropbox API Permissions

### Scopes

The Dropbox API uses [OAuth scopes](https://oauth.net/2/scope/) to determine the actions your application is allowed to perform on a user’s data. When you create your application in the [](https://www.dropbox.com/developers/apps) [App Console](https://www.dropbox.com/developers/apps), you’ll choose from different scopes in the ‘Permissions’ tab.

![Permissions tab in app settings for a Dropbox app](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/dropbox-api.docs.buildwithfern.com/29f4f3e3aff0e7960997121d0017f2713ceb0ddad52a87cee8507db17f45bac0/docs/assets/migrated/oauth/6de9add5bb.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260926%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260926T182223Z&X-Amz-Expires=604800&X-Amz-Signature=bd72f9633816cb414ce254dba35fbff924653190a36bf2923cf956e19384b789&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Permissions tab in app settings for a Dropbox app

The selected scopes are applied to your access token and determine which API calls your application is allowed to execute. This level of access is then communicated to the end user on the Dropbox app authorization page where the user consents to sharing their data.

Scopes are generally organized into major *actions,* often read and write, on major *objects*. These objects include:

- Account Info
- Files and Folders
- Collaboration (sharing)

For applications using the [Business API](/dropbox-api/api-reference/business-endpoints/overview) to operate on Teams, this also includes:

- Team Info
- Membership
- Group Settings
- Sessions
- Team Data
- The Event log

The scope required for any given API call is [documented on the endpoint:](/dropbox-api/api-reference)

![Required scope field of an endpoint of the Dropbox API](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/dropbox-api.docs.buildwithfern.com/f666de6b7c8740bc4f9efc46ec35bdb84321306b9e502421df63daf9230937c8/docs/assets/migrated/oauth/d8bad8f860.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260926%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260926T182223Z&X-Amz-Expires=604800&X-Amz-Signature=fabd209db56fea27ef8f38901d70ae25f24395c96265ac668e60597b1b2e8190&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Required scope field of an endpoint of the Dropbox API

### Legacy App Types

Prior to the introduction of scopes, Dropbox API apps would select only their level of content access (described below). Business API apps would select from one of four permission types to determine the API calls they have access to:

- **Team information** – Information about the team and aggregate usage data
- **Team auditing** – Team information, plus the team’s detailed activity log
- **Team member file access** – Team information and auditing, plus the ability to [perform any action as any team member](/dropbox-api/api-reference/business-endpoints/overview#member-file-access)
- **Team member management** – Team information, plus the ability to add, edit, and delete team members

For compatibility, these deprecated app types remain selectable - but over the coming months we will begin to transition these apps to equivalent scopes. If you have an existing app on these types, don’t worry - this transition does not require code change.

### Content Access

As you [create](https://www.dropbox.com/developers/apps) your Dropbox application, you will also be prompted to select the scope of file access. Currently, these two options are:

- **App Folder:** Your application will be able to take actions allowed by its scopes on data within its app folder *only* (in the /apps folder). This option is suitable for apps that export content or manage *only* their content.
- **Full Dropbox:** Your application will be able to take actions allowed by its scopes on all data within the user’s Dropbox account. This permission is appropriate when your application needs to regularly access pre-existing content in the user’s account.

### Minimal Access

Always ask for the *least* amount permissions required by your applications. Requesting more scope and content access than required may result in end users not accepting your OAuth request and could impact your [app review process.](/dropbox-api/docs/developer-resources/developer-guide)

When using API scopes, you may also ask for minimal permissions at [authorization time](/dropbox-api/docs/get-started/authorization) - then re-authorize at later time if and when your application requires more permissions from the user.

![Different levels of scopes on a user's authorization page](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/dropbox-api.docs.buildwithfern.com/36f12f17d6d261f07ce246ca9d61e5be8bb04ec0a0561d3acd40c8418d25127f/docs/assets/migrated/oauth/62c2f53ec6.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260926%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260926T182223Z&X-Amz-Expires=604800&X-Amz-Signature=c151001e139efd27f4cd6831d1b2e1c89129fd3a5d3bed55ce3b6964948c7286&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Different levels of scopes on a user's authorization page

Remember, that pre-built components (the [Chooser](/dropbox-api/docs/pre-built-components/chooser), [Saver](/dropbox-api/docs/pre-built-components/saver), and [Embedder](/dropbox-api/docs/pre-built-components/embedder)) are authorized on dropbox.com. You don’t need to manage their access - but the components can be used in conjunction with apps making API calls.

For example, you may discover that using these components for uploading, downloading, or previewing means that you *don’t* need to build functionality and request permission to do this in direct API endpoints.

## Implementing OAuth

### Setting up your app

Before you can get started, you’ll need to register your app with Dropbox by creating a new app in the [App Console](https://www.dropbox.com/developers/apps). That page will guide you through the process of registering your app, selecting permissions, and obtaining an app key and secret (a.k.a. `client_id` and `client_secret`) and inputting redirect URIs.

### Testing with a generated token

If you’d like to quickly test out the Dropbox APIs using your own Dropbox account before implementing OAuth, you can generate an access token from your newly created app in [My apps](https://www.dropbox.com/developers/apps) by pressing the button that says “Generate” in the OAuth 2 section of your app settings page.

![Generate button in OAuth 2 section of app settings](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/dropbox-api.docs.buildwithfern.com/05d03c33297f3deacfa04918f4fef3291831400c60dd08dfe582603779262f14/docs/assets/migrated/oauth/d91967f022.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260926%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260926T182223Z&X-Amz-Expires=604800&X-Amz-Signature=1e7168bb6b553f75286c70092c3cd4c82d23cecd48226b18c2b1b1c029354b3c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Generate button in OAuth 2 section of app settings

Keep in mind that this is only for your own account - you’ll need to use the standard OAuth flow to obtain access tokens for other users.

Do *not* instruct your users to register their own Dropbox application to use your app - you just need to register your app once. Your end-users will connect to that app via the OAuth flow.

### SDK Support

While doc will cover details of OAuth using HTTP calls, remember that [Dropbox SDKs](/dropbox-api/docs/sdks/overview) will take care of some of the OAuth 2 process automatically for you. Using one of these SDKs is recommended when possible. If you’re using one of the SDKs, see their tutorials and sample apps for reference after reviewing this guide.

### Implementing Code Flow

The [code flow](https://oauth.net/2/grant-types/authorization-code/) is the recommended OAuth flow for all types of applications. In order to implement it, your application should:

1.  Construct a Dropbox [authorization URL](/dropbox-api/docs/get-started/authorization#oauth2authorize), with your application’s `client_id` and `redirect_uri` (if applicable) and specifying the `response_type` of `code`, and present it to the user Your Authorization URL should look like: `https://www.dropbox.com/oauth2/authorize?client_id=MY_CLIENT_ID&redirect_uri=MY_REDIRECT_URI&response_type=code`
2.  Wait for the end user to complete authorization on dropbox.com, whom is then redirected back to your URI with an authorization code in the query string
3.  Call the [/oauth2/token](/dropbox-api/docs/get-started/authorization#oauth2token) endpoint with your app’s `client_secret` to exchange the code for an access token in order to make API calls

![Dropbox OAuth 2 code flow](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/dropbox-api.docs.buildwithfern.com/02de9805a9a2b3eded7eca604b4d38d9ca2b7dfc32b349631a42609e336a062f/docs/assets/migrated/oauth/48fdc8f6d4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260926%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260926T182223Z&X-Amz-Expires=604800&X-Amz-Signature=37ebdace64145a7c8d72349975ba1d8210815156b10464e3a548ea030ad891b0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Dropbox OAuth 2 code flow

As you configure redirects, remember:

- You’ll need to register the exact redirect URI(s) your app may use in the [App Console](https://www.dropbox.com/developers/apps) for your application. Dropbox checks that the specified `redirect_uri` parameter in your Authorization URL matches one of the registered values at authorization time.
- The `redirect_uri` is *optional* with the code flow - if unspecified, the authorization code is displayed on dropbox.com for the user to copy and paste to your app.
  - This extra step is less convenient for end users, but appropriate for apps that *cannot* support a redirect.
- If your application needs additional context to complete the redirect, you may pass a `state` parameter the authorization URL - which will be returned as a query parameter in the redirect.

When using the code flow, your app must keep the `client_secret` secure. If your app can’t guarantee it’s security, then we recommend the use of PKCE as described below

### Implementing PKCE

Some types of applications may be unable to keep the `client_secret` secure. This includes, but isn’t restricted to:

- Desktop and mobile apps without a server (which need to include the secret in binaries)
- Single-page applications in pure JavaScript
- Hosted software deployed on untrusted or client infrastructure
- Open source applications

[PKCE](https://oauth.net/2/pkce/) is an open extension to OAuth 2.0, and solves this problem using dynamic codes instead of the static `client_secret`. Your app should construct a random `code_verifier` at authorization time of the user.

Incorporating these codes is similar to the code flow above, with the following additions:

- Your initial string (`code_verifier`) *and* generated value must follow the character restrictions of the spec

  - Regex of permitted characters: `[0-9a-zA-Z\-\.\_\~], {43,128}`

- Include a `code_challenge_method` and `code_challenge` in your authorization URL. The code challenge method may be `S256` or `plain`. Using `S256` is the recommended approach.

  - If the challenge method is `S256`, then the code challenge is created by SHA256 hashing the `code_verifier` and base64 URL encoding the resulting hash
  - If the method is plain, then the `code_verifier` can be used without encryption

- In your request to the [/oauth2/token](/dropbox-api/docs/get-started/authorization#oauth2token) endpoint, pass the `code_verifier` with your generated value *instead of* the `client_id`.

For more information about PKCE, please refer to the blog post, [PKCE: What and Why?](https://dropbox.tech/developers/pkce--what-and-why-)

### Implicit Grant

Prior to the introduction of PKCE, the [implicit grant](https://oauth.net/2/grant-types/implicit/) flow was the recommended solution to applications which cannot secure a `client_secret`.

Dropbox continues to support this legacy flow for compatibility, but recommends PKCE for new apps. You should disable the implicit grant option in App Console if you are not using it.

In the implicit grant flow:

- Your application constructs an [authorization URL](/dropbox-api/docs/get-started/authorization#oauth2authorize) to dropbox.com for the user, with your application’s `client_id` and `response_type` and specifying the `response_type` of `token`

- Once the user authenticates on Dropbox.com, they are redirected back to the specified URI with the access token in the URL fragment.

Your authorization URL should look like:

`https://www.dropbox.com/oauth2/authorize?client_id=MY_CLIENT_ID&redirect_uri=MY_REDIRECT_URI&response_type=code`

In this flow, the `redirect_uri` is *required* and verified in the App Console as described in the code flow.

The Dropbox mobile SDKs previously used the implicit grant, but have been updated to support PKCE.

### Using User and Team Tokens

Apps that request only scopes from the [User API](/dropbox-api/api-reference) will receive a token associated with the user that authorizes the app.

When an app requests team scopes for the [Business API](/dropbox-api/api-reference/business-endpoints/overview), the resulting token is associated with the team (rather than the administrator who authorized it). The user scopes requested as part of the team authorization define the calls that can be used when acting on behalf of a team member with `Dropbox-API-Select-User`.

Apps may request different scopes, per authorization, using the `scopes` parameter in the Authorization URL. For example, user apps may re-authorize to enable additional team functionality.

### Using Refresh Tokens

Dropbox access tokens are short lived, and will expire after a short period of time. The exact expiry time of an access token is returned by the [/oauth2/token](/dropbox-api/docs/get-started/authorization#oauth2token) endpoint (or the redirect URI in implicit grant) - but is generally long enough for a reasonable web session.

If the token expires - throwing a 401 error - your application may simply re-authenticate as described above. If your token is expired, but the user is signed into Dropbox and their [approval is still valid](https://help.dropbox.com/installs-integrations/third-party/third-party-apps), the redirects will not require end-user input. A user’s approval remains valid until explicitly revoked.

Applications that require *offline* access to the API - meaning using the API when the end user is *not* actively interacting through your app - will not be able to prompt for re-authorization. These apps may instead use long-lived [refresh tokens](https://oauth.net/2/grant-types/refresh-token/) can be used to obtain new access tokens.

When using refresh tokens, your call to the [/oauth2/token](/dropbox-api/docs/get-started/authorization#oauth2token) endpoint with the `grant_type` of `authorization_code` will return a short-lived access token and a refresh token, which should be securely stored.

**Note** : you’ll need to include `token_access_type=offline` as a parameter on your Authorization URL in order to return a `refresh_token` inside your access token payload.

To update your access token, call the [/oauth2/token](/dropbox-api/docs/get-started/authorization#oauth2token) endpoint - specifying your `refresh_token` as a parameter and using the `grant_type` of `refresh_token`. The endpoint will return a new short-lived access token and a timestamp indicating its expiration time.

Working with refresh tokens is easier with an SDK. Helper methods accept the refresh token, and manage this update of the short-lived access token for you.

In the past, the Dropbox API used only long-lived access tokens. These are now deprecated, but will remain available as an option in the Developer console for compatibility until mid 2021.

For existing apps migrating to short-lived tokens, the `token_access_type` parameter on your authorization URL enables requesting short-lived tokens per-auth, allowing you to update your code without versioning issues in the Dropbox App Console.

## Summary

There are several implementation options to OAuth - which is best for you will depend on the nature of your application. Dropbox recommends the following:

| If your app is | It should |
|----|----|
| A server-side web application that only calls the Dropbox API as users interact with it | Use the OAuth code flow with short-lived access tokens only (no refresh tokens). |
| A client-side web application (pure Javascript) | Use the OAuth code flow with short-lived access tokens with PKCE (no refresh tokens). |
| A server-side application that requires background access. | Use the OAuth code flow, with refresh tokens. |
| A client-side Desktop app or mobile app that requires background access | Use the OAuth code flow with PKCE, with refresh tokens. |
| Currently using long-lived tokens | Adopt short-lived tokens over the coming months |
| Currently using a legacy app permission type | Convert to a scoped app in the app console |
