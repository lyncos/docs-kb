---
title: Add and configure the custom OpenID Connect application
description: This topic covers how to add the custom OpenID Connect application to the Identity Administration portal and configure trust. For information on OpenID connect, see About OpenID Connect.
product: Amazon Bedrock AgentCore
section: References / docs.cyberark.com
source_url: https://docs.cyberark.com/identity/latest/en/content/applications/appscustom/openidaddconfigapp.htm
fetched: '2026-09-26'
tags:
- agentcore
- docs-cyberark-com
- reference
- related
referenced_by:
- identity-idp-cyberark.md
conversion: pandoc
---

# Add and configure the custom OpenID Connect application

This topic covers how to add the custom OpenID Connect application to the Identity Administration portal and configure trust. For information on OpenID connect, see [About OpenID Connect](https://docs.cyberark.com/snapshot/identity/en/content/developer/oidc/about-openidconnect.htm).

## Step 1: Add the OpenID Connect application

To add and configure a generic OpenID Connect application:

1.  Go to Manage \> Identities \> Web apps, then click Add Web Apps.

    The Add Web Apps screen displays.

2.  Select the Custom tab.

    ![](appscustomimg/addwebapps_clickcustom.png)

3.  On the Custom tab, next to the OpenID Connect application, click Add.

4.  In the Add Web Apps screen, click Yes to add the application.

5.  Click Close to exit the Application Catalog.

    The application that you just added opens to the Settings page.

6.  Enter the application ID.

    The application ID is used by the client application to send authorization and token requests to the custom application. The application ID identifies the custom application uniquely to make the API requests.

    The app key is used to integrate the custom application with widgets and client applications.

7.  Update the name, description, category, and logo fields as needed.

    We recommend giving this application a unique name because this is a custom application. You can also provide a custom application logo.

    The Category field specifies the default grouping for the application in the user portal. Users have the option to create a tag that overrides the default grouping in the user portal.

    You can customize the name and description for each supported language.

    ![](appscustomimg/oidc_settingsdescription.png "OIDC Description settings")

8.  (Optional) Click On enrolled mobile devices, open this application in the built-in browser (required for Derived Credential login) to authenticate with this application.

    See [Idira-issued derived credentials](/setup/latest/en/content/identity/coreservices/authenticate/derived-credentials-company-issued.htm "Derived Credentials") for more information.

## Step 2: Configure Trust settings

1.  Go to the Trust page.

2.  For the following options, copy the content from the application website to the Trust page.

    [TABLE]

    Copy from application to Trust page

3.  For the following options, copy the content from the Trust page to the application website.

    | Option | Description |
    |----|----|
    | OpenID Connect Client ID | Copy the Client ID and paste it into the appropriate field on the application website. |
    | OpenID Connect Metadata URL | Copy the metadata URL and paste it into the appropriate field on the application website. |
    | OpenID Connect Issuer URL | A URL unique to this application profile. This value is the entity ID used in the assertion to identify the identity provider attempting to authenticate. The web application doesn’t contact this URL so it doesn’t need to be functional. |

    Copy from Trust page to application

## Step 3: Configure Tokens settings

1.  On the Tokens page, set the token lifetime for ID tokens, access tokens and refresh if you choose to issue refresh tokens.

    The default ID and access token lifetime is five hours.

    If you issue refresh tokens, the default lifetime for a refresh token is 365 days. Refresh tokens are exchanged for new access tokens, allowing your application to have a valid access token without additional user interaction.

    ![](appscustomimg/oidc_tokens.png)

    For existing custom OpenID Connect applications, select the Generate access and ID tokens with new structure (recommended) checkbox to exclude claim information from the access token, and scope information from the ID token. The new access and ID token structure is based on the OIDC standards. For more information, see [OpenID specifications](https://openid.net/specs/openid-connect-core-1_0.html). For a detailed description of the old and new structure for the access and ID tokens, see [OpenID Connect tokens](https://docs.cyberark.com/snapshot/identity/en/content/developer/oidc/tokens/tokens-intro.htm).

2.  You can add parameters for the client application to send in OIDC authorization requests. The parameters are used to execute further actions after the user logs in. You can access these parameters in the script and set the custom claims or call inline hooks for processing.

    For example, you can send a user's Universally Unique Identifier (UUID) in the authorization request to validate whether the user is being impersonated during sign-in. The token is generated based on this information.

    Other examples of possible actions include:

    - Modify access and ID tokens.

    - Call APIs to enrich user profiles or send notifications.

    - Create authorization rules and make access decisions based on custom logic.

    - Conditionally enable MFA.

    - Redirect users to an external site.

    The parameters must be pre-registered with the authorization server.

    Parameters are sent in the request as `additional_params` in the following format:

    `{<parameter-name>":"value1", "parameter-name":"value2"}`

    For example: `{"param1" : "devadmin@identity-poc", "param2" : "abc123"}`

    1.  Under Authorized Parameters, click Add. Enter the name of the parameter and an optional description, then click Save. Add as many parameters as you need.

    2.  Scroll down to Script to set custom claims. Enter the parameter name as shown in the following example, where `param1` is the example parameter name. (To learn more about custom claims, see [Customize the OpenID Connect Custom Logic script](openidscriptcust.htm) and [Claims and headers](https://docs.cyberark.com/snapshot/identity/en/content/developer/oidc/claims.htm).)

        ![](appscustomimg/oidc-set-custom-claim.png)

    3.  Click Save.

## Step 4: Configure Scope settings

1.  On the Scope page, add any desired scopes and select from the following options:

    [TABLE]

    Scope settings

2.  The OpenID Connect scopes are categorized into the following two types:

    | Scope | Description |
    |----|----|
    | [API scope](https://docs.cyberark.com/snapshot/identity/en/content/developer/oidc/api-scopes.htm) | Used to define the scopes to access APIs. |
    | [Custom claims scope](https://docs.cyberark.com/snapshot/identity/en/content/developer/oidc/claims.htm#Custom) | Used to define the scopes to retrieve custom claims that are part of the ID token. |

    Scope types

    Click Add under Scope Definitions to add an API scope or a custom claims scope. You can use a regular expression (regex) to define scopes. To add a scope for all APIs, enter .\* as the REST Regex value. For example, use `/UserMgmt/.*` to match the User Management APIs only.

    ![](appscustomimg/oidc_scopes.png)

## Step 5: Configure permission settings

1.  [Deploy the application by setting permissions on the application.](#)
    1.  On the Permissions page, click Add.

    2.  Select the user(s), group(s), or role(s) that you want to grant permissions to, then click Add.

        The added object displays on the Permissions page with View, Run, and Automatically Deploy permissions selected by default.

    3.  Select the permissions you want and click Save.

        Default permissions automatically deploy the application to the User Portal if the Show in user app list option is selected on the Settings page. Do not select this option if you intend to use only SP-initiated SSO.

        Change the permissions if you want to add additional control or if you prefer not to automatically deploy the application.

2.  [(Optional) On the Policy page, specify additional authentication controls for this application.](#)
    ![](appscustomimg/policy_app.png)

    1.  Click Add Rule.  

        The Authentication Rule window displays.

        ![](appscustomimg/addrulefilterwindow.png)

    2.  Click Add Filter on the Authentication Rule window.

    3.  Define the filter and condition using the drop-down boxes.  

        For example, you can create a rule that requires a specific authentication method when users access Idira Identity from an IP address that is outside of your corporate IP range.

        For more information on defining the filters and conditions, see [Create authentication rules](/identity-administration/latest/en/content/coreservices/authenticate/authrulescreate.htm).

    4.  Click the Add button associated with the filter and condition.

    5.  Select the profile you want applied if all filters/conditions are met in the Authentication Profile drop-down.  

        The authentication profile is where you define the authentication methods. If you have not created the necessary authentication profile, select the Add New Profile option. See [Creating authentication profiles](/setup/latest/en/content/identity/coreservices/authenticate/authprofilescreate.htm).

    6.  Click OK.

    7.  (Optional) In the Default Profile (used if no conditions matched) drop-down, you can select a default profile to be applied if a user does not match any of the configured conditions.  

        If you have no authentication rules configured and you select Not Allowed in the Default Profile dropdown, users will not be able to log in to the service.

    8.  Click Save.  

        If you have more than one authentication rule, you can prioritize them on the Policy page. You can also include JavaScript code to identify specific circumstances when you want to block an application or you want to require additional authentication methods. For details, see [Application access policies with JavaScript](../appsscriptref/appaccesspol_js.htm).

        If you left the Apps section of the Identity Administration portal to specify additional authentication control, you will need to return to the Apps section before continuing by clicking Apps at the top of the page in the Identity Administration portal.

## Step 6: Configure account mapping

1.  On the Account Mapping page, configure how the login information is mapped to the application’s user accounts.

    ![](appscustomimg/accountmapping.png)

    The options are as follows:

    [TABLE]

    Account mapping options

2.  (Optional) Click App Gateway to allow users to securely access this application outside of your corporate network.

    For detailed configuration instructions, see [Configure an application to use App Gateway](../appgateway-configure-app.htm).

3.  (Optional) Click Workflow to set up a request and approval work flow for this application.

    See [Manage application access requests](../appsadminportal/manage-workflow-requests.htm "Managing application access requests") for more information.

4.  (Optional) On the Changelog page, you can see recent changes that have been made to the application settings, by date, user, and the type of change that was made.

5.  Click Save.

Next, you’re ready to edit the Advanced Script (see [Customize the OpenID Connect Custom Logic script](openidscriptcust.htm) ).
