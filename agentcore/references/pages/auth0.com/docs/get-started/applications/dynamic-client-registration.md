---
title: Dynamic Client Registration
description: You can dynamically register third-party applications for your tenant. Dynamic Client Registration (DCR) is based on the OpenID Connect Dynamic Client Registration specification.
product: Amazon Bedrock AgentCore
section: References / auth0.com
source_url: https://auth0.com/docs/get-started/applications/dynamic-client-registration
fetched: '2026-09-26'
tags:
- agentcore
- auth0-com
- reference
- related
referenced_by:
- runtime-mcp.md
conversion: native-md
---

> ## Documentation Index
> Fetch the complete documentation index at: https://auth0.com/llms.txt
> Use this file to discover all available pages before exploring further.

> Learn how to dynamically register third-party applications with Auth0.

# Dynamic Client Registration

export const AuthCodeGroup = ({children, dropdown}) => {
  const [processedChildren, setProcessedChildren] = useState(children);
  useEffect(() => {
    let unsubscribe = null;
    function init() {
      unsubscribe = window.autorun(() => {
        const processChildren = node => {
          if (typeof node === "string") {
            let processedNode = node;
            for (const [key, value] of window.rootStore.variableStore.values.entries()) {
              const escapedKey = key.replaceAll(/[.*+?^${}()|[\]\\]/g, (String.raw)`\$&`);
              processedNode = processedNode.replaceAll(new RegExp(escapedKey, "g"), value);
            }
            return processedNode;
          } else if (Array.isArray(node)) {
            return node.map(processChildren);
          } else if (node && node.props && node.props.children) {
            return {
              ...node,
              props: {
                ...node.props,
                children: processChildren(node.props.children)
              }
            };
          }
          return node;
        };
        setProcessedChildren(processChildren(children));
      });
    }
    if (window.rootStore) {
      init();
    } else {
      window.addEventListener("adu:storeReady", init);
    }
    return () => {
      window.removeEventListener("adu:storeReady", init);
      unsubscribe?.();
    };
  }, [children]);
  return <CodeGroup dropdown={dropdown}>{processedChildren}</CodeGroup>;
};

export const AuthCodeBlock = ({filename, icon, language, highlight, children}) => {
  const [displayText, setDisplayText] = useState(children);
  const [copyText, setCopyText] = useState(children);
  const wrapperRef = React.useRef(null);
  useEffect(() => {
    let unsubscribe = null;
    function init() {
      if (!window.autorun || !window.rootStore) {
        return;
      }
      unsubscribe = window.autorun(() => {
        let processedChildrenForDisplay = children;
        let processedChildrenForCopy = children;
        for (const [key, value] of window.rootStore.variableStore.values.entries()) {
          const escapedKey = key.replaceAll(/[.*+?^${}()|[\]\\]/g, (String.raw)`\$&`);
          let displayValue = value;
          if (key === "{yourClientSecret}" && value !== "{yourClientSecret}") {
            displayValue = value.substring(0, 3) + "*****MASKED*****";
          }
          processedChildrenForDisplay = processedChildrenForDisplay.replaceAll(new RegExp(escapedKey, "g"), displayValue);
          processedChildrenForCopy = processedChildrenForCopy.replaceAll(new RegExp(escapedKey, "g"), value);
        }
        setDisplayText(processedChildrenForDisplay);
        setCopyText(processedChildrenForCopy);
      });
    }
    if (window.rootStore) {
      init();
    } else {
      window.addEventListener("adu:storeReady", init);
    }
    return () => {
      window.removeEventListener("adu:storeReady", init);
      unsubscribe?.();
    };
  }, [children]);
  useEffect(() => {
    if (!wrapperRef.current) return;
    const originalWriteText = navigator.clipboard.writeText.bind(navigator.clipboard);
    let isOverriding = false;
    const handleClick = e => {
      const button = e.target.closest('[data-testid="copy-code-button"]');
      if (!button || !wrapperRef.current.contains(button)) return;
      isOverriding = true;
      navigator.clipboard.writeText = text => {
        if (isOverriding) {
          isOverriding = false;
          navigator.clipboard.writeText = originalWriteText;
          return originalWriteText(copyText);
        }
        return originalWriteText(text);
      };
      setTimeout(() => {
        if (isOverriding) {
          isOverriding = false;
          navigator.clipboard.writeText = originalWriteText;
        }
      }, 100);
    };
    const wrapper = wrapperRef.current;
    wrapper.addEventListener('click', handleClick, true);
    return () => {
      wrapper.removeEventListener('click', handleClick, true);
      if (navigator.clipboard.writeText !== originalWriteText) {
        navigator.clipboard.writeText = originalWriteText;
      }
    };
  }, [copyText]);
  return <div ref={wrapperRef}>
      <CodeBlock filename={filename} icon={icon} language={language} lines highlight={highlight}>
        {displayText}
      </CodeBlock>
    </div>;
};

