---
title: Setting up the AWS CLI
description: This topic explains how to quickly configure basic settings that the AWS Command Line Interface (AWS CLI) uses to interact with AWS. These include your security credentials, the default output format, and the default AWS Region.
product: Amazon Bedrock AgentCore
section: References / docs.aws.amazon.com
source_url: https://docs.aws.amazon.com/cli/latest/userguide/getting-started-quickstart.html
fetched: '2026-09-26'
tags:
- agentcore
- docs-aws-amazon-com
- reference
- related
referenced_by:
- gateway-setup-tools-credentials.md
conversion: native-md
---

# Setting up the AWS CLI
<a name="getting-started-quickstart"></a>

This topic explains how to quickly configure basic settings that the AWS Command Line Interface (AWS CLI) uses to interact with AWS. These include your security credentials, the default output format, and the default AWS Region.

**Topics**
+ [Gather your credential information for programmatic access](#getting-started-prereqs-keys)
+ [Setting up new configuration and credentials](#getting-started-quickstart-new)
+ [Using existing configuration and credentials files](#getting-started-quickstart-existing)

## Gather your credential information for programmatic access
<a name="getting-started-prereqs-keys"></a>

You'll need programmatic access if you want to interact with AWS outside of the AWS Management Console. For authentication and credential instructions, choose one of the following options:



| Authentication type | Purpose | Instructions | 
| --- | --- | --- | 
| AWS Management Console credentials | **(Recommended)**Use short-term credentials by logging into the AWS CLI with your console credentials. Recommended if you use root, IAM users, or federation with IAM for AWS account access | [Login for AWS local development using console credentials](cli-configure-sign-in.md) | 
| IAM Identity Center workforce users short-term credentials | Use short-term credentials for an IAM Identity Center workforce user.Security best practice is to use AWS Organizations with IAM Identity Center. It combines short-term credentials with a user directory, such as the built-in IAM Identity Center directory or Active Directory. | [Configuring IAM Identity Center authentication with the AWS CLI](cli-configure-sso.md) | 
| IAM user short-term credentials | Use IAM user short-term credentials, which are more secure than long-term credentials. If your credentials are compromised, there is a limited time they can be used before they expire. | [Authenticating with short-term credentials for the AWS CLI](cli-authentication-short-term.md) | 
| IAM or IAM Identity Center users on an Amazon EC2 instance.  | Use Amazon EC2 instance metadata to query for temporary credentials using the role assigned to the Amazon EC2 instance. | [Using Amazon EC2 instance metadata as credentials in the AWS CLI](cli-configure-metadata.md) | 
| Assume roles for permissions | Pair another credential method and assume a role for temporary access to AWS services your user might not have access to. | [Using an IAM role in the AWS CLI](cli-configure-role.md) | 
| IAM user long-term credentials | (Not recommended) Use long-term credentials, which have no expiration. | [Authenticating using IAM user credentials for the AWS CLI](cli-authentication-user.md) | 
| External storage of IAM or IAM Identity Center workforce users   | (Not recommended) Pair another credential method but store credential values in a location outside of the AWS CLI. This method is only as secure as the external location the credentials are stored. | [Sourcing credentials with an external process in the AWS CLI](cli-configure-sourcing-external.md) | 

## Setting up new configuration and credentials
<a name="getting-started-quickstart-new"></a>

The AWS CLI stores your configuration and credential information in a *profile* (a collection of settings) in the `credentials` and `config` files. 

**Topics**
+ [Configuring using AWS CLI commands](#getting-started-quickstart-new-command)
+ [Manually editing the credentials and config files](#getting-started-quickstart-new-file)

The following examples use sample values for each of the authentication methods. Replace sample values with your own.

### Configuring using AWS CLI commands
<a name="getting-started-quickstart-new-command"></a>

For general use, the `aws configure` or `aws configure sso` commands in your preferred terminal are the fastest way to set up your AWS CLI installation. Based on the credential method you prefer, the AWS CLI prompts you for the relevant information. By default, the information in this profile is used when you run an AWS CLI command that doesn't explicitly specify a profile to use.

For more information on the `credentials` and `config` files, see [Configuration and credential file settings in the AWS CLI](cli-configure-files.md).

------
#### [ Console sessions as short-term credentials ]

This example lets you use your existing console credentials with the `aws login` command. This sign in method can be used with root credentials created during initial account set up, an IAM user, or a federated identity from your identity provider. For more information, see [Login for AWS local development using console credentials](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sign-in.html).

```
$ aws login
No AWS region has been configured. The AWS region is the geographic location of your AWS resources. 

If you've used AWS before and already have resources in your account, tell us which region they were 
created in. If you haven't created resources in your account before, you can pick the region closest to you: 
https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html. You are able to change 
the region in the CLI at any time with the command `aws configure set region NEW_REGION`.

AWS Region [us-east-1]: us-east-1
Attempting to open the login page for `us-east-1` in your default browser. If the browser does not open, 
use the following URL to complete your login:

https://us-east-1.signin.aws.amazon.com/v1/authorize<abbreviated>

If you cannot connect to this URL, make sure that you have specified a valid region.

Waiting for login...

Logged in with role `arn:aws:sts::012345678910:user/iam-user`, and configured profile 
`default` to use `us-east-1`. This session will expire on October 14, 2025 at 2:04 PST. After this time, you 
can renew your session with `aws login`.
```

------
#### [ IAM Identity Center (SSO) ]

This example is for AWS IAM Identity Center using the `aws configure sso` wizard. For more information, see [Configuring IAM Identity Center authentication with the AWS CLI](cli-configure-sso.md).

```
$ aws configure sso
SSO session name (Recommended): {{my-sso}}
SSO start URL [None]: {{https://my-sso-portal.awsapps.com/start}}
SSO region [None]:{{us-east-1}}

Attempting to automatically open the SSO authorization page in your default browser.

There are 2 AWS accounts available to you.
> DeveloperAccount, developer-account-admin@example.com ({{111122223333}}) 
  ProductionAccount, production-account-admin@example.com ({{444455556666}})

Using the account ID {{111122223333}}

There are 2 roles available to you.
> ReadOnly
  FullAccess

Using the role name "ReadOnly"

CLI default client Region [None]: {{us-west-2}}
CLI default output format [None]: {{json}}
CLI profile name [123456789011_ReadOnly]: {{user1}}
```

------
#### [ IAM Identity Center (Legacy SSO) ]

This example is for the legacy method of AWS IAM Identity Center using the `aws configure sso` wizard. To use the legacy SSO, leave the session name blank. For more information, see [Configuring IAM Identity Center authentication with the AWS CLI](cli-configure-sso.md).

```
$ aws configure sso
SSO session name (Recommended):
SSO start URL [None]: {{https://my-sso-portal.awsapps.com/start}}
SSO region [None]:{{us-east-1}}

SSO authorization page has automatically been opened in your default browser.
Follow the instructions in the browser to complete this authorization request.

There are 2 AWS accounts available to you.
> DeveloperAccount, developer-account-admin@example.com ({{111122223333}}) 
  ProductionAccount, production-account-admin@example.com ({{444455556666}})

Using the account ID {{111122223333}}

There are 2 roles available to you.
> ReadOnly
  FullAccess

Using the role name "ReadOnly"

CLI default client Region [None]: {{us-west-2}}
CLI default output format [None]: {{json}}
CLI profile name [123456789011_ReadOnly]: {{user1}}
```

------
#### [ Short-term credentials ]

This example is for the short-term credentials from AWS Identity and Access Management. The aws configure wizard is used to set initial values and then the `aws configure set` command assigns the last value needed. For more information, see [Authenticating with short-term credentials for the AWS CLI](cli-authentication-short-term.md).

```
$ aws configure
AWS Access Key ID [None]: {{AKIAIOSFODNN7EXAMPLE}}
AWS Secret Access Key [None]: {{wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY}}
Default region name [None]: {{us-west-2}}
Default output format [None]: {{json}}
$ aws configure set aws_session_token {{fcZib3JpZ2luX2IQoJb3JpZ2luX2IQoJb3JpZ2luX2IQoJb3JpZ2luX2IQoJb3JpZVERYLONGSTRINGEXAMPLE}}
```

------
#### [ IAM role ]

This example is for assuming an IAM role. Profiles that use IAM roles pull credentials from another profile, and then apply IAM role permissions. In the following examples, `default` is the source profile for credentials and `user1` borrows the same credentials then assumes a new role. There is no wizard for this process, therefore each value is set using the `aws configure set` command. For more information, see [Using an IAM role in the AWS CLI](cli-configure-role.md).

```
$ aws configure set role_arn {{arn:aws:iam::123456789012:role/defaultrole}}
$ aws configure set source_profile {{default}}
$ aws configure set role_session_name {{session_user1}}
$ aws configure set region {{us-west-2}}
$ aws configure set output {{json}}
```

------
#### [ Amazon EC2 instance metadata credentials ]

This example is for the credentials obtained from the hosting Amazon EC2 instance metadata. There is no wizard for this process, therefore each value is set using the `aws configure set` command. For more information, see [Using Amazon EC2 instance metadata as credentials in the AWS CLI](cli-configure-metadata.md).

```
$ aws configure set role_arn {{arn:aws:iam::123456789012:role/defaultrole}}
$ aws configure set credential_source {{Ec2InstanceMetadata}}
$ aws configure set region {{us-west-2}}
$ aws configure set output {{json}}
```

------
#### [ Long-term credentials ]

**Warning**  
To avoid security risks, don't use IAM users for authentication when developing purpose-built software or working with real data. Instead, use federation with an identity provider such as [AWS IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html).

This example is for the long-term credentials from AWS Identity and Access Management. For more information, see [Authenticating using IAM user credentials for the AWS CLI](cli-authentication-user.md).

```
$ aws configure
AWS Access Key ID [None]: {{AKIAIOSFODNN7EXAMPLE}}
AWS Secret Access Key [None]: {{wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY}}
Default region name [None]: {{us-west-2}}
Default output format [None]: {{json}}
```

------

For more detailed information on authentication and credential methods see [Authentication and access credentials for the AWS CLI](cli-chap-authentication.md).

### Manually editing the credentials and config files
<a name="getting-started-quickstart-new-file"></a>

When copy and pasting information, we suggest manually editing the `config` and `credentials` file. Based on the credential method you prefer, the files are setup in a different way. 

The files are stored in your home directory under the `.aws` folder. Where you find your home directory location varies based on the operating system, but is referred to using the environment variables `%UserProfile%` in Windows and `$HOME` or `~` (tilde) in Unix-based systems. For more information on where these settings are stored, see [Where are configuration settings stored?](cli-configure-files.md#cli-configure-files-where).

The following examples show a `default` profile and a profile named `user1` and use sample values. Replace sample values with your own. For more information on the `credentials` and `config` files, see [Configuration and credential file settings in the AWS CLI](cli-configure-files.md).

------
#### [ IAM Identity Center (SSO) ]

This example is for AWS IAM Identity Center. For more information, see [Configuring IAM Identity Center authentication with the AWS CLI](cli-configure-sso.md).

**Credentials file**

The `credentials` file is not used for this authentication method.

**Config file**

```
[default]
sso_session = {{my-sso}}
sso_account_id = {{111122223333}}
sso_role_name = {{readOnly}}
region = {{us-west-2}}
output = {{text}}

[profile user1]
sso_session = {{my-sso}}
sso_account_id = {{444455556666}}
sso_role_name = {{readOnly}}
region = {{us-east-1}}
output = {{json}}

[sso-session {{my-sso}}]
sso_region = {{us-east-1}}
sso_start_url = {{https://my-sso-portal.awsapps.com/start}}
sso_registration_scopes = {{sso:account:access}}
```

------
#### [ IAM Identity Center (Legacy SSO) ]

This example is for the legacy method of AWS IAM Identity Center. For more information, see [Configuring IAM Identity Center authentication with the AWS CLI](cli-configure-sso.md).

**Credentials file**

The `credentials` file is not used for this authentication method.

**Config file**

```
[default]
sso_start_url = {{https://my-sso-portal.awsapps.com/start}}
sso_region = {{us-east-1}}
sso_account_id = {{111122223333}}
sso_role_name = {{readOnly}}
region = {{us-west-2}}
output = {{text}}

[profile user1]
sso_start_url = {{https://my-sso-portal.awsapps.com/start}}
sso_region = {{us-east-1}}
sso_account_id = {{444455556666}}
sso_role_name = {{readOnly}}
region = {{us-east-1}}
output = {{json}}
```

------
#### [ Short-term credentials ]

This example is for the short-term credentials from AWS Identity and Access Management. For more information, see [Authenticating with short-term credentials for the AWS CLI](cli-authentication-short-term.md).

**Credentials file**

```
[default]
aws_access_key_id={{ASIAIOSFODNN7EXAMPLE}}
aws_secret_access_key={{wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY}}
aws_session_token = {{IQoJb3JpZ2luX2IQoJb3JpZ2luX2IQoJb3JpZ2luX2IQoJb3JpZ2luX2IQoJb3JpZVERYLONGSTRINGEXAMPLE}}

[user1]
aws_access_key_id={{ASIAI44QH8DHBEXAMPLE}}
aws_secret_access_key={{je7MtGbClwBF/2Zp9Utk/h3yCo8nvbEXAMPLEKEY}}
aws_session_token = {{fcZib3JpZ2luX2IQoJb3JpZ2luX2IQoJb3JpZ2luX2IQoJb3JpZ2luX2IQoJb3JpZVERYLONGSTRINGEXAMPLE}}
```

**Config file**

```
[default]
region={{us-west-2}}
output={{json}}

[profile user1]
region={{us-east-1}}
output={{text}}
```

------
#### [ IAM role ]

This example is for assuming an IAM role. Profiles that use IAM roles pull credentials from another profile, and then apply IAM role permissions. In the following examples, `default` is the source profile for credentials and `user1` borrows the same credentials then assumes a new role. For more information, see [Using an IAM role in the AWS CLI](cli-configure-role.md).

**Credentials file**

The `credentials` file depends on what authentication your source profile uses. For the following example, the source profile uses short-term credentials.

```
[default]
aws_access_key_id={{ASIAIOSFODNN7EXAMPLE}}
aws_secret_access_key={{wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY}}
aws_session_token = {{IQoJb3JpZ2luX2IQoJb3JpZ2luX2IQoJb3JpZ2luX2IQoJb3JpZ2luX2IQoJb3JpZVERYLONGSTRINGEXAMPLE}}
```

**Config file**

```
[default]
region={{us-west-2}}
output={{json}}

[profile user1]
role_arn={{arn:aws:iam::777788889999:role/user1role}}
source_profile={{default}}
role_session_name={{session_user1}}
region={{us-east-1}}
output={{text}}
```

------
#### [ Amazon EC2 instance metadata credentials ]

This example is for the credentials obtained from the hosting Amazon EC2 instance metadata. For more information, see [Using Amazon EC2 instance metadata as credentials in the AWS CLI](cli-configure-metadata.md).

**Credentials file**

The `credentials` file is not used for this authentication method.

**Config file**

```
[default]
role_arn={{arn:aws:iam::123456789012:role/defaultrole}}
credential_source={{Ec2InstanceMetadata}}
region={{us-west-2}}
output={{json}}

[profile user1]
role_arn={{arn:aws:iam::777788889999:role/user1role}}
credential_source={{Ec2InstanceMetadata}}
region={{us-east-1}}
output={{text}}
```

------
#### [ Long-term credentials ]

**Warning**  
To avoid security risks, don't use IAM users for authentication when developing purpose-built software or working with real data. Instead, use federation with an identity provider such as [AWS IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html).

This example is for the long-term credentials from AWS Identity and Access Management. For more information, see [Authenticating using IAM user credentials for the AWS CLI](cli-authentication-user.md).

**Credentials file**

```
[default]
aws_access_key_id={{AKIAIOSFODNN7EXAMPLE}}
aws_secret_access_key={{wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY}}

[user1]
aws_access_key_id={{AKIAI44QH8DHBEXAMPLE}}
aws_secret_access_key={{je7MtGbClwBF/2Zp9Utk/h3yCo8nvbEXAMPLEKEY}}
```

**Config file**

```
[default]
region={{us-west-2}}
output={{json}}

[profile user1]
region={{us-east-1}}
output={{text}}
```

------

For more detailed information on authentication and credential methods see [Authentication and access credentials for the AWS CLI](cli-chap-authentication.md).

## Using existing configuration and credentials files
<a name="getting-started-quickstart-existing"></a>

If you have existing configuration and credentials files, these can be used for the AWS CLI. 

To use the `config` and `credentials` files, move them to the folder named `.aws` in your home directory. Where you find your home directory location varies based on the operating system, but is referred to using the environment variables `%UserProfile%` in Windows and `$HOME` or `~` (tilde) in Unix-based systems. 

You can specify a non-default location for the `config` and `credentials` files by setting the `AWS_CONFIG_FILE` and `AWS_SHARED_CREDENTIALS_FILE` environment variables to another local path. See [Configuring environment variables for the AWS CLI](cli-configure-envvars.md) for details. 

For more detailed information on configuration and credentials files, see [Configuration and credential file settings in the AWS CLI](cli-configure-files.md).
