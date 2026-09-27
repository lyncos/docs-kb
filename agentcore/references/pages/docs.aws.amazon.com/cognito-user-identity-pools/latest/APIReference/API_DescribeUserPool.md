---
title: DescribeUserPool
description: Given a user pool ID, returns configuration information. This operation is useful when you want to inspect an existing user pool and programmatically replicate the configuration to another user pool.
product: Amazon Bedrock AgentCore
section: References / docs.aws.amazon.com
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DescribeUserPool.html
fetched: '2026-09-26'
tags:
- agentcore
- docs-aws-amazon-com
- reference
- related
referenced_by:
- gateway-using-auth-ex-starter.md
conversion: native-md
---

# DescribeUserPool
<a name="API_DescribeUserPool"></a>

Given a user pool ID, returns configuration information. This operation is useful when you want to inspect an existing user pool and programmatically replicate the configuration to another user pool.

**Note**  
Amazon Cognito evaluates AWS Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.  
 [Signing AWS API Requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html) 
 [Using the Amazon Cognito user pools API and user pool endpoints](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html) 

## Request Syntax
<a name="API_DescribeUserPool_RequestSyntax"></a>

```
{
   "UserPoolId": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeUserPool_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [UserPoolId](#API_DescribeUserPool_RequestSyntax) **   <a name="CognitoUserPools-DescribeUserPool-request-UserPoolId"></a>
The ID of the user pool you want to describe.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 55.  
Pattern: `[\w-]+_[0-9a-zA-Z]+`   
Required: Yes

## Response Syntax
<a name="API_DescribeUserPool_ResponseSyntax"></a>

```
{
   "UserPool": { 
      "AccountRecoverySetting": { 
         "RecoveryMechanisms": [ 
            { 
               "Name": "string",
               "Priority": number
            }
         ]
      },
      "AdminCreateUserConfig": { 
         "AllowAdminCreateUserOnly": boolean,
         "InviteMessageTemplate": { 
            "EmailMessage": "string",
            "EmailSubject": "string",
            "SMSMessage": "string"
         },
         "UnusedAccountValidityDays": number
      },
      "AliasAttributes": [ "string" ],
      "Arn": "string",
      "AutoVerifiedAttributes": [ "string" ],
      "CreationDate": number,
      "CustomDomain": "string",
      "DeletionProtection": "string",
      "DeviceConfiguration": { 
         "ChallengeRequiredOnNewDevice": boolean,
         "DeviceOnlyRememberedOnUserPrompt": boolean
      },
      "Domain": "string",
      "EmailConfiguration": { 
         "ConfigurationSet": "string",
         "EmailSendingAccount": "string",
         "From": "string",
         "ReplyToEmailAddress": "string",
         "SourceArn": "string"
      },
      "EmailConfigurationFailure": "string",
      "EmailVerificationMessage": "string",
      "EmailVerificationSubject": "string",
      "EstimatedNumberOfUsers": number,
      "Id": "string",
      "IssuerConfiguration": { 
         "Type": "string"
      },
      "KeyConfiguration": { 
         "KeyType": "string",
         "KmsKeyArn": "string"
      },
      "LambdaConfig": { 
         "CreateAuthChallenge": "string",
         "CustomEmailSender": { 
            "LambdaArn": "string",
            "LambdaVersion": "string"
         },
         "CustomMessage": "string",
         "CustomSMSSender": { 
            "LambdaArn": "string",
            "LambdaVersion": "string"
         },
         "DefineAuthChallenge": "string",
         "InboundFederation": { 
            "LambdaArn": "string",
            "LambdaVersion": "string"
         },
         "KMSKeyID": "string",
         "PostAuthentication": "string",
         "PostConfirmation": "string",
         "PreAuthentication": "string",
         "PreSignUp": "string",
         "PreTokenGeneration": "string",
         "PreTokenGenerationConfig": { 
            "LambdaArn": "string",
            "LambdaVersion": "string"
         },
         "UserMigration": "string",
         "VerifyAuthChallengeResponse": "string"
      },
      "LastModifiedDate": number,
      "MfaConfiguration": "string",
      "Name": "string",
      "Policies": { 
         "PasswordPolicy": { 
            "MinimumLength": number,
            "PasswordHistorySize": number,
            "RequireLowercase": boolean,
            "RequireNumbers": boolean,
            "RequireSymbols": boolean,
            "RequireUppercase": boolean,
            "TemporaryPasswordValidityDays": number
         },
         "SignInPolicy": { 
            "AllowedFirstAuthFactors": [ "string" ]
         }
      },
      "SchemaAttributes": [ 
         { 
            "AttributeDataType": "string",
            "DeveloperOnlyAttribute": boolean,
            "Mutable": boolean,
            "Name": "string",
            "NumberAttributeConstraints": { 
               "MaxValue": "string",
               "MinValue": "string"
            },
            "Required": boolean,
            "StringAttributeConstraints": { 
               "MaxLength": "string",
               "MinLength": "string"
            }
         }
      ],
      "SmsAuthenticationMessage": "string",
      "SmsConfiguration": { 
         "EumsSms": { 
            "CallerArn": "string",
            "ConfigurationSetName": "string",
            "ExternalId": "string",
            "InEntityId": "string",
            "InTemplateId": "string",
            "OriginationIdentity": "string",
            "Region": "string"
         },
         "ExternalId": "string",
         "SnsCallerArn": "string",
         "SnsRegion": "string"
      },
      "SmsConfigurationFailure": "string",
      "SmsVerificationMessage": "string",
      "Status": "string",
      "UserAttributeUpdateSettings": { 
         "AttributesRequireVerificationBeforeUpdate": [ "string" ]
      },
      "UsernameAttributes": [ "string" ],
      "UsernameConfiguration": { 
         "CaseSensitive": boolean
      },
      "UserPoolAddOns": { 
         "AdvancedSecurityAdditionalFlows": { 
            "CustomAuthMode": "string"
         },
         "AdvancedSecurityMode": "string"
      },
      "UserPoolTags": { 
         "string" : "string" 
      },
      "UserPoolTier": "string",
      "VerificationMessageTemplate": { 
         "DefaultEmailOption": "string",
         "EmailMessage": "string",
         "EmailMessageByLink": "string",
         "EmailSubject": "string",
         "EmailSubjectByLink": "string",
         "SmsMessage": "string"
      }
   }
}
```

## Response Elements
<a name="API_DescribeUserPool_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [UserPool](#API_DescribeUserPool_ResponseSyntax) **   <a name="CognitoUserPools-DescribeUserPool-response-UserPool"></a>
The details of the requested user pool.  
Type: [UserPoolType](API_UserPoolType.md) object

## Errors
<a name="API_DescribeUserPool_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalErrorException **   
This exception is thrown when Amazon Cognito encounters an internal error.    
 ** message **   
The message returned when Amazon Cognito throws an internal error exception.
HTTP Status Code: 500

 ** InvalidParameterException **   
This exception is thrown when the Amazon Cognito service encounters an invalid parameter.    
 ** message **   
The message returned when the Amazon Cognito service throws an invalid parameter exception.  
 ** reasonCode **   
The reason code of the exception.
HTTP Status Code: 400

 ** NotAuthorizedException **   
This exception is thrown when a user isn't authorized.    
 ** message **   
The message returned when the Amazon Cognito service returns a not authorized exception.
HTTP Status Code: 400

 ** OperationNotEnabledException **   
This exception is thrown when an operation is not available in the current region or for the current user pool configuration. This can occur when attempting to perform operations that are not supported in secondary replica regions.  
HTTP Status Code: 400

 ** ResourceNotFoundException **   
This exception is thrown when the Amazon Cognito service can't find the requested resource.    
 ** message **   
The message returned when the Amazon Cognito service returns a resource not found exception.
HTTP Status Code: 400

 ** TooManyRequestsException **   
This exception is thrown when the user has made too many requests for a given operation.    
 ** message **   
The message returned when the Amazon Cognito service returns a too many requests exception.
HTTP Status Code: 400

 ** UserPoolTaggingException **   
This exception is thrown when a user pool tag can't be set or updated.  
HTTP Status Code: 400

## Examples
<a name="API_DescribeUserPool_Examples"></a>

### Example
<a name="API_DescribeUserPool_Example_1"></a>

The following example request describes the user pool `us-east-1_EXAMPLE`.

#### Sample Request
<a name="API_DescribeUserPool_Example_1_Request"></a>

```
POST HTTP/1.1
Host: cognito-idp.us-east-1.amazonaws.com
X-Amz-Date: 20230613T200059Z
Accept-Encoding: gzip, deflate, br
X-Amz-Target: AWSCognitoIdentityProviderService.DescribeUserPool
User-Agent: <UserAgentString>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>
{
   "UserPoolId": "us-east-1_EXAMPLE"
}
```

#### Sample Response
<a name="API_DescribeUserPool_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Tue, 13 Jun 2023 20:00:59 GMT
Content-Type: application/x-amz-json-1.0
Content-Length: <PayloadSizeBytes>
x-amzn-requestid: a1b2c3d4-e5f6-a1b2-c3d4-EXAMPLE11111
Connection: keep-alive

{
    "UserPool": {
        "AccountRecoverySetting": {
            "RecoveryMechanisms": [
                {
                    "Name": "verified_email",
                    "Priority": 1
                }
            ]
        },
        "AdminCreateUserConfig": {
            "AllowAdminCreateUserOnly": false,
            "InviteMessageTemplate": {
                "EmailMessage": "Your username is {username} and temporary password is {####}.",
                "EmailSubject": "Your sign-in information",
                "SMSMessage": "Your username is {username} and temporary password is {####}."
            },
            "UnusedAccountValidityDays": 7
        },
        "AliasAttributes": [
            "email"
        ],
        "Arn": "arn:aws:cognito-idp:us-east-1:123456789012:userpool/us-east-1_EXAMPLE",
        "AutoVerifiedAttributes": [
            "email"
        ],
        "CreationDate": 1689721665.239,
        "DeletionProtection": "ACTIVE",
        "DeviceConfiguration": {
            "ChallengeRequiredOnNewDevice": true,
            "DeviceOnlyRememberedOnUserPrompt": true
        },
        "EmailConfiguration": {
            "ConfigurationSet": "my-test-ses-configuration-set",
            "EmailSendingAccount": "DEVELOPER",
            "From": "support@example.com",
            "ReplyToEmailAddress": "support@example.com",
            "SourceArn": "arn:aws:ses:us-east-1:123456789012:identity/support@example.com"
        },
        "EmailVerificationMessage": "Your verification code is {####}.",
        "EmailVerificationSubject": "Verify your email address",
        "EstimatedNumberOfUsers": 0,
        "Id": "us-east-1_EXAMPLE",
        "LambdaConfig": {
            "CustomEmailSender": {
                "LambdaArn": "arn:aws:lambda:us-east-1:123456789012:function:MyFunction",
                "LambdaVersion": "V1_0"
            },
            "CustomMessage": "arn:aws:lambda:us-east-1:123456789012:function:MyFunction",
            "CustomSMSSender": {
                "LambdaArn": "arn:aws:lambda:us-east-1:123456789012:function:MyFunction",
                "LambdaVersion": "V1_0"
            },
            "DefineAuthChallenge": "arn:aws:lambda:us-east-1:123456789012:function:MyFunction",
            "KMSKeyID": "arn:aws:kms:us-east-1:767671399759:key/4d43904c-8edf-4bb4-9fca-fb1a80e41cbe",
            "PostAuthentication": "arn:aws:lambda:us-east-1:123456789012:function:MyFunction",
            "PostConfirmation": "arn:aws:lambda:us-east-1:123456789012:function:MyFunction",
            "PreAuthentication": "arn:aws:lambda:us-east-1:123456789012:function:MyFunction",
            "PreSignUp": "arn:aws:lambda:us-east-1:123456789012:function:MyFunction",
            "PreTokenGeneration": "arn:aws:lambda:us-east-1:123456789012:function:MyFunction",
            "UserMigration": "arn:aws:lambda:us-east-1:123456789012:function:MyFunction",
            "VerifyAuthChallengeResponse": "arn:aws:lambda:us-east-1:123456789012:function:MyFunction",
            "InboundFederation": {
                "LambdaArn": "arn:aws:lambda:us-east-1:123456789012:function:MyFunction",
                "LambdaVersion": "V1_0"
            }
        },
        "LastModifiedDate": 1689721665.239,
        "MfaConfiguration": "OPTIONAL",
        "Name": "my-test-user-pool",
        "Policies": {
            "PasswordPolicy": {
                "MinimumLength": 6,
                "RequireLowercase": true,
                "RequireNumbers": true,
                "RequireSymbols": true,
                "RequireUppercase": true,
                "TemporaryPasswordValidityDays": 7
            }
        },
        "SchemaAttributes": [
            {
                "AttributeDataType": "String",
                "DeveloperOnlyAttribute": false,
                "Mutable": false,
                "Name": "sub",
                "Required": true,
                "StringAttributeConstraints": {
                    "MaxLength": "2048",
                    "MinLength": "1"
                }
            },
            {
                "AttributeDataType": "String",
                "DeveloperOnlyAttribute": false,
                "Mutable": true,
                "Name": "name",
                "Required": false,
                "StringAttributeConstraints": {
                    "MaxLength": "2048",
                    "MinLength": "0"
                }
            },
            {
                "AttributeDataType": "String",
                "DeveloperOnlyAttribute": false,
                "Mutable": true,
                "Name": "given_name",
                "Required": false,
                "StringAttributeConstraints": {
                    "MaxLength": "2048",
                    "MinLength": "0"
                }
            },
            {
                "AttributeDataType": "String",
                "DeveloperOnlyAttribute": false,
                "Mutable": true,
                "Name": "family_name",
                "Required": false,
                "StringAttributeConstraints": {
                    "MaxLength": "2048",
                    "MinLength": "0"
                }
            },
            {
                "AttributeDataType": "String",
                "DeveloperOnlyAttribute": false,
                "Mutable": true,
                "Name": "middle_name",
                "Required": false,
                "StringAttributeConstraints": {
                    "MaxLength": "2048",
                    "MinLength": "0"
                }
            },
            {
                "AttributeDataType": "String",
                "DeveloperOnlyAttribute": false,
                "Mutable": true,
                "Name": "nickname",
                "Required": false,
                "StringAttributeConstraints": {
                    "MaxLength": "2048",
                    "MinLength": "0"
                }
            },
            {
                "AttributeDataType": "String",
                "DeveloperOnlyAttribute": false,
                "Mutable": true,
                "Name": "preferred_username",
                "Required": false,
                "StringAttributeConstraints": {
                    "MaxLength": "2048",
                    "MinLength": "0"
                }
            },
            {
                "AttributeDataType": "String",
                "DeveloperOnlyAttribute": false,
                "Mutable": true,
                "Name": "profile",
                "Required": false,
                "StringAttributeConstraints": {
                    "MaxLength": "2048",
                    "MinLength": "0"
                }
            },
            {
                "AttributeDataType": "String",
                "DeveloperOnlyAttribute": false,
                "Mutable": true,
                "Name": "picture",
                "Required": false,
                "StringAttributeConstraints": {
                    "MaxLength": "2048",
                    "MinLength": "0"
                }
            },
            {
                "AttributeDataType": "String",
                "DeveloperOnlyAttribute": false,
                "Mutable": true,
                "Name": "website",
                "Required": false,
                "StringAttributeConstraints": {
                    "MaxLength": "2048",
                    "MinLength": "0"
                }
            },
            {
                "AttributeDataType": "String",
                "DeveloperOnlyAttribute": false,
                "Mutable": true,
                "Name": "email",
                "Required": false,
                "StringAttributeConstraints": {
                    "MaxLength": "2048",
                    "MinLength": "0"
                }
            },
            {
                "AttributeDataType": "Boolean",
                "DeveloperOnlyAttribute": false,
                "Mutable": true,
                "Name": "email_verified",
                "Required": false
            },
            {
                "AttributeDataType": "String",
                "DeveloperOnlyAttribute": false,
                "Mutable": true,
                "Name": "gender",
                "Required": false,
                "StringAttributeConstraints": {
                    "MaxLength": "2048",
                    "MinLength": "0"
                }
            },
            {
                "AttributeDataType": "String",
                "DeveloperOnlyAttribute": false,
                "Mutable": true,
                "Name": "birthdate",
                "Required": false,
                "StringAttributeConstraints": {
                    "MaxLength": "10",
                    "MinLength": "10"
                }
            },
            {
                "AttributeDataType": "String",
                "DeveloperOnlyAttribute": false,
                "Mutable": true,
                "Name": "zoneinfo",
                "Required": false,
                "StringAttributeConstraints": {
                    "MaxLength": "2048",
                    "MinLength": "0"
                }
            },
            {
                "AttributeDataType": "String",
                "DeveloperOnlyAttribute": false,
                "Mutable": true,
                "Name": "locale",
                "Required": false,
                "StringAttributeConstraints": {
                    "MaxLength": "2048",
                    "MinLength": "0"
                }
            },
            {
                "AttributeDataType": "String",
                "DeveloperOnlyAttribute": false,
                "Mutable": true,
                "Name": "phone_number",
                "Required": false,
                "StringAttributeConstraints": {
                    "MaxLength": "2048",
                    "MinLength": "0"
                }
            },
            {
                "AttributeDataType": "Boolean",
                "DeveloperOnlyAttribute": false,
                "Mutable": true,
                "Name": "phone_number_verifie",
                "Required": false
            },
            {
                "AttributeDataType": "String",
                "DeveloperOnlyAttribute": false,
                "Mutable": true,
                "Name": "address",
                "Required": false,
                "StringAttributeConstraints": {
                    "MaxLength": "2048",
                    "MinLength": "0"
                }
            },
            {
                "AttributeDataType": "Number",
                "DeveloperOnlyAttribute": false,
                "Mutable": true,
                "Name": "updated_at",
                "NumberAttributeConstraints": {
                    "MinValue": "0"
                },
                "Required": false
            },
            {
                "AttributeDataType": "Number",
                "DeveloperOnlyAttribute": true,
                "Mutable": true,
                "Name": "dev:custom:mydev",
                "NumberAttributeConstraints": {
                    "MaxValue": "99",
                    "MinValue": "1"
                },
                "Required": false
            }
        ],
        "SmsAuthenticationMessage": "Your verification code is {####}.",
        "SmsConfiguration": {
            "ExternalId": "my-role-external-id",
            "SnsCallerArn": "arn:aws:iam::123456789012:role/service-role/test-cognito-SMS-Role",
            "SnsRegion": "us-east-1"
        },
        "SmsVerificationMessage": "Your verification code is {####}.",
        "UserAttributeUpdateSettings": {
            "AttributesRequireVerificationBeforeUpdate": [
                "email"
            ]
        },
        "UserPoolAddOns": {
            "AdvancedSecurityMode": "OFF"
        },
        "UserPoolTags": {
            "my-test-tag-key": "my-test-tag-value"
        },
        "UserPoolTier": "ESSENTIALS",
        "UsernameConfiguration": {
            "CaseSensitive": true
        },
        "VerificationMessageTemplate": {
            "DefaultEmailOption": "CONFIRM_WITH_CODE",
            "EmailMessage": "Your confirmation code is {####}",
            "EmailMessageByLink": "Choose this link to {##verify your email##}",
            "EmailSubject": "Here is your confirmation code",
            "EmailSubjectByLink": "Here is your confirmation link",
            "SmsMessage": "Your confirmation code is {####}"
        }
    }
}
```

## See Also
<a name="API_DescribeUserPool_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cognito-idp-2016-04-18/DescribeUserPool) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cognito-idp-2016-04-18/DescribeUserPool) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/DescribeUserPool) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cognito-idp-2016-04-18/DescribeUserPool) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/DescribeUserPool) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cognito-idp-2016-04-18/DescribeUserPool) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cognito-idp-2016-04-18/DescribeUserPool) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cognito-idp-2016-04-18/DescribeUserPool) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cognito-idp-2016-04-18/DescribeUserPool) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/DescribeUserPool)
