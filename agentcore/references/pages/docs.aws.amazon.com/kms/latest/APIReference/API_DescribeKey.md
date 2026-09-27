---
title: DescribeKey
description: Provides detailed information about a KMS key. You can run `DescribeKey` on a customer managed key or an AWS managed key.
product: Amazon Bedrock AgentCore
section: References / docs.aws.amazon.com
source_url: https://docs.aws.amazon.com/kms/latest/APIReference/API_DescribeKey.html
fetched: '2026-09-26'
tags:
- agent-registry
- agentcore
- docs-aws-amazon-com
- reference
- related
referenced_by:
- registry-data-encryption.md
conversion: native-md
---

# DescribeKey
<a name="API_DescribeKey"></a>

Provides detailed information about a KMS key. You can run `DescribeKey` on a [customer managed key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-mgn-key) or an [AWS managed key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-managed-key).

This detailed information includes the key ARN, creation date (and deletion date, if applicable), the key state, and the origin and expiration date (if any) of the key material. It includes fields, like `KeySpec`, that help you distinguish different types of KMS keys. It also displays the key usage (encryption, signing, or generating and verifying MACs) and the algorithms that the KMS key supports. 

For [multi-Region keys](https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html), `DescribeKey` displays the primary key and all related replica keys. For KMS keys in [AWS CloudHSM key stores](https://docs.aws.amazon.com/kms/latest/developerguide/keystore-cloudhsm.html), it includes information about the key store, such as the key store ID and the AWS CloudHSM cluster ID. For KMS keys in [external key stores](https://docs.aws.amazon.com/kms/latest/developerguide/keystore-external.html), it includes the custom key store ID and the ID of the external key.

 `DescribeKey` does not return the following information:
+ Aliases associated with the KMS key. To get this information, use [ListAliases](API_ListAliases.md).
+ Whether automatic key rotation is enabled on the KMS key. To get this information, use [GetKeyRotationStatus](API_GetKeyRotationStatus.md). Also, some key states prevent a KMS key from being automatically rotated. For details, see [How key rotation works](https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html#rotate-keys-how-it-works) in the * AWS Key Management Service Developer Guide*.
+ Tags on the KMS key. To get this information, use [ListResourceTags](API_ListResourceTags.md).
+ Key policies and grants on the KMS key. To get this information, use [GetKeyPolicy](API_GetKeyPolicy.md) and [ListGrants](API_ListGrants.md).

In general, `DescribeKey` is a non-mutating operation. It returns data about KMS keys, but doesn't change them. However, AWS services use `DescribeKey` to create [AWS managed keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-managed-key) from a *predefined AWS alias* with no key ID.

 **Cross-account use**: Yes. To perform this operation with a KMS key in a different AWS account, specify the key ARN or alias ARN in the value of the `KeyId` parameter.

 **Required permissions**: [kms:DescribeKey](https://docs.aws.amazon.com/kms/latest/developerguide/kms-api-permissions-reference.html) (key policy)

 **Related operations:** 
+  [GetKeyPolicy](API_GetKeyPolicy.md) 
+  [GetKeyRotationStatus](API_GetKeyRotationStatus.md) 
+  [ListAliases](API_ListAliases.md) 
+  [ListGrants](API_ListGrants.md) 
+  [ListKeys](API_ListKeys.md) 
+  [ListResourceTags](API_ListResourceTags.md) 
+  [ListRetirableGrants](API_ListRetirableGrants.md) 

 **Eventual consistency**: The AWS KMS API follows an eventual consistency model. For more information, see [AWS KMS eventual consistency](https://docs.aws.amazon.com/kms/latest/developerguide/accessing-kms.html#programming-eventual-consistency).

## Request Syntax
<a name="API_DescribeKey_RequestSyntax"></a>

```
{
   "GrantTokens": [ "{{string}}" ],
   "KeyId": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeKey_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**  
In the following list, the required parameters are described first.

 ** [KeyId](#API_DescribeKey_RequestSyntax) **   <a name="KMS-DescribeKey-request-KeyId"></a>
Describes the specified KMS key.   
If you specify a predefined AWS alias (an AWS alias with no key ID), AWS KMS associates the alias with an [AWS managed key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-managed-key) and returns its `KeyId` and `Arn` in the response.  
To specify a KMS key, use its key ID, key ARN, alias name, or alias ARN. When using an alias name, prefix it with `"alias/"`. To specify a KMS key in a different AWS account, you must use the key ARN or alias ARN.  
For example:  
+ Key ID: `1234abcd-12ab-34cd-56ef-1234567890ab` 
+ Key ARN: `arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab` 
+ Alias name: `alias/ExampleAlias` 
+ Alias ARN: `arn:aws:kms:us-east-2:111122223333:alias/ExampleAlias` 
To get the key ID and key ARN for a KMS key, use [ListKeys](API_ListKeys.md) or [DescribeKey](#API_DescribeKey). To get the alias name and alias ARN, use [ListAliases](API_ListAliases.md).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Required: Yes

 ** [GrantTokens](#API_DescribeKey_RequestSyntax) **   <a name="KMS-DescribeKey-request-GrantTokens"></a>
A list of grant tokens.  
Use a grant token when your permission to call this operation comes from a new grant that has not yet achieved *eventual consistency*. For more information, see [Grant token](https://docs.aws.amazon.com/kms/latest/developerguide/grants.html#grant_token) and [Using a grant token](https://docs.aws.amazon.com/kms/latest/developerguide/using-grant-token.html) in the * AWS Key Management Service Developer Guide*.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 10 items.  
Length Constraints: Minimum length of 1. Maximum length of 8192.  
Required: No

## Response Syntax
<a name="API_DescribeKey_ResponseSyntax"></a>

```
{
   "KeyMetadata": { 
      "Arn": "string",
      "AWSAccountId": "string",
      "CloudHsmClusterId": "string",
      "CreationDate": number,
      "CurrentKeyMaterialId": "string",
      "CustomerMasterKeySpec": "string",
      "CustomKeyStoreId": "string",
      "DeletionDate": number,
      "Description": "string",
      "Enabled": boolean,
      "EncryptionAlgorithms": [ "string" ],
      "ExpirationModel": "string",
      "KeyAgreementAlgorithms": [ "string" ],
      "KeyId": "string",
      "KeyManager": "string",
      "KeySpec": "string",
      "KeyState": "string",
      "KeyUsage": "string",
      "MacAlgorithms": [ "string" ],
      "MultiRegion": boolean,
      "MultiRegionConfiguration": { 
         "MultiRegionKeyType": "string",
         "PrimaryKey": { 
            "Arn": "string",
            "Region": "string"
         },
         "ReplicaKeys": [ 
            { 
               "Arn": "string",
               "Region": "string"
            }
         ]
      },
      "Origin": "string",
      "PendingDeletionWindowInDays": number,
      "SigningAlgorithms": [ "string" ],
      "ValidTo": number,
      "XksKeyConfiguration": { 
         "Id": "string"
      }
   }
}
```

## Response Elements
<a name="API_DescribeKey_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [KeyMetadata](#API_DescribeKey_ResponseSyntax) **   <a name="KMS-DescribeKey-response-KeyMetadata"></a>
Metadata associated with the key.  
Type: [KeyMetadata](API_KeyMetadata.md) object

## Errors
<a name="API_DescribeKey_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DependencyTimeoutException **   
The system timed out while trying to fulfill the request. You can retry the request.  
HTTP Status Code: 500

 ** InvalidArnException **   
The request was rejected because a specified ARN, or an ARN in a key policy, is not valid.  
HTTP Status Code: 400

 ** KMSInternalException **   
The request was rejected because an internal exception occurred. The request can be retried.  
HTTP Status Code: 500

 ** NotFoundException **   
The request was rejected because the specified entity or resource could not be found.  
HTTP Status Code: 400

## Examples
<a name="API_DescribeKey_Examples"></a>

The following examples are formatted for legibility.

### Example Request
<a name="API_DescribeKey_Example_1"></a>

This example illustrates one usage of DescribeKey.

```
POST / HTTP/1.1
Host: kms.us-east-2.amazonaws.com
Content-Length: 49
X-Amz-Target: TrentService.DescribeKey
X-Amz-Date: 20170705T211529Z
Authorization: AWS4-HMAC-SHA256\
 Credential=AKIAI44QH8DHBEXAMPLE/20170705/us-east-2/kms/aws4_request,\
 SignedHeaders=content-type;host;x-amz-date;x-amz-target,\
 Signature=6bcb6a5ef9ee7585d83955e8a5c3f6d47cf581596208fc0e436fa1de26ef3f6a
Content-Type: application/x-amz-json-1.1

{"KeyId": "1234abcd-12ab-34cd-56ef-1234567890ab"}
```

### Example Response
<a name="API_DescribeKey_Example_2"></a>

This example illustrates one usage of DescribeKey.

```
HTTP/1.1 200 OK
Server: Server
Date: Wed, 05 Jul 2017 21:15:30 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 335
Connection: keep-alive
x-amzn-RequestId: 13230ddb-61c7-11e7-af6f-c5b105d7a982

{
  "KeyMetadata": {
    "AWSAccountId": "111122223333",
    "Arn": "arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab",
    "CreationDate": "2025-04-16T16:03:04.060000-07:00",
    "CustomerMasterKeySpec": "SYMMETRIC_DEFAULT",
    "Description": "",
    "Enabled": true,
    "KeyId": "1234abcd-12ab-34cd-56ef-1234567890ab",
    "KeyManager": "CUSTOMER",
    "KeySpec": "SYMMETRIC_DEFAULT",
    "KeyState": "Enabled",
    "KeyUsage": "ENCRYPT_DECRYPT",
    "MultiRegion": false,
    "Origin": "AWS_KMS",
    "EncryptionAlgorithms": [
        "SYMMETRIC_DEFAULT"
    ],
    "CurrentKeyMaterialId": "0b7fd7ddbac6eef27907413567cad8c810e2883dc8a7534067a82ee1142fc1e6"
  }
}
```

## See Also
<a name="API_DescribeKey_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kms-2014-11-01/DescribeKey) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kms-2014-11-01/DescribeKey) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kms-2014-11-01/DescribeKey) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kms-2014-11-01/DescribeKey) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kms-2014-11-01/DescribeKey) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kms-2014-11-01/DescribeKey) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kms-2014-11-01/DescribeKey) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kms-2014-11-01/DescribeKey) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/kms-2014-11-01/DescribeKey) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kms-2014-11-01/DescribeKey)
