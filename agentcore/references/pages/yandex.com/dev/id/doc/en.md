---
title: About
description: Yandex ID — is a single account to access all Yandex services. API Yandex ID you can set up user authorization via the OAuth 2.0 protocol on your website or in your mobile app.
product: Amazon Bedrock AgentCore
section: References / yandex.com
source_url: https://yandex.com/dev/id/doc/en
fetched: '2026-09-26'
tags:
- agentcore
- reference
- related
- yandex-com
referenced_by:
- identity-idp-yandex.md
conversion: pandoc
---

# About

- [How it works](en/#how-it-works)
- [Useful links](en/#useful-links)

[Yandex ID](https://yandex.com/support/id/index.html) — is a single account to access all Yandex services. API Yandex ID you can set up user authorization via the [OAuth 2.0 protocol](en/concepts/ya-oauth-intro) on your website or in your mobile app.

API Yandex ID makes interaction with your website easier:

- Users can authorize with their Yandex account. They won't have to create a new account and fill out additional forms.
- Developers will be able to identify the user and use information from their Yandex account to personalize the app's content and interface. Permissions granted to each app are limited to those that were specified by the developer when [registering](en/register-client) the app.
- You can use the [instant authorization technology](en/suggest-description) for a website or the [SDK Yandex ID library](en/mobileauthsdk/about) for mobile devices to implement the login system.

See [OAuth implementation at Yandex](en/concepts/ya-oauth-intro) for information about the basic OAuth concepts and the features specific to Yandex.

Tip

To make your service more trustworthy to users, [verify your account via Gosuslugi](en/confirm-account).

## [](en/#how-it-works)How it works

1.  When authorizing in your app, the user chooses logging in with their Yandex account.

Screenshot

![](https://cdn-viewer.diplodoc.com/docs-assets/dev-id/rev/r21194166/en/_assets/log-in.png)

1.  The app [connected to API Yandex ID](en/how-to) redirects the user to Yandex OAuth and requests access to their Yandex account data. The user confirms logging in with their Yandex account and allows access to their data.

Screenshot

![](https://cdn-viewer.diplodoc.com/docs-assets/dev-id/rev/r21194166/en/_assets/confirm-data-2.png)

1.  The app [obtains an OAuth token](en/access) with permissions enabling it to access API Yandex ID. Then a request can be sent to API Yandex ID to retrieve the following user data:

    - Login, first name, last name, and gender.
    - User's profile picture.
    - Email address.
    - Phone number.
    - Date of birth.

2.  The app sends a request to API Yandex ID specifying the OAuth token it received and gets the [unique user ID and their data](en/user-information).

3.  The app authorizes the user using the settings and content linked to the ID it received. This way, Yandex users get an account in your app without creating a new account.

## [](en/#useful-links)Useful links

- [OAuth implementation at Yandex](en/concepts/ya-oauth-intro)
- [Connecting to API Yandex ID](en/how-to)
- [SDK Yandex ID for mobile apps](en/mobileauthsdk/about)

### Was the article helpful?

Yes

No
