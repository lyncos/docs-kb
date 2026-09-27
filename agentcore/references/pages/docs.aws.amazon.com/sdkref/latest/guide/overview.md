---
title: What is covered in the AWS SDKs and Tools Reference Guide
description: Many SDKs and tools share some common functionality, either through shared design specifications or through a shared library.
product: Amazon Bedrock AgentCore
section: References / docs.aws.amazon.com
source_url: https://docs.aws.amazon.com/sdkref/latest/guide/overview.html
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

# What is covered in the AWS SDKs and Tools Reference Guide
<a name="overview"></a>

Many SDKs and tools share some common functionality, either through shared design specifications or through a shared library. 

This guide includes information regarding:
+ [Globally configuring AWS SDKs and tools](creds-config-files.md) – How to use the shared `config` and `credentials` files or environment variables to configure your AWS SDKs and tools. 
+ [Authentication and access using AWS SDKs and tools](access.md) – Establish how your code or tool authenticates with AWS when you develop with AWS services.
+ [AWS SDKs and tools settings reference](settings-reference.md) – Reference for all standardized settings available for authentication and configuration.
+ [AWS Common Runtime (CRT) libraries](common-runtime.md) – Overview of the shared AWS Common Runtime (CRT) libraries that are available to almost all SDKs.
+ [Protocol support changes for AWS service clients](service-protocol-updates.md) – Information about protocol support changes for AWS service clients and where support is in preview or released.
+ [AWS SDKs and Tools maintenance policy](maint-policy.md) covers the maintenance policy and versioning for AWS Software Development Kits (SDKs) and tools, including Mobile and Internet of Things (IoT) SDKs, and their underlying dependencies.

This AWS SDKs and Tools Reference Guide is intended to be a base of information that is applicable to multiple SDKs and tools. The specific guide for the SDK or tool that you are using should be used in addition to any information presented here. The following are the SDK and tools which have relevant sections of material in this guide: 


