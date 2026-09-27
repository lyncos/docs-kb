---
title: GenerateDataKey
description: Returns a unique symmetric data key for use outside of AWS KMS. This operation returns a plaintext copy of the data key and a copy that is encrypted under a symmetric encryption KMS key that you specify. The bytes in the plaintext key are random; they are not related to the calle
product: Amazon Bedrock AgentCore
section: References / docs.aws.amazon.com
source_url: https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKey.html
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

# GenerateDataKey
<a name="API_GenerateDataKey"></a>

Returns a unique symmetric data key for use outside of AWS KMS. This operation returns a plaintext copy of the data key and a copy that is encrypted under a symmetric encryption KMS key that you specify. The bytes in the plaintext key are random; they are not related to the caller or the KMS key. You can use the plaintext key to encrypt your data outside of AWS KMS and store the encrypted data key with the encrypted data.

To generate a data key, specify the symmetric encryption KMS key that will be used to encrypt the data key. You cannot use an asymmetric KMS key to encrypt data keys. To get the type of your KMS key, use the [DescribeKey](API_DescribeKey.md) operation.

You must also specify the length of the data key. Use either the `KeySpec` or `NumberOfBytes` parameters (but not both). For 128-bit and 256-bit data keys, use the `KeySpec` parameter.

To generate a 128-bit SM4 data key (China Regions only), specify a `KeySpec` value of `AES_128` or a `NumberOfBytes` value of `16`. The symmetric encryption key used in China Regions to encrypt your data key is an SM4 encryption key.

To get only an encrypted copy of the data key, use [GenerateDataKeyWithoutPlaintext](API_GenerateDataKeyWithoutPlaintext.md). To generate an asymmetric data key pair, use the [GenerateDataKeyPair](API_GenerateDataKeyPair.md) or [GenerateDataKeyPairWithoutPlaintext](API_GenerateDataKeyPairWithoutPlaintext.md) operation. To get a cryptographically secure random byte string, use [GenerateRandom](API_GenerateRandom.md).

