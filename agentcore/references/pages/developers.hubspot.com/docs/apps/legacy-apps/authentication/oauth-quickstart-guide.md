---
title: Working with OAuth | OAuth Quickstart Guide
description: Learn how set up OAuth for your app using this quickstart Guide and sample Node.js app.
product: Amazon Bedrock AgentCore
section: References / developers.hubspot.com
source_url: https://developers.hubspot.com/docs/apps/legacy-apps/authentication/oauth-quickstart-guide
fetched: '2026-09-26'
tags:
- agentcore
- developers-hubspot-com
- reference
- related
referenced_by:
- identity-idp-hubspot.md
conversion: native-md
---

> ## Documentation Index
> Fetch the complete documentation index at: https://developers.hubspot.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

---
id: a9369ad8-0b6a-411c-8951-d15b9518f06d
---

# Working with OAuth | OAuth Quickstart Guide

> Learn how set up OAuth for your app using this quickstart Guide and sample Node.js app.

<Warning>
  This authentication guide pertains to [legacy public apps](/docs/apps/legacy-apps/public-apps/overview). For the OAuth quickstart guide focused on apps built on the new developer platform, check out [this article](/docs/apps/developer-platform/build-apps/authentication/oauth/oauth-quickstart-guide) instead.
</Warning>

## Before you get started

Before you can start using OAuth with HubSpot, you'll need to have:

* [A developer account](/docs/getting-started/account-types)
* [An app](/docs/apps/legacy-apps/public-apps/overview) associated with your developer account
* A HubSpot account to install your app in (you can use an existing account or [create a test account](/docs/getting-started/account-types))