You can dynamically register third-party applications for your tenant. Dynamic Client Registration (DCR) is based on the [OpenID Connect Dynamic Client Registration specification](https://openid.net/specs/openid-connect-registration-1_0.html).

All applications created through Dynamic Client Registration are [third-party applications](/docs/get-started/applications/third-party-applications) with [enhanced security controls](/docs/get-started/applications/third-party-applications/security-controls). This means DCR clients:

* Receive a `tpc_` client ID prefix
* Require PKCE for authorization code flows
* Support only `authorization_code` and `refresh_token` grant types. The `client_credentials` grant type is not available via DCR.
* Can only access APIs through explicit [client grants](/docs/get-started/applications/application-access-to-apis-client-grants)
* Can only use [domain-level connections](/docs/authenticate/identity-providers/promote-connections-to-domain-level) for authentication

## Enable Dynamic Client Registration

<Warning>
  Auth0 supports Open Dynamic Registration. If enabled, anyone will be able to create applications in your tenant without a token.
</Warning>

By default, Dynamic Client Registration is disabled for all tenants. To enable Dynamic Client Registration, use the Auth0 Dashboard or Management API.

<Tabs>
  <Tab title="Auth0 Dashboard">
    1. Navigate to [Dashboard > Settings > Advanced](https://manage.auth0.com/#/tenant/advanced) and enable **Dynamic Client Registration (DCR)**.
  </Tab>

  <Tab title="Management API">
    Set the `enable_dynamic_client_registration` flag to `true` in your tenant settings using the [`/api/v2/tenants/settings`](https://auth0.com/docs/api/management/v2#!/Tenants/patch_settings) endpoint.

    <Callout icon="file-lines" color="#0EA5E9" iconType="regular">Using the Auth0 CLI? If you haven't already, [set up and authenticate your CLI session](/docs/deploy-monitor/auth0-cli) before running this command.</Callout>

    <AuthCodeGroup>
      ```bash Auth0 CLI theme={null}
      auth0 api patch "tenants/settings" \
        --data '{ "flags": { "enable_dynamic_client_registration": true } }'
      ```

      ```bash cURL theme={null}
      curl --request PATCH \
        --url 'https://{yourDomain}/api/v2/tenants/settings' \
        --header 'authorization: Bearer {YOUR_MANAGEMENT_API_TOKEN}' \
        --header 'content-type: application/json' \
        --data '{ "flags": { "enable_dynamic_client_registration": true } }'
      ```
    </AuthCodeGroup>

    You need to update the `{YOUR_MANAGEMENT_API_TOKEN}` with a valid token with the scope `update:tenant_settings`. To learn more, read [Management API Access Tokens](/docs/secure/tokens/access-tokens/management-api-access-tokens).
  </Tab>
</Tabs>

## Configure API access for DCR clients

Before enabling DCR, configure [default permissions for third-party applications](/docs/get-started/applications/application-access-to-apis-client-grants#default-permissions-for-third-party-applications) on the APIs that dynamically registered clients should access. Without default permissions, DCR clients will not be able to access any API.

Default permissions define a baseline set of APIs and scopes available to all third-party applications automatically. This is essential for DCR because you cannot configure per-application client grants during the registration flow.

To learn how to configure default permissions, read [Configure Third-Party Applications](/docs/get-started/applications/third-party-applications/configure-third-party-applications#default-permissions-for-all-third-party-applications).

## Register an application

To dynamically register an application, make a `POST` request to the `/oidc/register` endpoint. Because Auth0 supports Open Dynamic Registration, the `/oidc/register` endpoint accepts registration requests without an access token.

<AuthCodeGroup>
  ```bash cURL theme={null}
  curl --request POST \
    --url 'https://{yourDomain}/oidc/register' \
    --header 'content-type: application/json' \
    --data '{
      "client_name": "My Dynamic Application",
      "redirect_uris": ["https://application.example.com/callback"],
      "token_endpoint_auth_method": "none",
      "grant_types": ["authorization_code", "refresh_token"],
      "response_types": ["code"]
    }'
  ```
</AuthCodeGroup>

| **Parameter**                | **Description**                                                                                                                                                                                           |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `client_name`                | The name of the application to create.                                                                                                                                                                    |
| `redirect_uris` (required)   | An array of URLs that Auth0 will accept as valid callback URLs at the end of an authentication flow.                                                                                                      |
| `token_endpoint_auth_method` | The authentication method for the token endpoint. Use `none` for public clients (SPA, Native) or `client_secret_post` (default) for confidential clients.                                                 |
| `grant_types`                | The grant types the application wants to use. Filtered down in response to reflect the ones it will be allowed to use. Applications created through DCR support `authorization_code` and `refresh_token`. |
| `response_types`             | The response types the application will use. Use `code` for authorization code flow.                                                                                                                      |

If successful, Auth0 returns the application credentials:

```json theme={null}
{
  "client_name": "My Dynamic Application",
  "client_id": "tpc_8SXWY6j3afl2CP5ntwEOpMdPxxy49Gt2",
  "client_secret": "Q5O...33P",
  "redirect_uris": [
    "https://application.example.com/callback"
  ],
  "client_secret_expires_at": 0,
  "grant_types": ["authorization_code", "refresh_token"],
  "token_endpoint_auth_method": "none"
}
```

| **Field**                  | **Description**                                                                                        |
| -------------------------- | ------------------------------------------------------------------------------------------------------ |
| `client_id`                | Unique application identifier with a `tpc_` prefix. Use this when initiating authentication flows.     |
| `client_secret`            | Application secret for confidential clients. Not returned when `token_endpoint_auth_method` is `none`. |
| `client_secret_expires_at` | Expiration time for the client secret. Always `0` (never expires) for Auth0.                           |

<Callout icon="file-lines" color="#0EA5E9" iconType="regular">
  Third-party developers cannot modify application settings after registration. If changes are necessary, they must contact the tenant owner.
</Callout>

After registration, the application can initiate an [Authorization Code Flow with PKCE](/docs/get-started/authentication-and-authorization-flow/authorization-code-flow-with-pkce) using the `client_id` and configured `redirect_uris`.

## Tenant Access Control List (ACL)

Auth0 provides a [Tenant Access Control List (ACL)](/docs/secure/tenant-access-control-list) to manage traffic to the `/oidc/register` endpoint. You can restrict who can send DCR requests by configuring ACL rules based on:

* Source IP addresses and CIDR ranges
* Geolocation
* Other request signals

To configure ACL rules for DCR, add the `dynamic_client_registration` scope to an ACL rule. To learn more, read [Tenant ACL Reference](/docs/secure/tenant-access-control-list/reference).

## Rate limits

The `/oidc/register` endpoint is rate-limited to 5 requests per second per tenant. To learn more about rate limits, read [Rate Limit Configuration](/docs/troubleshoot/customer-support/operational-policies/rate-limit-policy/rate-limit-configurations).

## Permissive mode for DCR

Some customers who were using third-party applications before April 2026 can configure DCR to create applications with pre-existing behavior instead of enhanced security controls. To learn more, read [Dynamic Client Registration in Permissive Mode](/docs/get-started/applications/third-party-applications/permissive-mode#dynamic-client-registration-in-permissive-mode).

## Learn more

* [Third-Party Applications](/docs/get-started/applications/third-party-applications)
* [Security Controls for Third-Party Applications](/docs/get-started/applications/third-party-applications/security-controls)
* [Application Access to APIs: Client Grants](/docs/get-started/applications/application-access-to-apis-client-grants)
* [First-Party and Third-Party Applications](/docs/get-started/applications/first-party-and-third-party-applications)
* [User Consent and Third-Party Applications](/docs/get-started/applications/third-party-applications/user-consent-and-third-party-applications)
