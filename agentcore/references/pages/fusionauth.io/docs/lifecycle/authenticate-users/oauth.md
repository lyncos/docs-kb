---
title: OAuth
description: An overview of how FusionAuth provides an OAuth 2.0 and OpenID Connect SSO login system.
product: Amazon Bedrock AgentCore
section: References / fusionauth.io
source_url: https://fusionauth.io/docs/lifecycle/authenticate-users/oauth
fetched: '2026-09-26'
tags:
- agentcore
- fusionauth-io
- reference
- related
referenced_by:
- identity-idp-fusionauth.md
conversion: native-md
---

# OAuth

An overview of how FusionAuth provides an OAuth 2.0 and OpenID Connect SSO login system.

> For the index of this section of the site, see [llms.txt](https://fusionauth.io/docs/llms.txt)

FusionAuth supports the following grant types as defined by the OAuth 2.0 framework in [RFC 6749](https://tools.ietf.org/html/rfc6749), [RFC 8628](https://tools.ietf.org/html/rfc8628), [RFC 9207](https://www.rfc-editor.org/rfc/rfc9207), and [OpenID Connect Core](https://openid.net/specs/openid-connect-core-1_0.html).

*   Authorization Code Grant
*   Implicit Grant
*   Password Grant (also referred to as the Resource Owner Credentials Grant)
*   Refresh Token Grant
*   Client Credentials Grant
*   Device Authorization Grant

To begin using the FusionAuth login system, start by configuring your Application for OAuth2.

To begin using the Client Credentials grant, start by configuring Entities.

It is recommended to utilize the Authorization Code Grant unless you have a technical requirement that makes a different grant a better choice. The following outline some example login flows.

*   [Example Authorization Code Grant](https://fusionauth.io/docs/lifecycle/authenticate-users/oauth.md#example-authorization-code-grant)
*   [Example Implicit Grant](https://fusionauth.io/docs/lifecycle/authenticate-users/oauth.md#example-implicit-grant)
*   [Example Password Grant](https://fusionauth.io/docs/lifecycle/authenticate-users/oauth.md#example-resource-owner-password-credentials-grant)
*   [Example Refresh Token Grant](https://fusionauth.io/docs/lifecycle/authenticate-users/oauth.md#example-refresh-token-grant)
*   [Example Client Credentials Grant](https://fusionauth.io/docs/lifecycle/authenticate-users/oauth.md#example-client-credentials-grant)
*   [Example Device Authorization Grant](https://fusionauth.io/docs/lifecycle/authenticate-users/oauth.md#example-device-authorization-grant)

You can also learn about [OAuth Modes](https://fusionauth.io/docs/lifecycle/authenticate-users/oauth/modes.md), which are different methods of using OAuth that are higher level than the individual grants.

You can also learn about [Response Modes](https://fusionauth.io/docs/lifecycle/authenticate-users/oauth/response-modes.md), which control how authorization response parameters are delivered to the client (`query`, `fragment`, or `form_post`).

## Configure Application OAuth Settings

Navigate to the Application configuration from the main menu, Applications .

If you have already created a FusionAuth Application for the purpose of your application, you do not need to create another, however you will still need to complete the OAuth configuration. If an application has not yet been created, click Add and name your application accordingly and fill out the OAuth configuration.

In this example you will see we have created a new Application named `Pied Piper` and have filled out the fields in the OAuth Configuration tab. A FusionAuth application represents an authenticated resource that you will be using with FusionAuth.

Additional OAuth controls can be managed through [Tenant Configuration](https://fusionauth.io/docs/get-started/core-concepts/types/tenants.md#tenant-configuration).

![Application OAuth Configuration](https://fusionauth.io/img/docs/lifecycle/authenticate-users/oauth/oauth-application.png)

### OAuth Form Fields

`Client Id`

*   Read only

The unique client identifier as defined by [RFC 6749 Section 2.2](https://tools.ietf.org/html/rfc6749#section-2.2). This value is read only and is equal to the unique Id of the Application.

`Client secret`

*   Read only

The client secret as defined by [RFC 6749 Section 2.3.1](https://tools.ietf.org/html/rfc6749#section-2.3.1). When **Client Authentication** is `Required`, this client secret will be required to obtain an access token from the Token endpoint.

This value may be regenerated if you think it has been compromised by clicking the regenerate button. If this Application is configured to require client authentication, regenerating the client secret will cause all clients to fail, and they will not be able to complete the OAuth login process. If this Application is not configured to require client authentication, regenerating this secret will not have any effect.

`Client Authentication`

*   optional
*   Available since 1.28.0

This selector allows you to set a rule for accessing the [Token endpoint](https://fusionauth.io/docs/apis/oauth/token.md).

The possible values are:

*   `Required` - The `client_secret` parameter must be used. This is the default setting. In most cases you will not want to change this setting.
*   `Not required` - Use of the `client_secret` parameter is optional.
*   `Not required when using PKCE` - Requires the use of the `client_secret` parameter unless a valid PKCE [code\verifier](https://datatracker.ietf.org/doc/html/rfc7636#section-4.1) parameter is used. This is useful for scenarios where you have a requirement to make a request to the Token endpoint where you cannot safely secure a client secret such as native mobile applications and single page applications (SPAs) running in a browser. In these scenarios it is recommended you use PKCE.

See the [Token endpoint](https://fusionauth.io/docs/apis/oauth/token.md) for more information.

`PKCE`

*   optional
*   Available since 1.28.0

This selector allows you to set a rule for [Proof Key for Code Exchange](https://datatracker.ietf.org/doc/html/rfc7636) (or PKCE) requirements when using the authorization code grant.

The possible values are:

*   `Required` - The `code_verifier` parameter must be used. If you want to require PKCE for this application, set **PKCE** to this value.
*   `Not required` - Use of the `code_verifier` parameter is optional. This is the default setting.
*   `Not required when using client authentication` - Requires the use of the `code_verifier` parameter unless a valid `client_secret` parameter is used.

`Generate refresh tokens`

*   Available since 1.3.0

When enabled, FusionAuth will return a refresh token when the `offline_access` scope has been requested. When this setting is disabled refresh tokens will not be generated even if the `offline_access` scope is requested.

In order to use the Refresh Token with the Refresh Grant to refresh a token, you must ensure that the `Refresh Token` grant is enabled. See the **Enabled grants** field.

`Enable debug logging`

*   optional
*   Available since 1.25.0

Enable debug to create an event log to assist you in debugging integration errors.

`URL validation`

*   optional
*   Available since 1.43.0

Controls the validation policy for **Authorized redirect URLs** and **Authorized request origin URLs**.

The possible values are:

*   `Exact match` - Only the configured values that do not contain wildcards are considered for validation. Values during OAuth 2.0 workflows must match a configured value exactly.
*   `Allow wildcards` - Configured values with and without wildcards are considered for validation. Values during OAuth 2.0 workflows can be matched against wildcard patterns or exactly match a configured value.

`Authorized redirect URLs`

*   optional

When OAuth grants, such as the authorization code grant, require a browser redirect to a URL found in the `redirect_uri` parameter, the destination URLs must be added to this list. URLs that are not authorized may not be utilized in the `redirect_uri` parameter or the `post_logout_redirect_uri` parameter.

You can add as many URLs as you'd like to this list. Prior to version `1.43.0` only exact string matches with the provided `redirect_uri` will be allowed. No partial or wildcard matches will be accepted.

Available since `1.43.0`

Configured URLs containing wildcards are considered during validation when **Authorized redirect URLs** is set to `Allow wildcards`. Wildcards are allowed in the following positions:

*   The left-most subdomain - A full or partial wildcard is allowed in the left-most subdomain. The replacement value cannot contain a `.`.
*   The port number - A wildcard is allowed in place of the port number. Partial wildcards are not allowed in this position.
*   A path segment - A full or partial wildcard is allowed in any path segment. The replacement value cannot contain a `/`.
*   A query string value - A wildcard is allowed in place of a query string value. Partial wildcards are not allowed in this position. Wildcards are not allowed in query string names.

See the OAuth 2.0 [URL Validation](https://fusionauth.io/docs/lifecycle/authenticate-users/oauth/url-validation.md) page for more detail.

`Authorized request origin URLs`

*   optional

This optional configuration allows you to restrict the origin of an OAuth2 / OpenID Connect grant request. If no origins are registered for this Application, all origins are allowed.

By default FusionAuth will add the `X-Frame-Options: DENY` HTTP response header to the login pages to keep these pages from being rendered in an iframe. If the request comes from an authorized origin, however, FusionAuth will not add this header to the response. To load FusionAuth hosted login pages in an iframe, you will need to add the request origin to this configuration.

Available since `1.43.0`

Configured URLs containing wildcards are considered during validation when **Authorized request origin URLs** is set to `Allow wildcards`. Wildcards are allowed in the following positions:

*   The left-most subdomain - A full or partial wildcard is allowed in the left-most subdomain. The replacement value cannot contain a `.`.
*   The port number - A wildcard is allowed in place of the port number. Partial wildcards are not allowed in this position.
*   A path segment - A full or partial wildcard is allowed in any path segment. The replacement value cannot contain a `/`.
*   A query string value - A wildcard is allowed in place of a query string value. Partial wildcards are not allowed in this position. Wildcards are not allowed in query string names.

See the OAuth 2.0 [URL Validation](https://fusionauth.io/docs/lifecycle/authenticate-users/oauth/url-validation.md) page for more detail.

`Authorized resource URIs`

*   optional
*   Available since 1.67.0

An optional list of allowed resource server URIs for this Application, per [RFC 8707 (Resource Indicators for OAuth 2.0)](https://www.rfc-editor.org/rfc/rfc8707.html). Defaults to an empty list.

Each URI must be an absolute URI and may not contain a fragment (`#`). When this list is non-empty, clients may pass a `resource` parameter during the OAuth authorize and token flows to request access tokens scoped to a specific resource server. These flows only accept URIs present in this list; all other values return an `invalid_target` error.

When this list is empty (the default), FusionAuth silently ignores any `resource` parameter sent by the client; existing application behavior is unchanged.

Examples of valid resource URIs:

*   `https://api.example.com`
*   `https://mcp.example.com/v2/api`

`Logout URL`

*   optional

The optional logout URL for this Application. When provided this logout URL should handle the logout of a user in your application.

If you need to end an HTTP session or delete cookies to logout a user from your application, these operations should be handled by this URL. When the `/oauth2/logout` endpoint is retrieved, each Logout URL registered for Applications in this tenant will be called within an iframe to complete the SSO logout.

If the OAuth2 logout endpoint is used with this Client Id, this configured Logout URL will be also utilized as the redirect URL. This behavior only occurs when the `post_logout_redirect_uri` parameter is not provided.

If this Application has not defined a Logout URL, the value configured at the Tenant level will be used. If no Logout URL has been configured, a redirect to `/` will occur. A specific redirect URL may also be provided by using the `post_logout_redirect_uri` request parameter.

See the [Logout endpoint](https://fusionauth.io/docs/apis/oauth/logout.md) or the [Logout And Session Management guide](https://fusionauth.io/docs/lifecycle/authenticate-users/logout-session-management.md) for more information.

`Logout behavior`

*   optional
*   Available since 1.11.0

This selector allows you to modify the behavior when using the [Logout endpoint](https://fusionauth.io/docs/apis/oauth/logout.md) with this Client Id.

The possible values are:

*   `All applications` - This is the default behavior. Upon Logout of the FusionAuth SSO, call each registered Logout URLs for the entire tenant and then redirect to the Logout URL registered for this application.
*   `Redirect only` - Do not call each registered Logout URL in the tenant, instead logout out of the FusionAuth SSO and then only redirect to the Logout URL registered for this application.

See the [Logout endpoint](https://fusionauth.io/docs/apis/oauth/logout.md) for more information.

`Enabled grants`

*   optional
*   Available since 1.5.0

The enabled OAuth2 grants. If a grant is not enabled and a client requests this grant during authentication an error will be returned to the caller indicating the grant is not enabled.

*   Authorization Code
*   Device
*   Implicit
*   Password
*   Refresh Token

When creating a new Application, the `Authorization Code` and `Refresh Token` grants will be enabled by default. See The [OAuth 2.0 & OpenID Connect Overview](https://fusionauth.io/docs/lifecycle/authenticate-users/oauth.md) for additional information on each of these grants.

`Device Verification URL`

*   optional
*   Available since 1.11.0

The URL to be returned during the Device Authorization request to be displayed to the end user. This URL will be where the end user navigates in order to complete the device authentication workflow.

This field is required if `Device` is enabled in the OAuth **Enabled grants** for this Application and hidden when not.

`Require registration to complete OAuth authorization`

*   optional
*   Available since 1.28.0

When enabled the user will be required to be registered, or complete registration before redirecting to the configured callback in the authorization code grant or the implicit grant. This configuration does not affect any other grant, and does not affect the API usage.

`UserInfo populate lambda`

*   optional
*   Available since 1.50.0

The lambda to be invoked during the generation of the UserInfo response when provided a token associated with this Application. See [UserInfo populate lambda](https://fusionauth.io/docs/extend/code/lambdas/userinfo-populate.md).

### OAuth Scopes

The supported OAuth grant types that involve user interaction allow specifying a space-delimited set of OAuth scopes via the **scope** request parameter. See [Scopes](https://fusionauth.io/docs/lifecycle/authenticate-users/oauth/scopes.md) for more information on configuring the application's OAuth scope policies, managing custom OAuth scopes, and prompting for user consent to granting scopes to third-party applications.

## Configure Entities

> **PLAN:** This feature requires [at least a Starter plan](https://fusionauth.io/docs/get-started/core-concepts/plans-features.md#starter-features).

The Client Credentials grant takes place between two Entities. You can learn more about [Entities](https://fusionauth.io/docs/get-started/core-concepts/types/entity-management.md) in the Core Concepts section.

There are two entities which take part in a Client Credentials grant in FusionAuth: the recipient Entity and the target Entity.

Imagine you have a todo API which lets you create, read, update, and delete todos. You also have an email API, which lets you send emails. You can represent these both in FusionAuth as Entities.

When building functionality to allow the todo API to send email reminders, grant permissions on the email API (the target Entity) to the todo API (the recipient Entity). To set up this relationship:

*   Create an API entity type with the following permissions: `execute` and `configure`.
*   Create a todo API entity
*   Create an email API entity
*   Grant the todo API `execute` permissions on the email API

The todo API is the recipient Entity, because it receives the permissions to call the email API. The email API is the target Entity, because it will process the token. The email API is the system to which access is controlled.

The set up happens once and then the todo API can perform the client credentials grant any time it needs to call the email API. It will get a token at the end of a successful grant and can present that to the email API.

You may configure Entities and Grants via the FusionAuth API or the administrative user interface. You can specify the **Client Id** and **Client Secret** if desired.

Below is the creation screen for an Entity:

![Setting up an Entity](https://fusionauth.io/img/docs/lifecycle/authenticate-users/oauth/add-entity-client-credentials.png)

Below is the management screen for an Entity where you'd add or remove Grants:

![Adding a Grant to an Entity](https://fusionauth.io/img/docs/lifecycle/authenticate-users/oauth/add-grant.png)

Here's an example of adding a Grant to an Entity via the API:

Example Grant Request

```shell
API_KEY=...
TARGET_ENTITY_ID=e13365f1-a270-493e-bd1b-3d239d753d53
RECIPIENT_ENTITY_ID=2934f41f-d277-4a32-b0d5-16e47dad9721

curl \
  -XPOST \
  -H "content-type: application/json" \
  -H "Authorization: $API_KEY"  \
  'https://local.fusionauth.io/api/entity/'$TARGET_ENTITY_ID'/grant' -d'
{
  "grant": {
    "recipientEntityId": "'$RECIPIENT_ENTITY_ID'",
    "permissions" : ["read","write"]
  }
}
'
```

Next, learn how to perform a [Client Credentials Grant](https://fusionauth.io/docs/lifecycle/authenticate-users/oauth.md#example-client-credentials-grant).

## Example Authorization Code Grant

Note

Mobile applications require additional security in implementing the Authorization Code Grant Flow due to inability to safely store a client-secret and the potential of the authorization code being intercepted.

For these reasons, it is best practice to implement the Authorization Code Grant Flow with [Proof Key for Code Exchange](https://tools.ietf.org/html/rfc7636) (PKCE, pronounced "pixie").

Review the [Authorization](https://fusionauth.io/docs/apis/oauth/authorize.md) and [Token](https://fusionauth.io/docs/apis/oauth/token.md) endpoint documentation for additional detail on these necessary request parameters.

### Point your application to the authorize endpoint

Now that your FusionAuth application has been configured to use the OAuth provider, you may now point the login for your application to the FusionAuth authorize endpoint which will now handle user authentication.

For the purposes of this example, I will make the assumption that FusionAuth App is running locally at `http://localhost:9011`, the `client_id` will be found on the OAuth tab in the application configuration, the `redirect_uri` will be where you wish FusionAuth to redirect the browser when the authorization step has completed. This value will need to be predefined in the authorized redirect URLs in the OAuth configuration. The `response_type` will always be `code` for this grant type. The `tenantId` will be the unique Id of the tenant this request is scoped for, the tenant's configured theme will be applied.

Review the [Authorization](https://fusionauth.io/docs/apis/oauth/authorize.md) endpoint documentation for more detail.

```plaintext
http://localhost:9011/oauth2/authorize?client_id=06494b74-a796-4723-af44-1bdb96b48875&redirect_uri=https://www.piedpiper.com/login&response_type=code&tenantId=78dda1c8-14d4-4c98-be75-0ccef244297d
```

### Consume the authorization code returned from the authorize request

When the authorize request completes successfully it will respond with a status code of `302` to the location provided by the redirect\_uri parameter. The request will contain a code parameter which can be exchanged for an access token. The access token contains the user Id of the authenticated user which can then be used to retrieve the entire user object.

Review the [Token](https://fusionauth.io/docs/apis/oauth/token.md) endpoint documentation for more detail. The following is an example redirect URI containing the authorization code.

```plaintext
https://www.piedpiper.com/login?code=+WYT3XemV4f81ghHi4V+RyNwvATDaD4FIj0BpfFC4Wzg=&iss=https%3A%2F%2Fpiedpiper.fusionauth.io&userState=Authenticated
```

### Exchange the authorization code for an access token

The last step to complete the authentication process and retrieve the user's Id is to exchange the returned authorization code for an access token. The JSON response will contain the user Id of the authenticated user.

If the authorization code grant is being implemented in a Single Page App (SPA), the token request should be made by the application server in order to keep the client secret secure from introspection of the client code.

Line breaks have been added for readability.

Example HTTP Request

```plaintext
POST /oauth2/token HTTP/1.1
Host: piedpiper.fusionauth.io
Content-Type: application/x-www-form-urlencoded
Accept: */*
Content-Length: 436
client_id=3c219e58-ed0e-4b18-ad48-f4f92793ae32
    &code=+WYT3XemV4f81ghHi4V+RyNwvATDaD4FIj0BpfFC4Wzg
    &grant_type=authorization_code
    &redirect_uri=https%3A%2F%2Fwww.piedpiper.com%2Flogin
```

Example HTTP Response

```json
{
  "access_token" : "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE0ODUxNDA5ODQsImlhdCI6MTQ4NTEzNzM4NCwiaXNzIjoiYWNtZS5jb20iLCJzdWIiOiIyOWFjMGMxOC0wYjRhLTQyY2YtODJmYy0wM2Q1NzAzMThhMWQiLCJhcHBsaWNhdGlvbklkIjoiNzkxMDM3MzQtOTdhYi00ZDFhLWFmMzctZTAwNmQwNWQyOTUyIiwicm9sZXMiOltdfQ.Mp0Pcwsz5VECK11Kf2ZZNF_SMKu5CgBeLN9ZOP04kZo",
  "expires_in" : 3600,
  "token_type" : "Bearer",
  "userId" : "3b6d2f70-4821-4694-ac89-60333c9c4165"
}
```

### Verify Authorization

If you only need to validate registration and User roles, this can be done by inspecting the JWT payload as returned in the `access_token` property of the response body.

If you require the entire User object to validate authorization, you may need to retrieve the entire User. The User may be retrieved in one of several ways. If you have an API key you can retrieve the User by Id or email, these two values are returned in the JWT payload. The email address is returned in the `email` identity claim, and the User's Id is returned in the `sub` identity claim. You may also retrieve the User without an API key by utilizing the JWT as returned in the `access_token` property in the response body.

See the [Retrieve a User](https://fusionauth.io/docs/apis/users/retrieve.md) API for examples.

You may also choose to use the [Introspect](https://fusionauth.io/docs/apis/oauth/introspect.md) or [Userinfo](https://fusionauth.io/docs/apis/oauth/userinfo.md) endpoints to validate the access token returned from the Token endpoint and to provide you decoded claims as a JSON object.

Now that you have the user, or retrieved the roles from the JWT, you may review their roles and registration to ensure they have adequate authority for the intended action, and if the user is not yet registered for the requested application, you can either fail their login, or complete a registration workflow. Once you have determined a user can be logged into your application, you'll need to log them into your application. For a web based application, this generally will include creating an HTTP session and storing the user in the newly created session.

### Log Out

To log the user out, a typical workflow would include first logging out of your application, if that is successful, you would then log the user out of FusionAuth. This is accomplished by making a `GET` request to the `/oauth2/logout` endpoint. The logout request will complete with a `302` redirect to the configured logout URL.

Line breaks have been added for readability.

Example HTTP Response

```plaintext
GET /oauth2/logout?
      client_id=06494b74-a796-4723-af44-1bdb96b48875
      &tenantId=78dda1c8-14d4-4c98-be75-0ccef244297d HTTP/1.1
Host: piedpiper.fusionauth.io
```

Example HTTP Request

```plaintext
HTTP/1.1 302 Found
Location: https://www.piedpiper.com
```

## Example Implicit Grant

Caution

Always prefer the Authorization Code Grant over the Implicit Grant. We provide the Implicit Grant for compatibility with existing integrations, but the we do not recommend using this grant for new development for the following reasons:

*   this grant type returns the access token in the URL as a fragment, which is susceptible to interception
*   the client (the browser) does not have a secure way to store the token, which makes the token susceptible to theft

The Implicit Grant is similar to the Authorization grant, instead of exchanging a code for an access token, the token is provided in response to the initial authorization request.

### Make the authorization request to the authorization server

Make a `GET` request to the Authorize endpoint with the `client_id` and `redirect_uri`. The `response_type` will always be `token`. Below is an example HTTP request.

Line breaks have been added for readability.

Example HTTP Request

```plaintext
GET /oauth2/authorize?
      client_id=3c219e58-ed0e-4b18-ad48-f4f92793ae32
      &response_type=token
      &redirect_uri=https%3A%2F%2Fwww.piedpiper.com%2Fcallback
Host: piedpiper.fusionauth.io
```

Upon successful authentication, a redirect to the configured **redirect\_uri** will be made with an **access\_token** as one of the redirect parameters. The following is an example HTTP 302 redirect, with line breaks added to improve readability. The redirect from an Implicit Grant will contain parameters after the fragment delimiter, `#`.

HTTP Redirect Response

```plaintext
HTTP/1.1 302 Found
Location: https://piedpiper.com/callback#
           access_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE0ODUxNDA5ODQsImlhdCI6MTQ4NTEzNzM4NCwiaXNzIjoiYWNtZS5jb20iLCJzdWIiOiIyOWFjMGMxOC0wYjRhLTQyY2YtODJmYy0wM2Q1NzAzMThhMWQiLCJhcHBsaWNhdGlvbklkIjoiNzkxMDM3MzQtOTdhYi00ZDFhLWFmMzctZTAwNmQwNWQyOTUyIiwicm9sZXMiOltdfQ.Mp0Pcwsz5VECK11Kf2ZZNF_SMKu5CgBeLN9ZOP04kZo
           &expires_in=3599
           &iss=https%3A%2F%2Fpiedpiper.fusionauth.io
           &locale=fr
           &token_type=Bearer
           &userState=Authenticated
```

## Example Resource Owner Password Credentials Grant

Note

*Note*

The Authorization Code Grant is nearly always preferred over the Resource Owner Password Credentials Grant. This grant is provided for compatibility with existing integrations but the use of this grant is not recommended.

The use of this grant removes the delegation pattern intended in the OAuth 2 framework. This means that you no longer will be delegating to FusionAuth to collect user credentials, instead you will be collecting the credentials and passing them to FusionAuth.

The Resource Owner Password Credentials Grant, also referred to as the Password Grant allows you to obtain an access token by directly providing the user credentials to the Token endpoint. This grant may also be used to receive a refresh token by specifying the `offline_access` scope.

### Exchange the user credentials for an access token

Once you have collected the user's email and password you will make a `POST` request to the Token endpoint. Below is an example HTTP request where the user's email is `richard@piedpiper.com` and password is `disrupt`. The `grant_type` will always be `password`.

Line breaks have been added for readability.

Example HTTP Request

```plaintext
POST /oauth2/token HTTP/1.1
Host: piedpiper.fusionauth.io
Content-Type: application/x-www-form-urlencoded
Accept: */*
Content-Length: 436
client_id=3c219e58-ed0e-4b18-ad48-f4f92793ae32
    &grant_type=password
    &username=richard%40piedpiper.com
    &password=disrupt
    &scope=offline_access
```

Example HTTP Response

```json
{
  "access_token" : "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE0ODUxNDA5ODQsImlhdCI6MTQ4NTEzNzM4NCwiaXNzIjoiYWNtZS5jb20iLCJzdWIiOiIyOWFjMGMxOC0wYjRhLTQyY2YtODJmYy0wM2Q1NzAzMThhMWQiLCJhcHBsaWNhdGlvbklkIjoiNzkxMDM3MzQtOTdhYi00ZDFhLWFmMzctZTAwNmQwNWQyOTUyIiwicm9sZXMiOltdfQ.Mp0Pcwsz5VECK11Kf2ZZNF_SMKu5CgBeLN9ZOP04kZo",
  "expires_in" : 3600,
  "refresh_token": "Nu00yJrGw0qlBJNUz2S6LJ3KZFN7uw6Dj4C2mnzF4I6wkM5xingxuw",
  "token_type" : "Bearer",
  "userId" : "3b6d2f70-4821-4694-ac89-60333c9c4165"
}
```

## Example Refresh Token Grant

An access token is designed to have a short time-to-live (TTL). A related refresh token with a longer TTL can be used for generating new access tokens and extending a user's session. The application's OAuth settings must be configured with "Generate refresh tokens" enabled, and "Refresh Token" as an "Enabled grant".

### Exchange a refresh token for an access token

With a refresh token obtained from a previous call to the /Authorize endpoint, a new access token may be generated with a `POST` request to the Token endpoint. Below is an example HTTP request, the `grant_type` will always be `refresh_token`.

Line breaks have been added for readability.

Example HTTP Request

```plaintext
POST /oauth2/token HTTP/1.1
Host: piedpiper.fusionauth.io
Content-Type: application/x-www-form-urlencoded
Accept: */*
Content-Length: 436
client_id=3c219e58-ed0e-4b18-ad48-f4f92793ae32
    &grant_type=refresh_token
    &refresh_token=Nu00yJrGw0qlBJNUz2S6LJ3KZFN7uw6Dj4C2mnzF4I6wkM5xingxuw
```

Example HTTP Response

```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImVjZWUzMTYyZjAifQ.eyJhdWQiOiI4YmY4YWIwYy1iMWNlLTQ0NjUtYmQzNy1jMTU1MThjYWU2YmQiLCJleHAiOjE1NzA0ODQwNTcsImlhdCI6MTU3MDQ4MDQ1NywiaXNzIjoiYWNtZS5jb20iLCJzdWIiOiJhZjRiMzk2Yy01MGM4LTQwNzQtOTA5YS0zYzgwNjU0OTEzMzUiLCJhdXRoZW50aWNhdGlvblR5cGUiOiJSRUZSRVNIX1RPS0VOIiwiZW1haWwiOiJqb2huQGRvZS5pbyIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJqb2hubnkxMjMiLCJyb2xlcyI6WyJjb21tdW5pdHlfaGVscGVyIiwidXNlciJdLCJhcHBsaWNhdGlvbklkIjoiOGJmOGFiMGMtYjFjZS00NDY1LWJkMzctYzE1NTE4Y2FlNmJkIn0.laSlkKQMOwZmfI_3NT3-1F_VdpLL-ceCQZ2fRL1lvF4",
  "expires_in": 3600,
  "scope": "offline_access",
  "token_type": "Bearer",
  "userId": "3b6d2f70-4821-4694-ac89-60333c9c4165"
}
```

## Example Client Credentials Grant

> **PLAN:** This feature requires [at least a Starter plan](https://fusionauth.io/docs/get-started/core-concepts/plans-features.md#starter-features).

Most OAuth grants are designed to allow users to delegate permissions.

The Client Credentials grant allows entities to authenticate and receive access tokens with no user interaction.

Therefore, unlike other grants, the Client Credentials grant isn't configured in an Application. Instead, it occurs between two Entities. [Learn more about setting up Entities](https://fusionauth.io/docs/lifecycle/authenticate-users/oauth.md#configure-entities).

Here's a short video showing one possible usage of this grant.

[Play](https://youtube.com/watch?v=pJIzYLSTrMM)

### Exchange credentials for an access token

An access token may be generated with a `POST` request to the Token endpoint. Below is an example HTTP request, the `grant_type` will always be `client_credentials`.

Line breaks have been added for readability.

Example HTTP Request

```plaintext
POST /oauth2/token HTTP/1.1
Host: piedpiper.fusionauth.io
Authorization: Basic MDkyZGJkZWQtMzBhZi00MTQ5LTljNjEtYjU3OGYyYzcyZjU5OitmY1hldDlJdTJrUWk2MXlXRDlUdTRSZVoxMTNQNnlFQWtyMzJ2NldLT1E9
Content-Type: application/x-www-form-urlencoded
Accept: */*
Content-Length: 436

grant_type=client_credentials
    &scope=target-entity%3Ae13365f1-a270-493e-bd1b-3d239d753d53%3Aread
```

```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjM0ZjE3ZDdiNzIifQ.eyJhdWQiOiJlMTMzNjVmMS1hMjcwLTQ5M2UtYmQxYi0zZDIzOWQ3NTNkNTMiLCJleHAiOjE2MjAyMzc3MjksImlhdCI6MTYyMDIzNDEyOSwiaXNzIjoiaHR0cHM6Ly9sb2NhbC5mdXNpb25hdXRoLmlvIiwic3ViIjoiMjkzNGY0MWYtZDI3Ny00YTMyLWIwZDUtMTZlNDdkYWQ5NzIxIiwianRpIjoiMGIwMmY1MDktYmNmMy00YjhkLWEzZGItMDNmOThhY2U5ZDlmIiwicGVybWlzc2lvbnMiOnsiZTEzMzY1ZjEtYTI3MC00OTNlLWJkMWItM2QyMzlkNzUzZDUzIjpbInJlYWQiXX19.1BR367JxpWp33HuHEY0_zHuVDmnYrgi7CzzjlIYwtqQ",
  "expires_in": 3599,
  "scope": "target-entity:e13365f1-a270-493e-bd1b-3d239d753d53:read",
  "token_type": "Bearer"
}
```

### Client Credentials Scopes

In order for permissions to be correctly determined, pass a **scope** parameter. This parameter can have multiple values, space separated. Each value has this format:

```plaintext
target-entity:entity_id:permission
```

where `entity_id` is a required entity UUID and `permission` is an optional, comma separated list of permissions.

You will typically provide a scope specifying a target entity:

```plaintext
target-entity:92dbded-30af-4149-9c61-b578f2c72600
```

You may provide append a comma separated list of permissions as well:

```plaintext
target-entity:92dbded-30af-4149-9c61-b578f2c72600:read,write
```

You may combine multiple entities and permissions in the same **scope** parameter:

```plaintext
target-entity:92dbded-30af-4149-9c61-b578f2c72600:read,write target-entity:119a84d9-06c5-4d1f-a0d4-a60490b70ac5:read
```

The **scope** will be checked against previously granted permissions. If all requested permissions have been found, the grant succeeds and an **access\_token** is returned.

If you do not pass **scope**, you will still get an **access\_token** if the request is authorized. The token will omit the following claims:

*   `aud`
*   `permissions`

Permissions associated with the grant from the target entity to the recipient entity will be available in the `permissions` claim in the token. If specific permissions are requested, the recipient entity must have previously been granted all of those permissions for a successful access request. If specific permissions are requested, only the requested permissions will be in the `permissions` claim, otherwise all permissions will be available in that claim.

You can see all claims of the token in the [Token documentation](https://fusionauth.io/docs/lifecycle/authenticate-users/oauth/tokens.md).

## Example Device Authorization Grant

This example contains screenshots of our [Device Grant Example](https://github.com/FusionAuth/fusionauth-example-device-grant) which may be a useful code reference during implementation.

### Device Authorization Grant Configuration

In order to leverage FusionAuth for the Device Authorization Grant, the Device Grant must be enabled and the Device Verification URL must be set. See the [Configure Application OAuth Settings](#configure-application-oauth-settings) section above.

FusionAuth requires that the Device Verification URL be a page that you control within your application so that a required Tenant Id is provided throughout the grant flow. While you may host your own form on this page, FusionAuth provides a themed OAuth device template that may be redirected to from your application to complete the user-interaction portion of the Device Authorization Grant as a convenience. This template is located at `/oauth2/device`. With the required request parameters being `client_id` and `tenantId`. On submission of the OAuth device template the end-user is prompted to authenticate using the Authorization Grant flow. This will redirect to the configured OAuth **redirect\_uri** per the typical Authorization Grant flow. The Device Authorization Grant will be considered approved when the Authorization Grant **code** has been exchanged for a token.

Default values are provided for the durations that the device code and user code remain valid, as well as the user code generator settings. These values may be adjusted through the Advanced tab of [Tenant Configuration](https://fusionauth.io/docs/get-started/core-concepts/types/tenants.md#advanced).

### Initiate the Device Authorization Grant flow

In order to initiate the Device Authorization Grant flow, make a request from the device to the [Device Authorize endpoint](https://fusionauth.io/docs/apis/oauth/device.md), which is also discoverable via the [OpenID Configuration](https://fusionauth.io/docs/apis/oauth/openid-configuration.md).

This request may be made with the optional **scope** field in order to request OAuth scopes on tokens from the eventual [/oauth2/token endpoint](https://fusionauth.io/docs/apis/oauth/token.md#complete-the-device-authorization-grant-request) return. A refresh token can be requested by including `offline_access` in the **scope** request parameter. The **scope** value here will be used for the interactive portion of the workflow when the [user\code is passed to FusionAuth](https://fusionauth.io/docs/lifecycle/authenticate-users/oauth.md#pass-user_code-to-fusionauth). See [Scopes](https://fusionauth.io/docs/lifecycle/authenticate-users/oauth/scopes.md) for more information on configuring the application's OAuth scope policies, managing custom OAuth scopes, and prompting for user consent to granting scopes to third-party applications.

This request will return a JSON response with values necessary to fulfill the remainder of the grant flow.

![OAuth Device Example - Connect](https://fusionauth.io/img/docs/lifecycle/authenticate-users/oauth/oauth-device-connect.png)

Line breaks have been added for readability.

Example HTTP Request

```plaintext
POST /oauth2/device_authorize HTTP/1.1
Host: piedpiper.fusionauth.io
Content-Type: application/x-www-form-urlencoded
Accept: */*
Content-Length: 67
client_id=3c219e58-ed0e-4b18-ad48-f4f92793ae32
    &scope=offline_access
```

Example JSON Response

```json
{
  "device_code": "e6f_lF1rG_yroI0DxeQB5OrLDKU18lrDhFXeQqIKAjg",
  "expires_in": 600,
  "interval": 5,
  "user_code": "SFYNPV",
  "verification_uri": "http://localhost:9011/oauth2/device",
  "verification_uri_complete": "http://localhost:9011/oauth2/device?user_code=SFYNPV"
}
```

### Poll Token endpoint

Upon receiving a response from the Device Authorize endpoint the device may begin polling the [Token endpoint](https://fusionauth.io/docs/apis/oauth/token.md#complete-the-device-authorization-grant-request) with the **device\_code** at the requested **interval** in seconds returned in the response. Requests to the [Token endpoint](https://fusionauth.io/docs/apis/oauth/token.md#complete-the-device-authorization-grant-request) will return an error stating that authorization is pending, until the end-user approves the request, at which point an access token will be returned.

Line breaks have been added for readability.

Example HTTP Request

```plaintext
POST /oauth2/token HTTP/1.1
Host: piedpiper.fusionauth.io
Content-Type: application/x-www-form-urlencoded
Accept: */*
Content-Length: 166
client_id=3c219e58-ed0e-4b18-ad48-f4f92793ae32
    &device_code=e6f_lF1rG_yroI0DxeQB5OrLDKU18lrDhFXeQqIKAjg
    &grant_type=urn%3Aietf%3Aparams%3Aoauth%3Agrant-type%3Adevice_code
```

Example pending JSON Error Response

```json
{
  "error": "authorization_pending",
  "error_description": "The authorization request is still pending"
}
```

Example expired JSON Error Response

```json
{
  "error": "expired_token",
  "error_description": "The device_code has expired, and the device authorization session has concluded."
}
```

Example invalid JSON Error Response

```json
{
  "error": "invalid_request",
  "error_reason": "invalid_device_code",
  "error_description": "The request has an invalid parameter: device_code"
}
```

### User-interaction

Upon receiving a response from the Device Authorize endpoint the device may display to the end-user the **user\_code** and a prompt to navigate to the **verification\_uri**. The **verification\_uri\_complete** is provided as a convenience so that the device may display a QR code used to navigate the end-user to the user-interaction page with a pre-populated **user\_code** in the form.

![OAuth Device Example - Display Code](https://fusionauth.io/img/docs/lifecycle/authenticate-users/oauth/oauth-device-display-code.png)

The user should then navigate to the displayed URL, and enter the activation code.

![OAuth Device Example - User Interaction](https://fusionauth.io/img/docs/lifecycle/authenticate-users/oauth/oauth-device-user-interaction.png)

### Pass `user_code` to FusionAuth

Once the `user_code` has been received from the end-user, it may be validated by making a request to the [Device Validate endpoint](https://fusionauth.io/docs/apis/oauth/device.md#device-validate). This endpoint will return a `200` response code without a JSON body on successful validation.

Upon validating the end-user provided `user_code` the typical Authorization Grant, Implicit Grant, or Password Grant flows may be followed for authentication. The OAuth endpoints that facilitate these typical OAuth flows take a `user_code` parameter to facilitate the Device Authorization Grant approval. See the [Authorize endpoint](https://fusionauth.io/docs/apis/oauth/authorize.md) and [Token endpoint](https://fusionauth.io/docs/apis/oauth/token.md) documentation for more information.

![OAuth Device Example - Success](https://fusionauth.io/img/docs/lifecycle/authenticate-users/oauth/oauth-device-success.png)

### Receive `access_token`

Once the user has provided a valid `user_code` and successfully authenticated, the request from the device to the [Token endpoint](https://fusionauth.io/docs/apis/oauth/token.md#complete-the-device-authorization-grant-request) will return successfully with an access token.

Line breaks have been added for readability.

Example HTTP Request

```plaintext
POST /oauth2/token HTTP/1.1
Host: piedpiper.fusionauth.io
Content-Type: application/x-www-form-urlencoded
Accept: */*
Content-Length: 166
client_id=3c219e58-ed0e-4b18-ad48-f4f92793ae32
    &device_code=e6f_lF1rG_yroI0DxeQB5OrLDKU18lrDhFXeQqIKAjg
    &grant_type=urn%3Aietf%3Aparams%3Aoauth%3Agrant-type%3Adevice_code
```

Example JSON Response

```json
{
  "access_token" : "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE0ODUxNDA5ODQsImlhdCI6MTQ4NTEzNzM4NCwiaXNzIjoiYWNtZS5jb20iLCJzdWIiOiIyOWFjMGMxOC0wYjRhLTQyY2YtODJmYy0wM2Q1NzAzMThhMWQiLCJhcHBsaWNhdGlvbklkIjoiNzkxMDM3MzQtOTdhYi00ZDFhLWFmMzctZTAwNmQwNWQyOTUyIiwicm9sZXMiOltdfQ.Mp0Pcwsz5VECK11Kf2ZZNF_SMKu5CgBeLN9ZOP04kZo",
  "expires_in" : 3600,
  "id_token" : "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE0ODUxNDA5ODQsImlhdCI6MTQ4NTEzNzM4NCwiaXNzIjoiYWNtZS5jb20iLCJzdWIiOiIyOWFjMGMxOC0wYjRhLTQyY2YtODJmYy0wM2Q1NzAzMThhMWQiLCJhcHBsaWNhdGlvbklkIjoiNzkxMDM3MzQtOTdhYi00ZDFhLWFmMzctZTAwNmQwNWQyOTUyIiwicm9sZXMiOltdfQ.Mp0Pcwsz5VECK11Kf2ZZNF_SMKu5CgBeLN9ZOP04kZo",
  "refresh_token": "ze9fi6Y9sMSf3yWp3aaO2w7AMav2MFdiMIi2GObrAi-i3248oo0jTQ",
  "token_type" : "Bearer",
  "userId" : "3b6d2f70-4821-4694-ac89-60333c9c4165"
}
```

Related

[APIs Authorize API API documentation for the FusionAuth Authorize OAuth2 endpoint. oauthoauth 2.0](https://fusionauth.io/docs/apis/oauth/authorize.md)

[APIs Client Secret Reference Client Secret reference for FusionAuth OAuth2 endpoints. oauthoauth 2.0](https://fusionauth.io/docs/apis/oauth/client-secret.md)

[APIs Device API API documentation for the FusionAuth Device OAuth2 endpoint. oauthoauth 2.0](https://fusionauth.io/docs/apis/oauth/device.md)

[APIs OAuth2 API This page details FusionAuth's OAuth2 endpoints. Learn about the Authorization Code grant, \Implicit\ grant, and other OAuth2 grants. oauth2oauth 2.0](https://fusionauth.io/docs/apis/oauth.md)
---

## Other pages in Authenticate Users

> For the full index of this section, see [Lifecycle](https://fusionauth.io/docs/llms-lifecycle.txt).

- [Application Authentication Tokens](https://fusionauth.io/docs/lifecycle/authenticate-users/application-authentication-tokens.md): Leverage Application specific authentication tokens to speed up certain authentication tasks.
- [Contextual Multi-Factor Authentication (MFA)](https://fusionauth.io/docs/lifecycle/authenticate-users/contextual-multi-factor.md): Learn about how FusionAuth decides to trigger multi-factor authentication (MFA) in the login flow.
- [Add a SAML v2 with ADFS IdP](https://fusionauth.io/docs/lifecycle/authenticate-users/identity-providers/enterprise/adfs.md): Configure SAML v2 for Active Directory Federation Services (ADFS).
- [Add an OpenID Connect with Azure AD IdP](https://fusionauth.io/docs/lifecycle/authenticate-users/identity-providers/enterprise/azure-ad-oidc.md): Set up user login using Azure AD/Microsoft Entra ID as an OpenID Connect Identity Provider.
- [Add a SAML v2 with Azure AD IdP](https://fusionauth.io/docs/lifecycle/authenticate-users/identity-providers/enterprise/azure-ad-saml.md): Configure SAML v2 for Azure Active Directory (Azure AD)/Microsoft Entra ID.
- [Add a OpenID Connect with Cognito IdP](https://fusionauth.io/docs/lifecycle/authenticate-users/identity-providers/enterprise/cognito.md): Set up user login using Cognito as an OpenID Connect Identity Provider.
- [Add a HYPR IdP](https://fusionauth.io/docs/lifecycle/authenticate-users/identity-providers/enterprise/hypr.md): Set up user login with HYPR using the HYPR Identity Provider.
- [Add an OpenID Connect with Okta IdP](https://fusionauth.io/docs/lifecycle/authenticate-users/identity-providers/enterprise/okta-oidc.md): Learn how to set up user login using Okta as an OpenID Connect Identity Provider.
- [Add a SAML v2 IdP-Initiated with Okta IdP](https://fusionauth.io/docs/lifecycle/authenticate-users/identity-providers/enterprise/okta-samlv2-idp-initiated.md): Configure SAML v2 IdP-Initiated SSO With Okta.
- [Add a SAML v2 with Okta IdP](https://fusionauth.io/docs/lifecycle/authenticate-users/identity-providers/enterprise/okta-samlv2.md): Configure SAML v2 for Okta.
- [Add a SAML v2 IdP-Initiated IdP](https://fusionauth.io/docs/lifecycle/authenticate-users/identity-providers/enterprise/samlv2-idp-initiated.md): Set up user login using a SAML v2 IdP-Initiated Identity Provider.
- [External JWT IdP Example Usage](https://fusionauth.io/docs/lifecycle/authenticate-users/identity-providers/external-jwt/example.md): Learn how to federate identity using the External JWT Identity Provider.
- [Add an External JWT IdP](https://fusionauth.io/docs/lifecycle/authenticate-users/identity-providers/external-jwt.md): Complete a FusionAuth login with an external JWT from a third party Identity Provider.
- [Add an OpenID Connect with Discord IdP](https://fusionauth.io/docs/lifecycle/authenticate-users/identity-providers/gaming/discord.md): Learn how to set up user log in using Discord as an OpenID Connect Identity Provider.
- [Add an Epic Games IdP](https://fusionauth.io/docs/lifecycle/authenticate-users/identity-providers/gaming/epic-games.md): Learn more about user login with Epic Games using the Epic Games Identity Provider.
- [Add a Nintendo IdP](https://fusionauth.io/docs/lifecycle/authenticate-users/identity-providers/gaming/nintendo.md): Learn more about user login with Nintendo using the Nintendo Identity Provider.
- [Add a Sony PlayStation Network IdP](https://fusionauth.io/docs/lifecycle/authenticate-users/identity-providers/gaming/sony.md): Learn more about user login with Sony PlayStation using the Sony PlayStation Identity Provider.
- [Add a Steam IdP](https://fusionauth.io/docs/lifecycle/authenticate-users/identity-providers/gaming/steam.md): Learn more about user login with Steam using the Steam Identity Provider.
- [Add a Twitch IdP](https://fusionauth.io/docs/lifecycle/authenticate-users/identity-providers/gaming/twitch.md): Learn more about user login with Twitch using the Twitch Identity Provider.
- [Add an Xbox IdP](https://fusionauth.io/docs/lifecycle/authenticate-users/identity-providers/gaming/xbox.md): Learn more about user login with Xbox using the Xbox Identity Provider.
- [Add an Identity Provider (IdP)](https://fusionauth.io/docs/lifecycle/authenticate-users/identity-providers.md): An overview of all FusionAuth Identity Providers, which allow authentication delegation.
- [Add an OpenID Connect IdP](https://fusionauth.io/docs/lifecycle/authenticate-users/identity-providers/overview-oidc.md): Learn more about user login using an OpenID Connect Identity Provider.
- [Add an External SAML v2 IdP](https://fusionauth.io/docs/lifecycle/authenticate-users/identity-providers/overview-samlv2.md): Learn how to set up user log in using the SAML v2 Identity Provider.
- [Add an Apple IdP](https://fusionauth.io/docs/lifecycle/authenticate-users/identity-providers/social/apple.md): Learn how to add a login with Apple button to your application.
- [Add a Facebook IdP](https://fusionauth.io/docs/lifecycle/authenticate-users/identity-providers/social/facebook.md): Learn how to add a login with Facebook button to your application.
- [Add a Github IdP](https://fusionauth.io/docs/lifecycle/authenticate-users/identity-providers/social/github.md): Set up user login using Github as an OpenID Connect Identity Provider.
- [Add a Google IdP](https://fusionauth.io/docs/lifecycle/authenticate-users/identity-providers/social/google.md): Learn how to add a login with Google button to your application.
- [Add a LinkedIn IdP](https://fusionauth.io/docs/lifecycle/authenticate-users/identity-providers/social/linkedin.md): Learn how to add a login with LinkedIn button to your application.
- [Add a Twitter/X IdP](https://fusionauth.io/docs/lifecycle/authenticate-users/identity-providers/social/twitter.md): Learn how to add a login with Twitter/X button to your application.
- [OIDC & CockroachDB](https://fusionauth.io/docs/lifecycle/authenticate-users/integrations/oidc/cockroachdb.md): Learn how to set up CockroachDB to allow users to log in using FusionAuth via OIDC.
- [OpenID Connect Integrations](https://fusionauth.io/docs/lifecycle/authenticate-users/integrations/oidc.md): Examples of OIDC integrations.
- [OIDC & Salesforce](https://fusionauth.io/docs/lifecycle/authenticate-users/integrations/oidc/salesforce.md): Learn how to set up Salesforce to allow users to log in using FusionAuth via OIDC.
- [OIDC & Tableau Cloud](https://fusionauth.io/docs/lifecycle/authenticate-users/integrations/oidc/tableau.md): Learn how to set up Tableau Cloud to allow users to log in using FusionAuth via OIDC.
- [SAML v2 & Aiven](https://fusionauth.io/docs/lifecycle/authenticate-users/integrations/saml/aiven.md): Setting up Aiven to allow users to log in using FusionAuth via SAML v2.
- [SAML v2 & Google](https://fusionauth.io/docs/lifecycle/authenticate-users/integrations/saml/google.md): Setting up Google to allow users to log in using FusionAuth via SAML v2.
- [SAML](https://fusionauth.io/docs/lifecycle/authenticate-users/integrations/saml.md): Examples of SAMLv2 integrations.
- [SAML v2 & PagerDuty](https://fusionauth.io/docs/lifecycle/authenticate-users/integrations/saml/pagerduty.md): Setting up PagerDuty to allow users to log in using FusionAuth via SAML v2.
- [SAML v2 & SendGrid](https://fusionauth.io/docs/lifecycle/authenticate-users/integrations/saml/sendgrid.md): Setting up SendGrid to allow users to log in using FusionAuth via SAML v2.
- [SAML v2 & Tableau Cloud](https://fusionauth.io/docs/lifecycle/authenticate-users/integrations/saml/tableau-cloud.md): Setting up Tableau Cloud to allow users to log in using FusionAuth via SAML v2.
- [SAML v2 & Zendesk](https://fusionauth.io/docs/lifecycle/authenticate-users/integrations/saml/zendesk.md): Setting up Zendesk to allow users to log in using FusionAuth via SAML v2.
- [Build a Login Page with the Login API](https://fusionauth.io/docs/lifecycle/authenticate-users/login-api.md): Learn about the Login API and when you would use it.
- [JSON Web Tokens](https://fusionauth.io/docs/lifecycle/authenticate-users/login-api/json-web-tokens.md): Learn how FusionAuth provides and manages JSON Web Tokens.
- [Logout And Session Management](https://fusionauth.io/docs/lifecycle/authenticate-users/logout-session-management.md): Learn about how FusionAuth handles logout and session management.
- [Multi-Factor Authentication (MFA)](https://fusionauth.io/docs/lifecycle/authenticate-users/multi-factor-authentication.md): Learn about how to use multi-factor authentication (MFA) in FusionAuth as a developer.
- [OAuth DPoP](https://fusionauth.io/docs/lifecycle/authenticate-users/oauth/dpop.md): Learn how to enable sender-constrained OAuth tokens DPoP (Demonstration of Proof-of-Possession) with FusionAuth and validate DPoP proofs in your APIs.
- [OAuth Issuer Validation](https://fusionauth.io/docs/lifecycle/authenticate-users/oauth/issuer-validation.md): Learn how to validate the authorization response issuer parameter (RFC 9207) to prevent mix-up attacks.
- [Modes](https://fusionauth.io/docs/lifecycle/authenticate-users/oauth/modes.md): An overview of OAuth modes and how OAuth is commonly used.
- [OIDC Prompt](https://fusionauth.io/docs/lifecycle/authenticate-users/oauth/prompt.md): Learn about OpenID Connect prompt and example use cases.
- [OAuth Response Modes](https://fusionauth.io/docs/lifecycle/authenticate-users/oauth/response-modes.md): Learn about OAuth 2.0 response modes (query, fragment, form_post) and when to use each one.
- [Access Control with OAuth Scopes](https://fusionauth.io/docs/lifecycle/authenticate-users/oauth/scopes.md): Learn about OAuth scope policy configuration, managing custom scopes, and using scopes in an OAuth2 workflow.
- [Manage Software Tokens](https://fusionauth.io/docs/lifecycle/authenticate-users/oauth/tokens.md): Learn about OAuth2 and OpenID Connect Tokens and how they are used.
- [URL Validation](https://fusionauth.io/docs/lifecycle/authenticate-users/oauth/url-validation.md): Learn about OAuth URL validation policies in FusionAuth.
- [Configure One-Time Passwords](https://fusionauth.io/docs/lifecycle/authenticate-users/one-time-passwords/configure.md): Set up a passwordless experience using magic links and codes.
- [Customize One-Time Passwords](https://fusionauth.io/docs/lifecycle/authenticate-users/one-time-passwords/customize.md): Customize the one-time password experience in your application.
- [One-Time Passwords](https://fusionauth.io/docs/lifecycle/authenticate-users/one-time-passwords.md): Create a passwordless experience using magic links and one-time passwords.
- [Configure Passkeys](https://fusionauth.io/docs/lifecycle/authenticate-users/passkeys/configure.md): Set up a passwordless experience using passkeys.
- [Customize Passkeys](https://fusionauth.io/docs/lifecycle/authenticate-users/passkeys/customize.md): Customize the passkey experience in your application.
- [Passkeys](https://fusionauth.io/docs/lifecycle/authenticate-users/passkeys.md): An overview of the passwordless capabilities of FusionAuth.
- [Risk Signals](https://fusionauth.io/docs/lifecycle/authenticate-users/risk-signals.md): Learn about the risk signals that FusionAuth uses to identify suspicious activity and influence intelligent MFA decisionmaking.
- [Host a SAML v2 Identity Provider](https://fusionauth.io/docs/lifecycle/authenticate-users/saml.md): An overview of the SAML Identity Provider capabilities of FusionAuth.
- [Setting Up User Account Lockout](https://fusionauth.io/docs/lifecycle/authenticate-users/setting-up-user-account-lockout.md): Learn how to set up user account locking rules.
- [Implementing Single Sign-on](https://fusionauth.io/docs/lifecycle/authenticate-users/single-sign-on.md): Learn how to implement single sign-on between applications using FusionAuth.