<Warning>
  You must be a [Super Admin](https://knowledge.hubspot.com/user-management/hubspot-user-permissions-guide#super-admin) to install an app in a HubSpot account.
</Warning>

### How it works

HubSpot supports the [OAuth 2.0 Authorization Code grant type](https://developer.okta.com/blog/2018/04/10/oauth-authorization-code-grant-type), which can be broken down into four basic steps:

1. Your app opens a browser window to send the user to the HubSpot OAuth 2.0 server
2. The user reviews the requested permissions and grants the app access
3. The user is redirected back to the app with an authorization code in the query string
4. The app sends a request to the OAuth 2.0 server to exchange the authorization code for an access token

### In this guide

* [Quickstart App](#quickstart-app): A Node.js demo app that authenticates with HubSpot's OAuth 2.0 server
* [Getting OAuth tokens](#getting-oauth-tokens): How to authorize your app with users
* [Using OAuth tokens](#using-oauth-tokens): How to make queries with a token
* [Refreshing OAuth tokens](#refreshing-oauth-tokens): How to use the refresh token provided by HubSpot

<Info>
  All code examples in this guide are written in JavaScript (Node.js)
</Info>

## Quickstart app

If this is your first time using OAuth authentication with HubSpot's APIs, it's strongly recommended that you check out the [OAuth 2.0 Quickstart App](https://github.com/HubSpot/oauth-quickstart-nodejs), written in Node.js. This sample app is designed to get you started using OAuth 2.0 as quickly as possible by demonstrating all the steps outlined below in the [getting OAuth tokens section](#getting-oauth-tokens) below.

<Card title="Get the quickstart app" href="https://github.com/HubSpot/oauth-quickstart-nodejs" icon="github" horizontal />

## Getting OAuth tokens

### 1. Create the authorization URL and direct the user to HubSpot's OAuth 2.0 server

When sending a user to HubSpot's OAuth 2.0 server, the first step is creating the authorization URL. This will identify your app and define the resources (scopes) it's requesting access to on behalf of the user. The query parameters you can pass as part of an authorization URL are shown in the table below. For more detailed information on this step, read the [reference doc](/docs/apps/legacy-apps/authentication/working-with-oauth).

<p className="table-key">
  Fields marked with <span style={{ color: 'red' }}>\*</span> are required.
</p>

| Parameter                                           | Description                                                                                                                                               | Example                                 |
| --------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------- |
| `client_id`<span style={{color:"red"}}>\*</span>    | The client ID identifies your app. Find it on your app's settings page.                                                                                   | `7fff1e36-2d40-4ae1-bbb1-5266d59564fb`  |
| `scope`<span style={{color:"red"}}>\*</span>        | The [scopes](/docs/apps/legacy-apps/authentication/scopes#list-of-available-scopes) your application is requesting, separated by URL-encoded spaces (`%20`).   | `oauth%20crm.objects.contacts.read`     |
| `redirect_uri`<span style={{color:"red"}}>\*</span> | The URL that the user will be redirected to after they authorize your app for the requested scopes. **For production applications, `https` is required.** | `https://www.example.com/auth-callback` |
| `optional_scope`                                    | The scopes that are optional for your app, and will be dropped if the selected HubSpot portal does not have access to those products                      | `automation`                            |
| `state`                                             | A unique string value that can be used to maintain the user's state when they're redirected back to your app.                                             | `WeHH_yy2irpl8UYAvv-my`                 |

Once you've created your URL, start the OAuth connection process by sending the user to it.

The code blocks below provide examples of using different redirect types:

**Using a server-side redirect:**

```js theme={null}
// Build the auth URL
const authUrl =
  "https://app.hubspot.com/oauth/authorize" +
  `?client_id=${encodeURIComponent(CLIENT_ID)}` +
  `&scope=${encodeURIComponent(SCOPES)}` +
  `&redirect_uri=${encodeURIComponent(REDIRECT_URI)}` +
  `&state=${encodeURIComponent(STATE)}`;

// Redirect the user
return res.redirect(authUrl);
```

**Using an HTML link:**

```html theme={null}
<a
  href="https://app.hubspot.com/oauth/authorize?scope=contacts%20social&redirect_uri=https://www.example.com/auth-callback&client_id=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx&state=xxxxxxxx"
  >Install</a
>
```

**Encoding an additional redirect user state:**

Some apps may need to redirect the user to different locations. For example, an app may wish to redirect users to different subdomains of their integration (e.g. `userA.integration.com` and `userB.integration.com`). To do so, use the `state` parameter to encode more information about the user state:

1\. Generate and store a nonce value for the state parameter.

2\. Store the user's state in a local datastore using the nonce as its key.

3\. Include the nonce value as the state parameter in the authorization URL.

4\. When the user authenticates and is redirected to your redirect URL, validate the state parameter and use it as the key to retrieve the user state that was stored.

5\. From there, redirect the user as needed (e.g. redirecting again to a user specific URL).

### 2. HubSpot prompts user for consent

HubSpot displays a consent window to the user showing the name of your app and a short description of the HubSpot API services it's requesting permission to access. The user can then grant access to your app.

<Frame>
  <img src="https://www.hubspot.com/hubfs/Knowledge_Base_2023/%5BExample%5D%20Install%20Screen.png" alt="Example installation prompt window" />
</Frame>

**Note:** The user installing the app must have access to all requested scopes. If they don't have the required access, the installation will fail and they will be directed to an error page. If a user sees this permissions error page, they'll need to have a Super Admin install the app.

Your application doesn't do anything at this stage. Once access is granted, the HubSpot OAuth 2.0 server will send a request to the callback URI defined in the authorization URL.

### 3. Handle the OAuth server response

When the user has completed the consent prompt from Step 2, the OAuth 2.0 server sends a `GET` request to the redirect URI specified in your authentication URL. If there are no issues and the user approves the access request, the request to the redirect URI will be returned with a `code` query parameter attached. If the user doesn't grant access, no request will be sent.

**Example:**

```js theme={null}
app.get("/oauth-callback", async (req, res) => {
  if (req.query.code) {
    // Handle the received code
  }
});
```

### 4. Exchange authorization code for tokens

After your app receives an authorization code from the OAuth 2.0 server, it can exchange that code for an access and refresh token by sending a URL-form encoded `POST` request to `https://api.hubapi.com/oauth/v1/token` with the values shown below. For more detailed information on this step, take a minute to read this [reference doc](/docs/api-reference/legacy/authentication/oauth-tokens/v1/guide).

| Parameter       | Description                                               | Example                                 |
| --------------- | --------------------------------------------------------- | --------------------------------------- |
| `grant_type`    | Must be `authorization_code`                              | `authorization_code`                    |
| `client_id`     | Your app's client ID                                      | `7fff1e36-2d40-4ae1-bbb1-5266d59564fb`  |
| `client_secret` | Your app's client secret                                  | `7c3ce02c-0f0c-4c9f-9700-92440c9bdf2d`  |
| `redirect_uri`  | The redirect URI from when the user authorized your app   | `https://www.example.com/auth-callback` |
| `code`          | The authorization code received from the OAuth 2.0 server | `5771f587-2fe7-40e8-8784-042fb4bc2c31`  |

**Example:**

```js theme={null}
const formData = {
  grant_type: 'authorization_code',
  client_id: CLIENT_ID,
  client_secret: CLIENT_SECRET,
  redirect_uri: REDIRECT_URI,
  code: req.query.code
};

request.post('https://api.hubapi.com/oauth/v1/token', { form: formData }, (err, data) => {
  // Handle the returned tokens
});
```

The body of the token response will be JSON data with the form:

```json theme={null}
{
  "refresh_token": "6f18f21e-a743-4509-b7fd-1a5e632fffa1",
  "access_token": "CN2zlYnmLBICAQIYgZXFLyCWp1Yoy_9GMhkAgddk-zDc-H_rOad1X2s6Qv3fmG1spSY0Og0ACgJBAAADAIADAAABQhkAgddk-03q2qdkwdXbYWCoB9g3LA97OJ9I",
  "expires_in": 1800
}
```

<Warning>
  **Please note:**

  The access token will expire after the number of seconds given in the `expires_in` field of the response, currently 30 minutes. For details on getting a new access token, see the [Refreshing OAuth tokens](#refreshing-oauth-tokens) section below.
</Warning>

## Using OAuth tokens

Once the authorization code flow is completed, your app is authorized to make requests on behalf of the user. To do this, provide the token as a bearer token in the `Authorization` HTTP header. Specific details can be found in the [reference doc](/docs/api-reference/legacy/authentication/oauth-tokens/v1/guide).

**Example:**

```js theme={null}
request.get(
  "https://api.hubapi.com/contacts/v1/lists/all/contacts/all?count=1",
  {
    headers: {
      Authorization: `Bearer ${ACCESS_TOKEN}`,
      "Content-Type": "application/json",
    },
  },
  (err, data) => {
    // Handle the API response
  }
);
```

<Warning>
  **Please note:**

  Access tokens reflect the scopes requested from the app and do not reflect the permissions or limitations of what a user can do in their HubSpot account. For example, if a user has permissions to view only owned contacts but authorizes a request for the `crm.objects.contacts.read` scope, the resulting access token can view all contacts in the account and not only those owned by the authorizing user.
</Warning>

## Refreshing OAuth tokens

OAuth access tokens expire periodically. This is to make sure that if they're compromised, attackers will only have access for a short time. The token's lifespan in seconds is specified in the `expires_in` field when an authorization code is exchanged for an access token.

Your app can exchange the received refresh token for a new access token by sending a URL-form encoded `POST` request to `https://api.hubapi.com/oauth/v1/token` with the values below. For more detailed information on this step, check out the [reference doc](/docs/api-reference/legacy/authentication/oauth-tokens/v1/guide).

| Parameter       | Description                                                  | Example                                 |
| --------------- | ------------------------------------------------------------ | --------------------------------------- |
| `grant_type`    | Must be `refresh_token`                                      | `refresh_token`                         |
| `client_id`     | Your app's client ID                                         | `7fff1e36-2d40-4ae1-bbb1-5266d59564fb`  |
| `client_secret` | Your app's client secret                                     | `7c3ce02c-0f0c-4c9f-9700-92440c9bdf2d`  |
| `redirect_uri`  | The redirect URI from when the user authorized your app      | `https://www.example.com/auth-callback` |
| `refresh_token` | The refresh token received when the user authorized your app | `b9443019-30fe-4df1-a67e-3d75cbd0f726`  |

**Example:**

```js theme={null}
const formData = {
  grant_type: 'refresh_token',
  client_id: CLIENT_ID,
  client_secret: CLIENT_SECRET,
  redirect_uri: REDIRECT_URI,
  refresh_token: REFRESH_TOKEN
};

request.post('https://api.hubapi.com/oauth/v1/token', { form: formData }, (err, data) => {
  // Handle the returned tokens
});
```

The body of the token response will be JSON data with the form:

```json theme={null}
{
  "refresh_token": "6f18f21e-a743-4509-b7fd-1a5e632fffa1",
  "access_token": "CN2zlYnmLBICAQIYgZXFLyCWp1Yoy_9GMhkAgddk-zDc-H_rOad1X2s6Qv3fmG1spSY0Og0ACgJBAAADAIADAAABQhkAgddk-03q2qdkwdXbYWCoB9g3LA97OJ9I",
  "expires_in": 1800
}
```

The new access token can then be used to make calls on behalf of the user. When the new token expires, you can follow the same steps again to retrieve a new one.

## Related articles

[Auth methods on HubSpot](/docs/apps/legacy-apps/authentication/intro-to-auth)

[Working with OAuth](/docs/apps/legacy-apps/authentication/working-with-oauth)

[Manage tokens](/docs/api-reference/legacy/authentication/oauth-tokens/v1/guide)