You can use an optional encryption context to add additional security to the encryption operation. If you specify an `EncryptionContext`, you must specify the same encryption context (a case-sensitive exact match) when decrypting the encrypted data key. Otherwise, the request to decrypt fails with an `InvalidCiphertextException`. For more information, see [Encryption Context](https://docs.aws.amazon.com/kms/latest/developerguide/encrypt_context.html) in the * AWS Key Management Service Developer Guide*.

 `GenerateDataKey` also supports [AWS Nitro Enclaves](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/nitro-enclave.html), which provide an isolated compute environment in Amazon EC2. To call `GenerateDataKey` for an AWS Nitro enclave or NitroTPM, use the [AWS Nitro Enclaves SDK](https://docs.aws.amazon.com/enclaves/latest/user/developing-applications.html#sdk) or any AWS SDK. Use the `Recipient` parameter to provide the attestation document for the attested environment. `GenerateDataKey` returns a copy of the data key encrypted under the specified KMS key, as usual. But instead of a plaintext copy of the data key, the response includes a copy of the data key encrypted under the public key from the attestation document (`CiphertextForRecipient`). For information about the interaction between AWS KMS and AWS Nitro Enclaves or AWS NitroTPM, see [Cryptographic attestation support in AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/cryptographic-attestation.html) in the * AWS Key Management Service Developer Guide*.

The KMS key that you use for this operation must be in a compatible key state. For details, see [Key states of AWS KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html) in the * AWS Key Management Service Developer Guide*.

 **How to use your data key** 

We recommend that you use the following pattern to encrypt data locally in your application. You can write your own code or use a client-side encryption library, such as the [AWS Encryption SDK](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/), the [Amazon DynamoDB Encryption Client](https://docs.aws.amazon.com/dynamodb-encryption-client/latest/devguide/), or [Amazon S3 client-side encryption](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingClientSideEncryption.html) to do these tasks for you.

To encrypt data outside of AWS KMS:

1. Use the `GenerateDataKey` operation to get a data key.

1. Use the plaintext data key (in the `Plaintext` field of the response) to encrypt your data outside of AWS KMS. Then erase the plaintext data key from memory.

1. Store the encrypted data key (in the `CiphertextBlob` field of the response) with the encrypted data.

To decrypt data outside of AWS KMS:

1. Use the [Decrypt](API_Decrypt.md) operation to decrypt the encrypted data key. The operation returns a plaintext copy of the data key.

1. Use the plaintext data key to decrypt data outside of AWS KMS, then erase the plaintext data key from memory.

 **Cross-account use**: Yes. To perform this operation with a KMS key in a different AWS account, specify the key ARN or alias ARN in the value of the `KeyId` parameter.

 **Required permissions**: [kms:GenerateDataKey](https://docs.aws.amazon.com/kms/latest/developerguide/kms-api-permissions-reference.html) (key policy)

 **Related operations:** 
+  [Decrypt](API_Decrypt.md) 
+  [Encrypt](API_Encrypt.md) 
+  [GenerateDataKeyPair](API_GenerateDataKeyPair.md) 
+  [GenerateDataKeyPairWithoutPlaintext](API_GenerateDataKeyPairWithoutPlaintext.md) 
+  [GenerateDataKeyWithoutPlaintext](API_GenerateDataKeyWithoutPlaintext.md) 

 **Eventual consistency**: The AWS KMS API follows an eventual consistency model. For more information, see [AWS KMS eventual consistency](https://docs.aws.amazon.com/kms/latest/developerguide/accessing-kms.html#programming-eventual-consistency).

## Request Syntax
<a name="API_GenerateDataKey_RequestSyntax"></a>

```
{
   "DryRun": {{boolean}},
   "EncryptionContext": { 
      "{{string}}" : "{{string}}" 
   },
   "GrantTokens": [ "{{string}}" ],
   "KeyId": "{{string}}",
   "KeySpec": "{{string}}",
   "NumberOfBytes": {{number}},
   "Recipient": { 
      "AttestationDocument": {{blob}},
      "KeyEncryptionAlgorithm": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_GenerateDataKey_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**  
In the following list, the required parameters are described first.

 ** [KeyId](#API_GenerateDataKey_RequestSyntax) **   <a name="KMS-GenerateDataKey-request-KeyId"></a>
Specifies the symmetric encryption KMS key that encrypts the data key. You cannot specify an asymmetric KMS key or a KMS key in a custom key store. To get the type and origin of your KMS key, use the [DescribeKey](API_DescribeKey.md) operation.  
To specify a KMS key, use its key ID, key ARN, alias name, or alias ARN. When using an alias name, prefix it with `"alias/"`. To specify a KMS key in a different AWS account, you must use the key ARN or alias ARN.  
For example:  
+ Key ID: `1234abcd-12ab-34cd-56ef-1234567890ab` 
+ Key ARN: `arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab` 
+ Alias name: `alias/ExampleAlias` 
+ Alias ARN: `arn:aws:kms:us-east-2:111122223333:alias/ExampleAlias` 
To get the key ID and key ARN for a KMS key, use [ListKeys](API_ListKeys.md) or [DescribeKey](API_DescribeKey.md). To get the alias name and alias ARN, use [ListAliases](API_ListAliases.md).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Required: Yes

 ** [DryRun](#API_GenerateDataKey_RequestSyntax) **   <a name="KMS-GenerateDataKey-request-DryRun"></a>
Checks if your request will succeed. `DryRun` is an optional parameter.   
To learn more about how to use this parameter, see [Testing your permissions](https://docs.aws.amazon.com/kms/latest/developerguide/testing-permissions.html) in the * AWS Key Management Service Developer Guide*.  
Type: Boolean  
Required: No

 ** [EncryptionContext](#API_GenerateDataKey_RequestSyntax) **   <a name="KMS-GenerateDataKey-request-EncryptionContext"></a>
Specifies the encryption context that will be used when encrypting the data key.  
Do not include confidential or sensitive information in this field. This field may be displayed in plaintext in CloudTrail logs and other output.
An *encryption context* is a collection of non-secret key-value pairs that represent additional authenticated data. When you use an encryption context to encrypt data, you must specify the same (an exact case-sensitive match) encryption context to decrypt the data. An encryption context is supported only on operations with symmetric encryption KMS keys. On operations with symmetric encryption KMS keys, an encryption context is optional, but it is strongly recommended.  
For more information, see [Encryption context](https://docs.aws.amazon.com/kms/latest/developerguide/encrypt_context.html) in the * AWS Key Management Service Developer Guide*.  
Type: String to string map  
Required: No

 ** [GrantTokens](#API_GenerateDataKey_RequestSyntax) **   <a name="KMS-GenerateDataKey-request-GrantTokens"></a>
A list of grant tokens.  
Use a grant token when your permission to call this operation comes from a new grant that has not yet achieved *eventual consistency*. For more information, see [Grant token](https://docs.aws.amazon.com/kms/latest/developerguide/grants.html#grant_token) and [Using a grant token](https://docs.aws.amazon.com/kms/latest/developerguide/using-grant-token.html) in the * AWS Key Management Service Developer Guide*.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 10 items.  
Length Constraints: Minimum length of 1. Maximum length of 8192.  
Required: No

 ** [KeySpec](#API_GenerateDataKey_RequestSyntax) **   <a name="KMS-GenerateDataKey-request-KeySpec"></a>
Specifies the length of the data key. Use `AES_128` to generate a 128-bit symmetric key, or `AES_256` to generate a 256-bit symmetric key.  
You must specify either the `KeySpec` or the `NumberOfBytes` parameter (but not both) in every `GenerateDataKey` request.  
Type: String  
Valid Values: `AES_256 | AES_128`   
Required: No

 ** [NumberOfBytes](#API_GenerateDataKey_RequestSyntax) **   <a name="KMS-GenerateDataKey-request-NumberOfBytes"></a>
Specifies the length of the data key in bytes. For example, use the value 64 to generate a 512-bit data key (64 bytes is 512 bits). For 128-bit (16-byte) and 256-bit (32-byte) data keys, use the `KeySpec` parameter.  
You must specify either the `KeySpec` or the `NumberOfBytes` parameter (but not both) in every `GenerateDataKey` request.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 1024.  
Required: No

 ** [Recipient](#API_GenerateDataKey_RequestSyntax) **   <a name="KMS-GenerateDataKey-request-Recipient"></a>
A signed [attestation document](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/nitro-enclave-how.html#term-attestdoc) from an AWS Nitro enclave or NitroTPM, and the encryption algorithm to use with the public key in the attestation document. The only valid encryption algorithm is `RSAES_OAEP_SHA_256`.   
This parameter supports the [AWS Nitro Enclaves SDK](https://docs.aws.amazon.com/enclaves/latest/user/developing-applications.html#sdk) or any AWS SDK for AWS Nitro Enclaves. It supports any AWS SDK for AWS NitroTPM.   
When you use this parameter, instead of returning the plaintext data key, AWS KMS encrypts the plaintext data key under the public key in the attestation document, and returns the resulting ciphertext in the `CiphertextForRecipient` field in the response. This ciphertext can be decrypted only with the private key in the enclave. The `CiphertextBlob` field in the response contains a copy of the data key encrypted under the KMS key specified by the `KeyId` parameter. The `Plaintext` field in the response is null or empty.  
For information about the interaction between AWS KMS and AWS Nitro Enclaves or AWS NitroTPM, see [Cryptographic attestation support in AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/cryptographic-attestation.html) in the * AWS Key Management Service Developer Guide*.  
Type: [RecipientInfo](API_RecipientInfo.md) object  
Required: No

## Response Syntax
<a name="API_GenerateDataKey_ResponseSyntax"></a>

```
{
   "CiphertextBlob": blob,
   "CiphertextForRecipient": blob,
   "KeyId": "string",
   "KeyMaterialId": "string",
   "Plaintext": blob
}
```

## Response Elements
<a name="API_GenerateDataKey_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CiphertextBlob](#API_GenerateDataKey_ResponseSyntax) **   <a name="KMS-GenerateDataKey-response-CiphertextBlob"></a>
The encrypted copy of the data key. When you use the HTTP API or the AWS CLI, the value is Base64-encoded. Otherwise, it is not Base64-encoded.  
Type: Base64-encoded binary data object  
Length Constraints: Minimum length of 1. Maximum length of 6144.

 ** [CiphertextForRecipient](#API_GenerateDataKey_ResponseSyntax) **   <a name="KMS-GenerateDataKey-response-CiphertextForRecipient"></a>
The plaintext data key encrypted with the public key from the attestation document. This ciphertext can be decrypted only by using a private key from the attested environment.   
This field is included in the response only when the `Recipient` parameter in the request includes a valid attestation document from an AWS Nitro enclave or NitroTPM. For information about the interaction between AWS KMS and AWS Nitro Enclaves or AWS NitroTPM, see [Cryptographic attestation support in AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/cryptographic-attestation.html) in the * AWS Key Management Service Developer Guide*.  
Type: Base64-encoded binary data object  
Length Constraints: Minimum length of 1. Maximum length of 6144.

 ** [KeyId](#API_GenerateDataKey_ResponseSyntax) **   <a name="KMS-GenerateDataKey-response-KeyId"></a>
The Amazon Resource Name ([key ARN](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN)) of the KMS key that encrypted the data key.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [KeyMaterialId](#API_GenerateDataKey_ResponseSyntax) **   <a name="KMS-GenerateDataKey-response-KeyMaterialId"></a>
The identifier of the key material used to encrypt the data key. This field is omitted if the request includes the `Recipient` parameter.  
Type: String  
Length Constraints: Fixed length of 64.  
Pattern: `^[a-f0-9]+$` 

 ** [Plaintext](#API_GenerateDataKey_ResponseSyntax) **   <a name="KMS-GenerateDataKey-response-Plaintext"></a>
The plaintext data key. When you use the HTTP API or the AWS CLI, the value is Base64-encoded. Otherwise, it is not Base64-encoded. Use this data key to encrypt your data outside of KMS. Then, remove it from memory as soon as possible.  
If the response includes the `CiphertextForRecipient` field, the `Plaintext` field is null or empty.  
Type: Base64-encoded binary data object  
Length Constraints: Minimum length of 1. Maximum length of 4096.

## Errors
<a name="API_GenerateDataKey_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DependencyTimeoutException **   
The system timed out while trying to fulfill the request. You can retry the request.  
HTTP Status Code: 500

 ** DisabledException **   
The request was rejected because the specified KMS key is not enabled.  
HTTP Status Code: 400

 ** DryRunOperationException **   
 The request was rejected because the DryRun parameter was specified.   
HTTP Status Code: 400

 ** InvalidGrantTokenException **   
The request was rejected because the specified grant token is not valid.  
HTTP Status Code: 400

 ** InvalidKeyUsageException **   
The request was rejected for one of the following reasons:   
+ The `KeyUsage` value of the KMS key is incompatible with the API operation.
+ The encryption algorithm or signing algorithm specified for the operation is incompatible with the type of key material in the KMS key `(KeySpec`).
For encrypting, decrypting, re-encrypting, and generating data keys, the `KeyUsage` must be `ENCRYPT_DECRYPT`. For signing and verifying messages, the `KeyUsage` must be `SIGN_VERIFY`. For generating and verifying message authentication codes (MACs), the `KeyUsage` must be `GENERATE_VERIFY_MAC`. For deriving key agreement secrets, the `KeyUsage` must be `KEY_AGREEMENT`. To find the `KeyUsage` of a KMS key, use the [DescribeKey](API_DescribeKey.md) operation.  
To find the encryption or signing algorithms supported for a particular KMS key, use the [DescribeKey](API_DescribeKey.md) operation.  
HTTP Status Code: 400

 ** KeyUnavailableException **   
The request was rejected because the specified KMS key was not available. You can retry the request.  
HTTP Status Code: 500

 ** KMSInternalException **   
The request was rejected because an internal exception occurred. The request can be retried.  
HTTP Status Code: 500

 ** KMSInvalidStateException **   
The request was rejected because the state of the specified resource is not valid for this request.  
This exceptions means one of the following:  
+ The key state of the KMS key is not compatible with the operation. 

  To find the key state, use the [DescribeKey](API_DescribeKey.md) operation. For more information about which key states are compatible with each AWS KMS operation, see [Key states of AWS KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html) in the * * AWS Key Management Service Developer Guide* *.
+ For cryptographic operations on KMS keys in custom key stores, this exception represents a general failure with many possible causes. To identify the cause, see the error message that accompanies the exception.
HTTP Status Code: 400

 ** NotFoundException **   
The request was rejected because the specified entity or resource could not be found.  
HTTP Status Code: 400

## Examples
<a name="API_GenerateDataKey_Examples"></a>

The following examples are formatted for legibility.

### Example Request
<a name="API_GenerateDataKey_Example_1"></a>

This example illustrates one usage of GenerateDataKey.

```
POST / HTTP/1.1
Host: kms.us-east-2.amazonaws.com
Content-Length: 50
X-Amz-Target: TrentService.GenerateDataKey
X-Amz-Date: 20161112T000940Z
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256\
 Credential=AKIAI44QH8DHBEXAMPLE/20161112/us-east-2/kms/aws4_request,\
 SignedHeaders=content-type;host;x-amz-date;x-amz-target,\
 Signature=815ac4ccbb5c53b8ca015f979704c7953bb0068bf53f4e0b7c6886ed5b0a8fe4

{
  "KeyId": "alias/ExampleAlias",
  "KeySpec": "AES_256"
}
```

### Example Response
<a name="API_GenerateDataKey_Example_2"></a>

This example illustrates one usage of GenerateDataKey.

```
HTTP/1.1 200 OK
Server: Server
Date: Sat, 12 Nov 2016 00:09:40 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 390
Connection: keep-alive
x-amzn-RequestId: 4e6fc242-a86c-11e6-aff0-8333261e2fbd

{
  "CiphertextBlob": "AQEDAHjRYf5WytIc0C857tFSnBaPn2F8DgfmThbJlGfR8P3WlwAAAH4wfAYJKoZIhvcNAQcGoG8wbQIBADBoBgkqhkiG9w0BBwEwHgYJYIZIAWUDBAEuMBEEDEFogLqPWZconQhwHAIBEIA7d9AC7GeJJM34njQvg4Wf1d5sw0NIo1MrBqZa+YdhV8MrkBQPeac0ReRVNDt9qleAt+SHgIRF8P0H+7U=",
  "KeyId": "arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab",
  "KeyMaterialId": "0b7fd7ddbac6eef27907413567cad8c810e2883dc8a7534067a82ee1142fc1e6",
  "Plaintext": "VdzKNHGzUAzJeRBVY+uUmofUGGiDzyB3+i9fVkh3piw="
}
```

## See Also
<a name="API_GenerateDataKey_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kms-2014-11-01/GenerateDataKey) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kms-2014-11-01/GenerateDataKey) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kms-2014-11-01/GenerateDataKey) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kms-2014-11-01/GenerateDataKey) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kms-2014-11-01/GenerateDataKey) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kms-2014-11-01/GenerateDataKey) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kms-2014-11-01/GenerateDataKey) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kms-2014-11-01/GenerateDataKey) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/kms-2014-11-01/GenerateDataKey) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kms-2014-11-01/GenerateDataKey)
