---
title: Using IAM Identity Center to authenticate AWS SDK and tools
description: AWS IAM Identity Center can be used to provide AWS credentials when developing an AWS application on a non-AWS compute service environments. If you are developing on an AWS resource, such as Amazon Elastic Compute Cloud (Amazon EC2) or AWS Cloud9, we recommend getting credentials
product: Amazon Bedrock AgentCore
section: References / docs.aws.amazon.com
source_url: https://docs.aws.amazon.com/sdkref/latest/guide/access-sso.html
fetched: '2026-09-26'
tags:
- agent-registry
- agentcore
- docs-aws-amazon-com
- reference
- related
referenced_by:
- gateway-prerequisites.md
- gateway-setup-tools-credentials.md
- registry-prerequisites.md
conversion: native-md
---

# Using IAM Identity Center to authenticate AWS SDK and tools
<a name="access-sso"></a>

 AWS IAM Identity Center can be used to provide AWS credentials when developing an AWS application on a non-AWS compute service environments. If you are developing on an AWS resource, such as Amazon Elastic Compute Cloud (Amazon EC2) or AWS Cloud9, we recommend getting credentials from that service instead.

Use IAM Identity Center authentication if you already use Identity Center for AWS account access or need to manage access for an organization. 

In this tutorial, you establish IAM Identity Center access and will configure it for your SDK or tool by using the AWS access portal and the AWS CLI.
+ The AWS access portal is the web location where you manually sign in to the IAM Identity Center. The format of the URL is `d-xxxxxxxxxx.awsapps.com/start`or `{{your_subdomain}}.awsapps.com/start`. When signed in to the AWS access portal, you can view AWS accounts and roles that have been configured for that user. This procedure uses the AWS access portal to get configuration values you need for the SDK/tool authentication process. 
+ The AWS CLI is used to configure your SDK or tool to use IAM Identity Center authentication for API calls made by your code. This one-time process updates your shared AWS `config` file, that is then used by your SDK or tool when you run your code. 

## Prerequisites
<a name="prereq-auth"></a>

