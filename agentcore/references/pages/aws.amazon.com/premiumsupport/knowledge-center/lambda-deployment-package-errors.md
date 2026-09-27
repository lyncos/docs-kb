---
title: How do I troubleshoot "permission denied" or "unable to import module" errors when I upload a Lambda deployment package?
description: 'AWS Builder Center: Learn, Build and Connect with builders in the AWS community'
product: Amazon Bedrock AgentCore
section: References / aws.amazon.com
source_url: http://aws.amazon.com/premiumsupport/knowledge-center/lambda-deployment-package-errors
fetched: '2026-09-26'
tags:
- agentcore
- aws-amazon-com
- reference
- related
referenced_by:
- runtime-get-started-code-deploy.md
conversion: pandoc
---

AWS Builder Center: Learn, Build and Connect with builders in the AWS community

[AWS Builder Center](https://builder.aws.com/start?trk=a71b0e56-319f-414d-a43c-78ffb7e3eeb3&sc_channel=el) is the official home for builders on AWS. Share and read what others are working on, follow people who inspire you, explore training and workshops, and find tools to support what you're building.

# How do I troubleshoot "permission denied" or "unable to import module" errors when I upload a Lambda deployment package?

5 minute read

0

When I upload my AWS Lambda deployment package, I get either a "permission denied" or "unable to import module" error.

## Short description

Lambda requires global read permissions on code files and any dependent libraries in your deployment package. If you don't configure your [Lambda deployment package](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-package.html) with the correct security permissions, then Lambda returns an error when you try to upload the file. The **permission denied** and **unable to import module** errors commonly occur when [continuous integration applications](https://aws.amazon.com/devops/continuous-integration/) create deployment packages.

For interpreted runtimes, such as Python, the correct permission for the files in the deployment package is **644**. For folders in the deployment package, the correct permission is **755**.

For compiled runtimes, such as Go, the correct permission for executable files and directories in a deployment package is **755** in Unix permissions numeric notation.

**Note:** Because Lambda uses POSIX permissions, it's a best practice to use a POSIX compliant operating system (OS) when you build Lambda deployment packages. Compliant OSs include Linux, Unix, or macOS. Equality between the permissions model in your build environment and Lambda's runtime environment reduces the chance of permissions issues.

To fix a permissions issue as a Windows user, complete one of the following tasks to set up a Linux environment:

- Install a Linux distribution on your PC. For more information, see [How to install Linux on Windows with WSL](https://learn.microsoft.com/en-us/windows/wsl/install) on the Microsoft website.
- Use [Lambda's Amazon Machine Image (AMI)](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html) to launch an Amazon Elastic Compute Cloud (Amazon EC2) instance.

## Resolution

### Find the file or folder that's causing the error

Depending on the [programing language you used to write your Lambda function code](https://docs.aws.amazon.com/lambda/latest/dg/deploying-lambda-apps.html), the cause of the error might not be clear in the error message.

For example, a Node.js function error message lists the name of the file or folder that's the source of the error. However, a Python function error message doesn't list the name of the file or folder that's the source of the error.

**Example of a Node.js Lambda function permission denied error**

    {  "errorMessage": "EACCES: permission denied, open '/var/task/index.js'",      "errorType": "Error",  
        "stackTrace": [  
        "Object.fs.openSync (fs.js:641:18)",  
        "Object.fs.readFileSync (fs.js:509:33)",  
        "Object.Module._extensions..js (module.js:578:20)",  
        "Module.load (module.js:487:32)",  
        "tryModuleLoad (module.js:446:12)",  
        "Function.Module._load (module.js:438:3)",  
        "Module.require (module.js:497:17)",  
        "require (internal/module.js:20:19)"  
      ]   
    }

**Example of a Python Lambda function unable to import module error**

"Unable to import module 'index': No module named index"

To fix this error, see [How do I resolve the "Unable to import module" error that I receive when I run Lambda code in Python?](https://repost.aws/knowledge-center/lambda-import-module-error-python)

If your Lambda deployment package isn't Amazon Linux 2 or Amazon Linux 2023, then you must match compatibility with Amazon Linux versions. To do this, use the following parameters when you install the package. The following example uses a Python 3.12 OS and NumPy libraries in the same folder where Lambda function is:

    pip3 install --platform manylinux2014_x86_64 --target . --python-version 3.12 --only-binary=:all: numpy

Based on your use case, adjust the following values: 

- Th **platform manylinux2014_x86_64** value specifies the package's platform.
- The **python-version 3.12** value indicates that the package is compatible with the specified Python version. Adjust this value according to the Python runtime version that you target in Lambda.
- The **only-binary=:all** parameter instructs pip to download only binaries. This makes sure that the package is compatible with the Lambda runtime environment.

**Example of a Python Lambda function error for external libraries that are missing required permissions**

"Unable to import module 'index': No module named requests"

To check the permissions for all files and folders in the deployment package .zip file, run the **zipinfo** command in your command line interface (CLI):

    zipinfo lambda-package.zip

**Note:** Replace **lambda-package.zip** with your deployment package .zip file name.

**Example of zipinfo command response**

    Archive:  lambda-package.zipZip file size: 305 bytes, number of entries: 1-r--------  3.0 unx      188 tx defN 21-Feb-13 20:48 example.py
    1 file, 188 bytes uncompressed, 135 bytes compressed:  28.2%

**Note:** In the preceding example, the permission for **example.py** is **-r--------**, or **400** in Unix permissions numeric notation. Update the permission for the file to **644**. For more information, see [Notation of traditional Unix permissions](https://en.wikipedia.org/wiki/File-system_permissions#Notation_of_traditional_Unix_permissions) on the Wikipedia website.

### Update the permissions for your deployment package

**Note:** The following commands work only for Linux, Unix, and macOS.

1.  To unpack the files and folders inside your deployment package to a temporary folder, run the following command in your CLI:

        mkdir temp-folder; unzip lambda-package.zip -d temp-folder ;cd temp-folder;ls -l

    **Note:** Replace **lambda-package.zip** with the file name of your deployment package and **temp-folder** with a name for the temporary folder.

2.  [Update the permissions of the library's files](https://docs.aws.amazon.com/lambda/latest/dg/troubleshooting-deployment.html#troubleshooting-deployment-denied).  
    **Note:** To make the directories executable and all files and folders in the unzipped deployment package readable by any user, run the **chmod** command:

        $ sudo chmod 644 $(find -type f) && chmod 755 $(find -type d)

    To make the unzipped deployment package files executable for compiled runtimes, run the following command:

        $ chmod 755 -R

3.  After you fix the permissions, run the following command to repackage the files and folder into a new .zip file:

        zip -r new-lambda-package.zip *

4.  [Upload the new deployment package](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-package.html#gettingstarted-package-zip).

Follow

Share

Topics  
[Compute](/topics/TA8YtFU8qJSXmTuZEBXRRQRg/compute)

Tags  
[AWS Lambda](/tags/TA5uNafDy2TpGNjidWLMSxDw/aws-lambda)

Language  
English

[![](/static/images/aws.png)](/aws-official)

[AWS OFFICIAL](/aws-official)Updated 3 years ago

No comments

Comment on this article

Clear

Post comment

## Relevant content

- [Error when trying to import package installed using lambda layer on nodejs14 ES module enabled lambda function](/questions/QUZs72yAJTQYuHr-OCk8fbyg/error-when-trying-to-import-package-installed-using-lambda-layer-on-nodejs14-es-module-enabled-lambda-function)

  [User-9670910](/community/users/USx9vDWw9OSZGwrcTtuZCRYQ)

  asked 5 years ago

- [error, "Unable to import module 'lambda_function': No module named 'requests'"](/questions/QUop6kd2TAQ9mHn-GFOfnbuQ/error-unable-to-import-module-lambda-function-no-module-named-requests)

  [DivZero](/community/users/USJ4xv1F9dQben0Xp-c9dKww)

  asked 3 years ago

- [Error with imports when trying to upload code to Lambda Function](/questions/QUt7g1mCL4QtiPnhD-BJPuLA/error-with-imports-when-trying-to-upload-code-to-lambda-function)

  [rePost-User-1836891](/community/users/USVwUvEPJCQziIoqPnoQQzdg)

  asked 3 years ago

- [How can I create deployment package for my lambda to work with my libraries or an alternative solution?](/questions/QUKVCi9EUIQESutNPS9njajg/how-can-i-create-deployment-package-for-my-lambda-to-work-with-my-libraries-or-an-alternative-solution)

  [User-5267765](/community/users/US49F4B1dzQt6wpZM3J5X52A)

  asked 4 years ago

- [When I try to run a python code on Lambda functions I got an error message related with regex module.](/questions/QUddCozSbYS92q8ZKRfAHZDQ/when-i-try-to-run-a-python-code-on-lambda-functions-i-got-an-error-message-related-with-regex-module)

  [rePost-User-6899729](/community/users/US4ts8bCfMTbOsfokrGDYGFw)

  asked 3 years ago

- [How do I build a Lambda deployment package for Node.js?](/knowledge-center/lambda-deployment-package-nodejs)

  [![](/static/images/aws.png)](/aws-official)
  [AWS OFFICIAL](/aws-official)Updated 4 years ago

- [How do I install a Lambda compatible Python deployment package with compiled code on macOS or Windows OS?](/knowledge-center/lambda-python-package-compatible)

  [![](/static/images/aws.png)](/aws-official)
  [AWS OFFICIAL](/aws-official)Updated 5 months ago

- [How do I resolve "Cannot find module" or "Cannot find Package" errors when I run Lambda code in Node.js?](/knowledge-center/lambda-import-module-error-nodejs)

  [![](/static/images/aws.png)](/aws-official)
  [AWS OFFICIAL](/aws-official)Updated 7 months ago

- [How do I build a Lambda deployment package for C# .NET?](/knowledge-center/build-lambda-deployment-dotnet)

  [![](/static/images/aws.png)](/aws-official)
  [AWS OFFICIAL](/aws-official)Updated 5 years ago

- [How to troubleshoot error “Uploaded file must be a non_empty zip” when updating a Lambda function using AWS CloudFormation ?](/articles/AR7o2H4M44QY6TtF8S6vqpDQ/how-to-troubleshoot-error-uploaded-file-must-be-a-non-empty-zip-when-updating-a-lambda-function-using-aws-cloud-formation)

  ![](/media/profilePicture/thumbnails/small/IMAwHlbuHuRF2meiUVZWEUBw)![AWS](/static/icons/common/aws_logo_rgb_squid.svg)

  SUPPORT ENGINEER
  [Nikhil](/community/users/USV-8BBRjCRdyJZS6YxXyHog)

  published a year ago

FEEDBACK
