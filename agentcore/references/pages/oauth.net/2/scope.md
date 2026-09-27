---
title: scope
description: tools.ietf.org/html/rfc6749#section-3.3
product: Amazon Bedrock AgentCore
section: References / oauth.net
source_url: https://oauth.net/2/scope
fetched: '2026-09-26'
tags:
- agentcore
- oauth-net
- reference
- related
referenced_by:
- gateway-inbound-auth.md
conversion: pandoc
---

## OAuth Scopes

[tools.ietf.org/html/rfc6749#section-3.3](https://tools.ietf.org/html/rfc6749#section-3.3)

Scope is a mechanism in OAuth 2.0 to limit an application's access to a user's account. An application can request one or more scopes, this information is then presented to the user in the consent screen, and the access token issued to the application will be limited to the scopes granted.

The OAuth spec allows the authorization server or user to modify the scopes granted to the application compared to what is requested, although there are not many examples of services doing this in practice.

OAuth does not define any particular values for scopes, since it is highly dependent on the service's internal architecture and needs.

**Examples of Scopes in Popular Services**

- [Slack](https://api.slack.com/docs/oauth-scopes)
- [GitHub](https://developer.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/)
- [Google](https://developers.google.com/identity/protocols/googlescopes)
- [FitBit](https://dev.fitbit.com/build/reference/web-api/developer-guide/application-design/#Scopes)

**More resources**

- [Defining Scopes](https://www.oauth.com/oauth2-servers/scope/defining-scopes/) (oauth.com)
- [OpenID Connect Scopes](https://openid.net/specs/openid-connect-core-1_0.html#ScopeClaims) (openid.net)