| If you are using: | This guide's relevant sections for you are: | 
| --- | --- | 
| +  Any SDK or tool  | [AWS SDKs and Tools maintenance policy](maint-policy.md) | 
| +  [AWS Cloud9](https://docs.aws.amazon.com/cloud9/latest/user-guide/) <br />+  [AWS CDK](https://docs.aws.amazon.com/cdk/latest/guide/) <br />+  [AWS Toolkit for Azure DevOps](https://docs.aws.amazon.com/vsts/latest/userguide/) <br />+  [AWS Toolkit for JetBrains](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/) <br />+  [AWS Toolkit for Visual Studio](https://docs.aws.amazon.com/AWSToolkitVS/latest/UserGuide/) <br />+  [AWS Toolkit for Visual Studio Code](https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/) <br />+  [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/) <br /> <br />+  [AWS CodeArtifact](https://docs.aws.amazon.com/codeartifact/latest/ug/) <br />+  [AWS CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/) <br />+  [Amazon CodeCatalyst](http://docs.aws.amazon.com/codecatalyst/latest/userguide/welcome.html) <br />+  [AWS CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/) <br />+  [AWS CodeDeploy](https://docs.aws.amazon.com/codedeploy/latest/userguide/) <br />+  [AWS CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/)  | [Globally configuring AWS SDKs and tools](creds-config-files.md)<br />[Authentication and access using AWS SDKs and tools](access.md)<br />[AWS SDKs and Tools maintenance policy](maint-policy.md)  | 
| +  [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/) <br />+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/sdk-for-cpp/latest/developer-guide/) <br />+  [AWS SDK for Go](https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/) <br />+  [AWS SDK for Java](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/) <br />+  [AWS SDK for JavaScript](https://docs.aws.amazon.com/sdk-for-javascript/latest/developer-guide/) <br />+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/) <br />+  [AWS SDK for .NET](https://docs.aws.amazon.com/sdk-for-net/latest/developer-guide/) <br />+  [AWS SDK for PHP](https://docs.aws.amazon.com/sdk-for-php/latest/developer-guide/) <br />+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/boto3/latest/) <br />+  [AWS SDK for Ruby](https://docs.aws.amazon.com/sdk-for-ruby/latest/developer-guide/) <br />+  [AWS SDK for Rust](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/) <br />+  [AWS SDK for Swift](https://docs.aws.amazon.com/sdk-for-swift/latest/developer-guide/) <br />+  [AWS Tools for Windows PowerShell](https://docs.aws.amazon.com/powershell/latest/userguide/)  | [Globally configuring AWS SDKs and tools](creds-config-files.md)<br />[Authentication and access using AWS SDKs and tools](access.md)<br />[AWS SDKs and tools settings reference](settings-reference.md)<br />[AWS Common Runtime (CRT) libraries](common-runtime.md)<br />[Protocol support changes for AWS service clients](service-protocol-updates.md)<br />[AWS SDKs and Tools maintenance policy](maint-policy.md)<br />[AWS SDKs and Tools version lifecycle](version-support-matrix.md) | 
+ For an overview of tools that can help you develop applications on AWS, see [Tools to Build on AWS](https://aws.amazon.com/tools/). 
+ For information on support, see the [AWS Knowledge Center](https://aws.amazon.com/premiumsupport/knowledge-center/). 
+ For AWS terminology, see the [AWS glossary](https://docs.aws.amazon.com/glossary/latest/reference/glos-chap.html) in the *AWS Glossary Reference*.

## Developer resources
<a name="resources"></a>

Amazon Q Developer is a generative AI-powered conversational assistant that can help you to understand, build, extend, and operate AWS applications. To accelerate your building on AWS, the model that powers Amazon Q is augmented with high-quality AWS content to produce more complete, actionable, and referenced answers. For more information, see [What is Amazon Q Developer?](https://docs.aws.amazon.com/amazonq/latest/aws-builder-use-ug/what-is.html) in the *Amazon Q Developer User Guide*. 

### Toolkit telemetry notification
<a name="support-maint-idetoolkits-telemetry"></a>

AWS Integrated Development Environment (IDE) Toolkits are plugins and extensions that enable access to AWS services in your IDE. Amazon Q IDE plugins and extensions enable generative AI assistance in your IDE. For detailed information about each of the IDE Toolkits, see the Toolkit User Guides in the preceding table. To learn more about using Amazon Q in your IDE, see the [Using Amazon Q in the IDE](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/q-in-IDE.html) topic in the *Amazon Q* developer guide.

 AWS IDE Toolkits and Amazon Q may collect and store client-side telemetry data to inform decisions regarding future AWS Toolkit and Amazon Q releases. The data collected quantifies your usage of the AWS Toolkit and Amazon Q. 

To learn more about the telemetry data collected across all of the AWS IDE Toolkits and Amazon Q, see the [commonDefinitions.json](https://github.com/aws/aws-toolkit-common/blob/main/telemetry/definitions/commonDefinitions.json) document in the `aws-toolkit-common` Github repository.

 For detailed information about the telemetry data collected by each of the AWS IDE Toolkits and Amazon Q extensions, reference the resource documents in the following AWS Toolkit GitHub repositories: 
+ [AWS Visual Studio Toolkit with Amazon Q](https://github.com/aws/aws-toolkit-visual-studio/blob/main/Telemetry/vs-telemetry-definitions.json)
+ [AWS Toolkit for Visual Studio Code and Amazon Q extension for VS Code](https://github.com/aws/aws-toolkit-vscode/blob/master/packages/core/src/shared/telemetry/vscodeTelemetry.json)
+ [AWS Toolkit for JetBrains and Amazon Q plugin for JetBrains](https://github.com/aws/aws-toolkit-jetbrains/blob/main/plugins/core/jetbrains-community/resources/telemetryOverride.json)
+ [Amazon Q for Eclipse](https://github.com/aws/amazon-q-eclipse/blob/main/plugin/codegen-resources/definitions/commonDefinitions.json)

 Certain AWS services that are accessible in the AWS Toolkits may collect additional client-side telemetry data. For detailed information about the type of data collected by each individual AWS service, see the [AWS Documentation](https://docs.aws.amazon.com/) topic for the specific service you're interested in.