Before starting this procedure, you should have completed the following:
+ If you do not have an AWS account, [sign up for an AWS account](https://portal.aws.amazon.com/billing/signup).
+ If you haven't enabled IAM Identity Center yet, [enable IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/get-set-up-for-idc.html) by following the instructions in the *AWS IAM Identity Center User Guide*.

## Configure programmatic access using IAM Identity Center
<a name="idcGettingStarted"></a>

### Step 1: Establish access and select appropriate permission set
<a name="establishAccess"></a>

Choose one of the following methods to access your AWS credentials.

#### I do not have established access through IAM Identity Center
<a name="idc-access"></a>

1. Add a user and add administrative permissions by following the [Configure user access with the default IAM Identity Center directory](https://docs.aws.amazon.com/singlesignon/latest/userguide/quick-start-default-idc.html) procedure in the *AWS IAM Identity Center User Guide*. 

1. The `AdministratorAccess` permission set should not be used for regular development. Instead, we recommend using the predefined `PowerUserAccess` permission set, unless your employer has created a custom permission set for this purpose.

   Follow the same [Configure user access with the default IAM Identity Center directory](https://docs.aws.amazon.com/singlesignon/latest/userguide/quick-start-default-idc.html) procedure again, but this time:
   + Instead of creating the `{{Admin team}}` group, create a `{{Dev team}}` group, and substitute this thereafter in the instructions.
   + You can use the existing user, but the user must be added to the new `{{Dev team}}` group.
   + Instead of creating the `{{AdministratorAccess}}` permission set, create a `{{PowerUserAccess}}` permission set, and substitute this thereafter in the instructions.

   When you are done, you should have the following:
   + A `Dev team` group.
   + An attached `PowerUserAccess` permission set to the `Dev team` group.
   + Your user added to the `Dev team` group.

1. Exit the portal and sign in again to see your AWS accounts and options for `Administrator` or `PowerUserAccess`. Select `PowerUserAccess` when working with your tool/SDK. 

#### I already have access to AWS through a federated identity provider managed by my employer (such as Microsoft Entra or Okta)
<a name="federated-access"></a>

Sign in to AWS through your identity provider's portal. If your Cloud Administrator has granted you `PowerUserAccess` (developer) permissions, you see the AWS accounts that you have access to and your permission set. Next to the name of your permission set, you see options to access the accounts manually or programmatically using that permission set. 

Custom implementations might result in different experiences, such as different permission set names. If you're not sure which permission set to use, contact your IT team for help. 

#### I already have access to AWS through the AWS access portal managed by my employer
<a name="accessportal-access"></a>

Sign in to AWS through the AWS access portal. If your Cloud Administrator has granted you `PowerUserAccess` (developer) permissions, you see the AWS accounts that you have access to and your permission set. Next to the name of your permission set, you see options to access the accounts manually or programmatically using that permission set. 

#### I already have access to AWS through a federated custom identity provider managed by my employer
<a name="customfederated-access"></a>

Contact your IT team for help.

### Step 2: Configure SDKs and tools to use IAM Identity Center
<a name="configureAccess"></a>

1.  On your development machine, install the latest AWS CLI. 

   1. See [Installing or updating the latest version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) in the *AWS Command Line Interface User Guide*. 

   1.  (Optional) To verify that the AWS CLI is working, open a command prompt and run the `aws --version` command. 

1. Sign in to the AWS access portal. Your employer may provide this URL or you may get it in an email following **Step 1: Establish access**. If not, find your **AWS access portal URL** on the **Dashboard** of [https://console.aws.amazon.com/singlesignon/](https://console.aws.amazon.com/singlesignon/). 

   1. In the AWS access portal, in the **Accounts** tab, select the individual account to manage. The roles for your user are displayed. Choose **Access keys** to get credentials for command line or programmatic access for the appropriate permission set. Use the predefined `PowerUserAccess` permission set, or whichever permission set you or your employer has created to apply least-privilege permissions for development. 

   1. In the **Get credentials** dialog box, choose either **MacOS and Linux** or **Windows**, depending on your operating system.

   1. Choose the **IAM Identity Center credentials** method to get the `Issuer URL` and `SSO Region` values that you need for the next step. Note: `SSO Start URL` can be used interchangeably with `Issuer URL`.

1. In the AWS CLI command prompt, run the `aws configure sso` command. When prompted, enter the configuration values that you collected in the previous step. For details on this AWS CLI command, see [Configure your profile with the `aws configure sso` wizard](https://docs.aws.amazon.com/cli/latest/userguide/sso-configure-profile-token.html#sso-configure-profile-token-auto-sso). 

   1. For the prompt `SSO Start URL`, enter the value you obtained for `Issuer URL`. 

   1.  For **CLI profile name**, we recommend entering {{default}} when you are getting started. For information about how to set non-default (named) profiles and their associated environment variable, see [Profiles](file-format.md#file-format-profile). 

1. (Optional) In the AWS CLI command prompt, confirm the active session identity by running the `aws sts get-caller-identity` command. The response should show the IAM Identity Center permission set that you configured. 

1. If you are using an AWS SDK, create an application for your SDK in your development environment.

   1. For some SDKs, additional packages such as `SSO` and `SSOOIDC` must be added to your application before you can use IAM Identity Center authentication. For details, see your specific SDK.

   1.  If you previously configured access to AWS, review your shared AWS `credentials` file for any [AWS access keys](feature-static-credentials.md). You must remove any static credentials before the SDK or tool will use the IAM Identity Center credentials because of the [Understand the credential provider chain](standardized-credentials.md#credentialProviderChain) precedence. 

 For a deep dive into how the SDKs and tools use and refresh credentials using this configuration, see [How IAM Identity Center authentication is resolved for AWS SDKs and tools](understanding-sso.md). 

To configure IAM Identity Center provider settings directly in the shared `config` file, see [IAM Identity Center credential provider](feature-sso-credentials.md) in this guide.

## Refreshing portal access sessions
<a name="refreshSession"></a>

Your access will eventually expire and the SDK or tool will encounter an authentication error. When this expiration occurs depends on your configured session lengths. To refresh the access portal session again when needed, use the AWS CLI to run the `aws sso login` command. 

You can extend both the IAM Identity Center access portal session duration and the permission set session duration. This lengthens the amount of time that you can run code before you need to manually sign in again with the AWS CLI. For more information, see the following topics in the *AWS IAM Identity Center User Guide*:
+ **IAM Identity Center session duration** – [Configure the duration of your users' AWS access portal sessions](https://docs.aws.amazon.com/singlesignon/latest/userguide/configure-user-session.html) 
+ **Permission set session duration** – [Set session duration ](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtosessionduration.html)
