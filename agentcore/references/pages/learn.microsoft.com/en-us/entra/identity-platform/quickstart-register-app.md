---
title: Register an application in Microsoft Entra ID
description: Table of contents
product: Amazon Bedrock AgentCore
section: References / learn.microsoft.com
source_url: https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app
fetched: '2026-09-26'
tags:
- agentcore
- learn-microsoft-com
- reference
- related
referenced_by:
- identity-idp-microsoft.md
conversion: pandoc
---

Table of contents

Exit editor mode

Ask Learn

Ask Learn

Reading mode

Table of contents

[ Read in English](#)

Add

Add to Plans

[ Edit](https://github.com/MicrosoftDocs/entra-docs/blob/main/docs/identity-platform/quickstart-register-app.md)

------------------------------------------------------------------------

Copy Markdown

Print

------------------------------------------------------------------------

Note

Access to this page requires authorization. You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Register an application in Microsoft Entra ID

Feedback

Summarize this article for me

In this how-to guide, you learn how to register an application in Microsoft Entra ID. This process is essential for establishing a trust relationship between your application and the Microsoft identity platform. By completing this quickstart, you enable identity and access management (IAM) for your app, allowing it to securely interact with Microsoft services and APIs.

## Prerequisites

- An Azure account that has an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
- The Azure account must be at least an [Application Developer](../identity/role-based-access-control/permissions-reference#application-developer).
- A workforce or external tenant. You can use your **Default Directory** for this quickstart. If you need an external tenant, complete [set up an external tenant](/en-us/entra/external-id/customers/quickstart-tenant-setup).

## Register an application

Registering your application in Microsoft Entra establishes a trust relationship between your app and the Microsoft identity platform. The trust is unidirectional. Your app trusts the Microsoft identity platform, and not the other way around. Once created, you can't move the application object between different tenants.

Follow these steps to create the app registration:

1.  Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least an [Application Developer](../identity/role-based-access-control/permissions-reference#application-developer).

2.  If you have access to multiple tenants, use the **Settings** icon ![](media/common/admin-center-settings-icon.png) in the top menu to switch to the tenant in which you want to register the application.

3.  Browse to **Entra ID** \> **App registrations** and select **New registration**.

4.  Enter a meaningful **Name** for your app; for example, *identity-client-app*. App users can see this name, and you can change it at any time. You can have multiple app registrations with the same name.

5.  Under **Supported account types**, open the drop-down and select who can use the application. We recommend **Single tenant only - \<your tenant\>** for most applications. Refer to the table for more information on each option.

    | Supported account types | Description |
    |----|----|
    | **Single tenant only - \<your tenant\>** | For *single-tenant* apps for use only by users (or guests) in *your* tenant. |
    | **Multiple Entra ID tenants** | For *multitenant* apps when you want users in *any* Microsoft Entra tenant to be able to use your application. Ideal for software-as-a-service (SaaS) applications that you intend to provide to multiple organizations. |
    | **Any Entra ID Tenant + Personal Microsoft accounts** | For *multitenant* apps that support both organizational and personal Microsoft accounts (for example, Skype, Xbox, Live, Hotmail). |
    | **Personal accounts only** | For apps used only by personal Microsoft accounts (for example: Xbox, Live, Hotmail). |

6.  Select **Register** to complete the app registration.

7.  The application's **Overview** page is displayed. Record the **Application (client) ID**, which uniquely identifies your application and is used in your application's code as part of validating the security tokens it receives from the Microsoft identity platform.

Important

New app registrations are hidden to users by default. When you're ready for users to see the app on their [My Apps page](https://support.microsoft.com/account-billing/sign-in-and-start-apps-from-the-my-apps-portal-2f3b1bae-0e5a-4a86-a33e-876fbd2a4510) you can enable it. To enable the app, navigate to **Entra ID** \> **Enterprise apps** in the Microsoft Entra admin center and select the app. Then set **Visible to users?** to **Yes** on the **Properties** page.

## Grant admin consent (external tenants only)

Once you register your application, it gets assigned the **User.Read** permission. However, for external tenants, the customer users can't consent to permissions themselves. You as the admin must consent to this permission on behalf of all the users in the tenant:

1.  Select **API permissions** under **Manage** on your app registration's **Overview** page.
2.  Select **Grant admin consent for \< tenant name \>**, then select **Yes**.
3.  Select **Refresh**, then verify that **Granted for \< tenant name \>** appears under **Status** for the permission.

## Related content

- [Add a redirect URI to your application](how-to-add-redirect-uri)
- [Add credentials to your application](how-to-add-credentials)
- [Configure an application to expose a web API](quickstart-configure-app-expose-web-apis)
- [Microsoft identity platform code samples](sample-v2-code)
- [Add your application to a user flow](/en-us/entra/external-id/customers/how-to-user-flow-add-application)

------------------------------------------------------------------------

## Feedback

Was this page helpful?

Yes

No

No

Need help with this topic?

Want to try using Ask Learn to clarify or guide you through this topic?

Ask Learn

Ask Learn

Suggest a fix?

------------------------------------------------------------------------

## Additional resources

------------------------------------------------------------------------

-  Last updated on 2026-06-05
