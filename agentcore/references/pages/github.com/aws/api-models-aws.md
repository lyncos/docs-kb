---
title: AWS API Models
description: aws / **api-models-aws** Public
product: Amazon Bedrock AgentCore
section: References / github.com
source_url: https://github.com/aws/api-models-aws
fetched: '2026-09-26'
tags:
- agentcore
- github-com
- reference
- related
referenced_by:
- gateway-building-smithy-targets.md
conversion: pandoc
---

[aws](/aws) / **[api-models-aws](/aws/api-models-aws)** Public

- [Notifications](/login?return_to=%2Faws%2Fapi-models-aws) You must be signed in to change notification settings

- [Fork 28](/login?return_to=%2Faws%2Fapi-models-aws)

- [ Star 228](/login?return_to=%2Faws%2Fapi-models-aws)

[](/aws/api-models-aws)

main

[Branches](/aws/api-models-aws/branches)[Tags](/aws/api-models-aws/tags)

[](/aws/api-models-aws/branches)[](/aws/api-models-aws/tags)

Go to file

Code

Open more actions menu

## Latest commit

 

## History

[401 Commits](/aws/api-models-aws/commits/main/)

[](/aws/api-models-aws/commits/main/)401 Commits

## Folders and files

[TABLE]

## Repository files navigation

# AWS API Models

[](#aws-api-models)

Warning

This repository is not closely monitored, and the files here are generated from other sources. Because of this, we are unable to accept pull requests and issues related to the service models should be directed to other channels.

For questions related to the AWS SDKs, please visit the respective repository for [SDK specific support](https://github.com/aws). If you have an AWS support plan, you can create a new technical support case in the [AWS Support Center](https://console.aws.amazon.com/support/home#/). Alternatively, you may reach out to general AWS Support [here](https://aws.amazon.com/contact-us/)).

This repository contains [Smithy](https://smithy.io/) models (in the [JSON AST](https://smithy.io/2.0/spec/json-ast.html) form) for all public AWS API services. Smithy is an open-source interface definition language, set of code generators, and developer tools used to generate code for web services and client SDKs from API models. At AWS, we use Smithy extensively to model our service APIs and provide the daily releases of the AWS SDKs and CLIs.

AWS API models can be helpful for a variety of uses cases such as building custom SDKs/CLIs SDKs for use with AWS or implementing MCP servers to interact with AWS services.

## Directory Structure

[](#directory-structure)

The AWS models repository contains a top-level directory, `models`, which contains:

- One directory per public AWS service
  - Note: service directories are named using the `<sdk-id>` of the service, where `<sdk-id>` is the value of the model's [`sdkId`](https://smithy.io/2.0/aws/aws-core.html#sdkid), lowercased and with spaces converted to hyphens
- Each service directory contains one directory per `<version>` of the service, where `<version>` is the value of the service shape's [version property](https://smithy.io/2.0/spec/service-types.html#service)
- Contained within a service-version directory, a model file named `<sdk-id>-<version>.json` will be present

## Learn more

[](#learn-more)

We invite you to learn more about the AWS preferred API modeling language at [smithy.io](https://smithy.io/).

## License

[](#license)

This project is licensed under the [Apache-2.0 License](/aws/api-models-aws/blob/main/LICENSE).

## About

API Models for all public AWS Services

[aws.amazon.com](https://aws.amazon.com)

### Resources

[Readme](#readme-ov-file)

[Apache-2.0 license](#Apache-2.0-1-ov-file)

### Code of conduct

[Code of conduct](/aws/api-models-aws#coc-ov-file)

### Contributing

[Contributing](#contributing-ov-file)

### Security policy

[Security policy](#security-ov-file)

[Activity](/aws/api-models-aws/activity)

[Custom properties](/aws/api-models-aws/custom-properties)

### Stars

**228** stars

### Watchers

**9** watching

### Forks

[**28** forks](/aws/api-models-aws/forks)

[Report repository](/contact/report-content?content_url=https%3A%2F%2Fgithub.com%2Faws%2Fapi-models-aws&report=aws+%28user%29)

## Releases

## Packages

## Used by

## Contributors

## Languages

Generated from [amazon-archives/\_\_template_Apache-2.0](/amazon-archives/__template_Apache-2.0)
