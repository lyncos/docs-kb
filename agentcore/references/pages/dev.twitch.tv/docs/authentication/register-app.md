---
title: Registering Your App
description: Contents
product: Amazon Bedrock AgentCore
section: References / dev.twitch.tv
source_url: https://dev.twitch.tv/docs/authentication/register-app
fetched: '2026-09-26'
tags:
- agentcore
- dev-twitch-tv
- reference
- related
referenced_by:
- identity-idp-twitch.md
conversion: pandoc
---

[Contents](#)

# Registering Your App

The first step to getting an access token is to register your application (this includes Twitch Extensions and chatbots). To register an application:

1.  Log in to the [developer console](https://dev.twitch.tv/console) using your Twitch account. If you don’t have an account, select the **Sign Up** tab to create one.
    - When you sign up for an account, Twitch sends you an email to verify your account. Be sure to open the email and verify your account before proceeding.
    - You must also enable two-factor authentication (2FA) for your account. To enable 2FA, navigate to [Security and Privacy](https://www.twitch.tv/settings/security), and follow the steps for enabling 2FA under the Security section.
    - You’ll need to refresh your console for these changes to take effect.
2.  Select the **Applications** tab on the developer console and then click **Register Your Application**.
3.  Set **Name** to your application’s name. The name must be unique among all Twitch applications. Your app’s name is listed on the [Connections](https://www.twitch.tv/settings/security) page under **Other Connections** if your app requires user consent to access or modify the user’s resources.
4.  Set **OAuth Redirect URLs** to the callback URL that your app uses for authorizations. After adding your redirect URL, click **Add**.
5.  Select a **Category** (type of application) that your app belongs to.
6.  Click the **I’m not a robot** checkbox.
7.  Click **Create**.
8.  Back in the **Applications** tab, locate your app under **Developer Applications**, and click **Manage**.
9.  Note your **Client ID**, which you’ll use to get your access token and to set the Client-Id header in all API requests. Client IDs are considered public and can be embedded in a web page’s source.
10. Depending on the flow you use to get a token, you may need a client secret. For example, the Authorization Code Grant Flow requires a client secret. Click **New Secret** to generate a secret that you’ll use to get your access token. You must copy the secret and store it somewhere safe. Getting a new secret invalidates the previous secret, which might make your API requests fail until you update your app.

**IMPORTANT** Treat client secrets as you would your password. You must keep it confidential and never expose it to users, even in an obscured form.

**WARNING** Do not share client IDs among applications; each application must have its own client ID. Sharing client IDs among applications may result in the suspension of your application’s access to the Twitch API.

## Next steps

After registering your app, the next step is to [get a token](/docs/authentication/getting-tokens-oauth).

Check out these code samples that show how to get access tokens:

- [Go](https://github.com/twitchdev/authentication-go-sample)
- [Node.js](https://github.com/twitchdev/authentication-node-sample)

Provide feedback for this page

[Docs](https://dev.twitch.tv/docs) [Support](https://dev.twitch.tv/support) [Showcase](https://dev.twitch.tv/showcase) [Announcements](https://discuss.dev.twitch.com/c/announcements/)

[](https://twitter.com/twitchdev) [](https://github.com/twitchdev) [](https://twitch.tv/twitchdev)
