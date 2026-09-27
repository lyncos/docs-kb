---
title: Getting started with the AWS CLI
description: This chapter provides steps to get started with version 2 of the AWS Command Line Interface (AWS CLI) and provides links to the relevant instructions.
product: Amazon Bedrock AgentCore
section: References / docs.aws.amazon.com
source_url: https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html
fetched: '2026-09-26'
tags:
- agent-registry
- agentcore
- docs-aws-amazon-com
- reference
- related
referenced_by:
- gateway-quick-start.md
- gateway-setup-tools-credentials.md
- registry-prerequisites.md
conversion: native-md
---

# Getting started with the AWS CLI
<a name="cli-chap-getting-started"></a>

This chapter provides steps to get started with version 2 of the AWS Command Line Interface (AWS CLI) and provides links to the relevant instructions. 

1. **[Complete all prerequisites](getting-started-prereqs.md)** - To access AWS services with the AWS CLI, you need at minimum an AWS account and IAM credentials. To increase the security of your AWS account, we recommend that you do not use your root account credentials. You should create a user with least privilege to provide access credentials to the tasks you'll be running in AWS. 

1. Install or gain access to the AWS CLI using one of the following methods:
   + **(Recommended)** [Installing or updating to the latest version of the AWS CLI](getting-started-install.md).
   + [Installing past releases of the AWS CLI version 2](getting-started-version.md). Installing a specific version is primarily used if your team aligns their tools to a specific version.
   + [Building and installing the AWS CLI from source](getting-started-source-install.md). Building the AWS CLI from GitHub source is a more in-depth method that is primarily used by customers who work on platforms that we do not directly support with our pre-built installers.
   + [Running the official Amazon ECR Public or Docker images for the AWS CLI](getting-started-docker.md).
   + Access the AWS CLI version 2 in the AWS console from your browser using AWS CloudShell. For more information, see the [AWS CloudShell User Guide](https://docs.aws.amazon.com/cloudshell/latest/userguide/).

1. [After you have access to the AWS CLI, configure your AWS CLI with your IAM credentials for first time use](getting-started-quickstart.md).

**Troubleshooting installer or configure errors**  
If you have issues after installing, uninstalling, or configuring the AWS CLI, see [Troubleshooting errors for the AWS CLI](cli-chap-troubleshooting.md) for troubleshooting steps.

**Topics**
+ [Prerequisites to use the AWS CLI version 2](getting-started-prereqs.md)
+ [Installing or updating to the latest version of the AWS CLI](getting-started-install.md)
+ [Installing past releases of the AWS CLI version 2](getting-started-version.md)
+ [Building and installing the AWS CLI from source](getting-started-source-install.md)
+ [Running the official Amazon ECR Public or Docker images for the AWS CLI](getting-started-docker.md)
+ [Setting up the AWS CLI](getting-started-quickstart.md)
