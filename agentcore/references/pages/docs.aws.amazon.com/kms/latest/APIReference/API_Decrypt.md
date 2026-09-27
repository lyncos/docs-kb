---
title: Decrypt
description: 'Decrypts ciphertext that was encrypted by a KMS key using any of the following operations: + Encrypt + GenerateDataKey + GenerateDataKeyPair + GenerateDataKeyWithoutPlaintext + GenerateDataKeyPairWithoutPlaintext'
product: Amazon Bedrock AgentCore
section: References / docs.aws.amazon.com
source_url: https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt.html
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

# Decrypt
<a name="API_Decrypt"></a>

Decrypts ciphertext that was encrypted by a KMS key using any of the following operations:
+  [Encrypt](API_Encrypt.md) 
+  [GenerateDataKey](API_GenerateDataKey.md) 
+  [GenerateDataKeyPair](API_GenerateDataKeyPair.md) 
+  [GenerateDataKeyWithoutPlaintext](API_GenerateDataKeyWithoutPlaintext.md) 
+  [GenerateDataKeyPairWithoutPlaintext](API_GenerateDataKeyPairWithoutPlaintext.md) 

You can use this operation to decrypt ciphertext that was encrypted under a symmetric encryption KMS key or an asymmetric encryption KMS key. When the KMS key is asymmetric, you must specify the KMS key and the encryption algorithm that was used to encrypt the ciphertext. For information about asymmetric KMS keys, see [Asymmetric KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/symmetric-asymmetric.html) in the * AWS Key Management Service Developer Guide*.

The `Decrypt` operation also decrypts ciphertext that was encrypted outside of AWS KMS by the public key in an AWS KMS asymmetric KMS key. However, it cannot decrypt symmetric ciphertext produced by other libraries, such as the [AWS Encryption SDK](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/) or [Amazon S3 client-side encryption](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingClientSideEncryption.html). These libraries return a ciphertext format that is incompatible with AWS KMS.

If the ciphertext was encrypted under a symmetric encryption KMS key, the `KeyId` parameter is optional. AWS KMS can get this information from metadata that it adds to the symmetric ciphertext blob. This feature adds durability to your implementation by ensuring that authorized users can decrypt ciphertext decades after it was encrypted, even if they've lost track of the key ID. However, specifying the KMS key is always recommended as a best practice. When you use the `KeyId` parameter to specify a KMS key, AWS KMS only uses the KMS key you specify. If the ciphertext was encrypted under a different KMS key, the `Decrypt` operation fails. This practice ensures that you use the KMS key that you intend.

Whenever possible, use key policies to give users permission to call the `Decrypt` operation on a particular KMS key, instead of using IAM policies. Otherwise, you might create an IAM policy that gives the user `Decrypt` permission on all KMS keys. This user could decrypt ciphertext that was encrypted by KMS keys in other accounts if the key policy for the cross-account KMS key permits it. If you must use an IAM policy for `Decrypt` permissions, limit the user to particular KMS keys or particular trusted accounts. For details, see [Best practices for IAM policies](https://docs.aws.amazon.com/kms/latest/developerguide/iam-policies.html#iam-policies-best-practices) in the * AWS Key Management Service Developer Guide*.

 `Decrypt` also supports [AWS Nitro Enclaves](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/nitro-enclave.html) and NitroTPM, which provide attested environments in Amazon EC2. To call `Decrypt` for a Nitro enclave or NitroTPM, use the [AWS Nitro Enclaves SDK](https://docs.aws.amazon.com/enclaves/latest/user/developing-applications.html#sdk) or any AWS SDK. Use the `Recipient` parameter to provide the attestation document for the attested environment. Instead of the plaintext data, the response includes the plaintext data encrypted with the public key from the attestation document (`CiphertextForRecipient`). For information about the interaction between AWS KMS and AWS Nitro Enclaves or AWS NitroTPM, see [Cryptographic attestation support in AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/cryptographic-attestation.html) in the * AWS Key Management Service Developer Guide*.

The KMS key that you use for this operation must be in a compatible key state. For details, see [Key states of AWS KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html) in the * AWS Key Management Service Developer Guide*.

 **Cross-account use**: Yes. To specify a KMS key in a different AWS account, use the [key ARN](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN) or [alias ARN](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-alias-ARN). A short [key ID](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-id) is also acceptable when decrypting symmetric ciphertexts, though using a full key ARN is recommended to be more explicit about the intended KMS key.

 **Required permissions**: [kms:Decrypt](https://docs.aws.amazon.com/kms/latest/developerguide/kms-api-permissions-reference.html) (key policy)

 **Related operations:** 
+  [Encrypt](API_Encrypt.md) 
+  [GenerateDataKey](API_GenerateDataKey.md) 
+  [GenerateDataKeyPair](API_GenerateDataKeyPair.md) 
+  [ReEncrypt](API_ReEncrypt.md) 

 **Eventual consistency**: The AWS KMS API follows an eventual consistency model. For more information, see [AWS KMS eventual consistency](https://docs.aws.amazon.com/kms/latest/developerguide/accessing-kms.html#programming-eventual-consistency).

## Request Syntax
<a name="API_Decrypt_RequestSyntax"></a>

```
{
   "CiphertextBlob": {{blob}},
   "DryRun": {{boolean}},
   "DryRunModifiers": [ "{{string}}" ],
   "EncryptionAlgorithm": "{{string}}",
   "EncryptionContext": { 
      "{{string}}" : "{{string}}" 
   },
   "GrantTokens": [ "{{string}}" ],
   "KeyId": "{{string}}",
   "Recipient": { 
      "AttestationDocument": {{blob}},
      "KeyEncryptionAlgorithm": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_Decrypt_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**  
In the following list, the required parameters are described first.

 ** [CiphertextBlob](#API_Decrypt_RequestSyntax) **   <a name="KMS-Decrypt-request-CiphertextBlob"></a>
Ciphertext to be decrypted. The blob includes metadata.  
This parameter is required in all cases except when `DryRun` is `true` and `DryRunModifiers` is set to `IGNORE_CIPHERTEXT`.  
Type: Base64-encoded binary data object  
Length Constraints: Minimum length of 1. Maximum length of 6144.  
Required: No

 ** [DryRun](#API_Decrypt_RequestSyntax) **   <a name="KMS-Decrypt-request-DryRun"></a>
Checks if your request will succeed. `DryRun` is an optional parameter.   
To learn more about how to use this parameter, see [Testing your permissions](https://docs.aws.amazon.com/kms/latest/developerguide/testing-permissions.html) in the * AWS Key Management Service Developer Guide*.  
Type: Boolean  
Required: No

 ** [DryRunModifiers](#API_Decrypt_RequestSyntax) **   <a name="KMS-Decrypt-request-DryRunModifiers"></a>
Specifies the modifiers to apply to the dry run operation. `DryRunModifiers` is an optional parameter that only applies when `DryRun` is set to `true`.  
When set to `IGNORE_CIPHERTEXT`, AWS KMS performs only authorization validation without ciphertext validation. This allows you to test permissions without requiring a valid ciphertext blob.  
To learn more about how to use this parameter, see [Testing your permissions](https://docs.aws.amazon.com/kms/latest/developerguide/testing-permissions.html) in the * AWS Key Management Service Developer Guide*.  
Type: Array of strings  
Valid Values: `IGNORE_CIPHERTEXT`   
Required: No

 ** [EncryptionAlgorithm](#API_Decrypt_RequestSyntax) **   <a name="KMS-Decrypt-request-EncryptionAlgorithm"></a>
Specifies the encryption algorithm that will be used to decrypt the ciphertext. Specify the same algorithm that was used to encrypt the data. If you specify a different algorithm, the `Decrypt` operation fails.  
This parameter is required only when the ciphertext was encrypted under an asymmetric KMS key. The default value, `SYMMETRIC_DEFAULT`, represents the only supported algorithm that is valid for symmetric encryption KMS keys.  
Type: String  
Valid Values: `SYMMETRIC_DEFAULT | RSAES_OAEP_SHA_1 | RSAES_OAEP_SHA_256 | SM2PKE`   
Required: No

 ** [EncryptionContext](#API_Decrypt_RequestSyntax) **   <a name="KMS-Decrypt-request-EncryptionContext"></a>
Specifies the encryption context to use when decrypting the data. An encryption context is valid only for [cryptographic operations](https://docs.aws.amazon.com/kms/latest/developerguide/kms-cryptography.html#cryptographic-operations) with a symmetric encryption KMS key. The standard asymmetric encryption algorithms and HMAC algorithms that AWS KMS uses do not support an encryption context.  
An *encryption context* is a collection of non-secret key-value pairs that represent additional authenticated data. When you use an encryption context to encrypt data, you must specify the same (an exact case-sensitive match) encryption context to decrypt the data. An encryption context is supported only on operations with symmetric encryption KMS keys. On operations with symmetric encryption KMS keys, an encryption context is optional, but it is strongly recommended.  
For more information, see [Encryption context](https://docs.aws.amazon.com/kms/latest/developerguide/encrypt_context.html) in the * AWS Key Management Service Developer Guide*.  
Type: String to string map  
Required: No

 ** [GrantTokens](#API_Decrypt_RequestSyntax) **   <a name="KMS-Decrypt-request-GrantTokens"></a>
A list of grant tokens.   
Use a grant token when your permission to call this operation comes from a new grant that has not yet achieved *eventual consistency*. For more information, see [Grant token](https://docs.aws.amazon.com/kms/latest/developerguide/grants.html#grant_token) and [Using a grant token](https://docs.aws.amazon.com/kms/latest/developerguide/using-grant-token.html) in the * AWS Key Management Service Developer Guide*.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 10 items.  
Length Constraints: Minimum length of 1. Maximum length of 8192.  
Required: No

 ** [KeyId](#API_Decrypt_RequestSyntax) **   <a name="KMS-Decrypt-request-KeyId"></a>
Specifies the KMS key that AWS KMS uses to decrypt the ciphertext.  
Enter a key ID of the KMS key that was used to encrypt the ciphertext. If you identify a different KMS key, the `Decrypt` operation throws an `IncorrectKeyException`.  
This parameter is required only when the ciphertext was encrypted under an asymmetric KMS key or when `DryRun` is `true` and `DryRunModifiers` is set to `IGNORE_CIPHERTEXT`. If you used a symmetric encryption KMS key, AWS KMS can get the KMS key from metadata that it adds to the symmetric ciphertext blob. However, it is always recommended as a best practice. This practice ensures that you use the KMS key that you intend.  
To specify a KMS key, use its key ID, key ARN, alias name, or alias ARN. When using an alias name, prefix it with `"alias/"`. To specify a KMS key in a different AWS account, you should use the key ARN or alias ARN.  
For example:  
+ Key ID: `1234abcd-12ab-34cd-56ef-1234567890ab` 
+ Key ARN: `arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab` 
+ Alias name: `alias/ExampleAlias` 
+ Alias ARN: `arn:aws:kms:us-east-2:111122223333:alias/ExampleAlias` 
To get the key ID and key ARN for a KMS key, use [ListKeys](API_ListKeys.md) or [DescribeKey](API_DescribeKey.md). To get the alias name and alias ARN, use [ListAliases](API_ListAliases.md).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Required: No

 ** [Recipient](#API_Decrypt_RequestSyntax) **   <a name="KMS-Decrypt-request-Recipient"></a>
A signed [attestation document](https://docs.aws.amazon.com/enclaves/latest/user/nitro-enclave-concepts.html#term-attestdoc) from an AWS Nitro enclave or NitroTPM, and the encryption algorithm to use with the public key in the attestation document. The only valid encryption algorithm is `RSAES_OAEP_SHA_256`.   
This parameter supports the [AWS Nitro Enclaves SDK](https://docs.aws.amazon.com/enclaves/latest/user/developing-applications.html#sdk) or any AWS SDK for AWS Nitro Enclaves. It supports any AWS SDK for AWS NitroTPM.   
When you use this parameter, instead of returning the plaintext data, AWS KMS encrypts the plaintext data with the public key in the attestation document, and returns the resulting ciphertext in the `CiphertextForRecipient` field in the response. This ciphertext can be decrypted only with the private key in the attested environment. The `Plaintext` field in the response is null or empty.  
For information about the interaction between AWS KMS and AWS Nitro Enclaves or AWS NitroTPM, see [Cryptographic attestation support in AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/cryptographic-attestation.html) in the * AWS Key Management Service Developer Guide*.  
Type: [RecipientInfo](API_RecipientInfo.md) object  
Required: No

## Response Syntax
<a name="API_Decrypt_ResponseSyntax"></a>

```
{
   "CiphertextForRecipient": blob,
   "EncryptionAlgorithm": "string",
   "KeyId": "string",
   "KeyMaterialId": "string",
   "Plaintext": blob
}
```

## Response Elements
<a name="API_Decrypt_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CiphertextForRecipient](#API_Decrypt_ResponseSyntax) **   <a name="KMS-Decrypt-response-CiphertextForRecipient"></a>
The plaintext data encrypted with the public key from the attestation document. This ciphertext can be decrypted only by using a private key from the attested environment.   
This field is included in the response only when the `Recipient` parameter in the request includes a valid attestation document from an AWS Nitro enclave or NitroTPM. For information about the interaction between AWS KMS and AWS Nitro Enclaves or AWS NitroTPM, see [Cryptographic attestation support in AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/cryptographic-attestation.html) in the * AWS Key Management Service Developer Guide*.  
Type: Base64-encoded binary data object  
Length Constraints: Minimum length of 1. Maximum length of 6144.

 ** [EncryptionAlgorithm](#API_Decrypt_ResponseSyntax) **   <a name="KMS-Decrypt-response-EncryptionAlgorithm"></a>
The encryption algorithm that was used to decrypt the ciphertext.  
Type: String  
Valid Values: `SYMMETRIC_DEFAULT | RSAES_OAEP_SHA_1 | RSAES_OAEP_SHA_256 | SM2PKE` 

 ** [KeyId](#API_Decrypt_ResponseSyntax) **   <a name="KMS-Decrypt-response-KeyId"></a>
The Amazon Resource Name ([key ARN](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN)) of the KMS key that was used to decrypt the ciphertext.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [KeyMaterialId](#API_Decrypt_ResponseSyntax) **   <a name="KMS-Decrypt-response-KeyMaterialId"></a>
The identifier of the key material used to decrypt the ciphertext. This field is present only when the operation uses a symmetric encryption KMS key. This field is omitted if the request includes the `Recipient` parameter.  
Type: String  
Length Constraints: Fixed length of 64.  
Pattern: `^[a-f0-9]+$` 

 ** [Plaintext](#API_Decrypt_ResponseSyntax) **   <a name="KMS-Decrypt-response-Plaintext"></a>
Decrypted plaintext data. When you use the HTTP API or the AWS CLI, the value is Base64-encoded. Otherwise, it is not Base64-encoded.  
If the response includes the `CiphertextForRecipient` field, the `Plaintext` field is null or empty.  
Type: Base64-encoded binary data object  
Length Constraints: Minimum length of 1. Maximum length of 4096.

## Errors
<a name="API_Decrypt_Errors"></a>

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

 ** IncorrectKeyException **   
The request was rejected because the specified KMS key cannot decrypt the data. The `KeyId` in a [Decrypt](#API_Decrypt) request and the `SourceKeyId` in a [ReEncrypt](API_ReEncrypt.md) request must identify the same KMS key that was used to encrypt the ciphertext.  
HTTP Status Code: 400

 ** InvalidCiphertextException **   
From the [Decrypt](#API_Decrypt) or [ReEncrypt](API_ReEncrypt.md) operation, the request was rejected because the specified ciphertext, or additional authenticated data incorporated into the ciphertext, such as the encryption context, is corrupted, missing, or otherwise invalid.  
From the [ImportKeyMaterial](API_ImportKeyMaterial.md) operation, the request was rejected because AWS KMS could not decrypt the encrypted (wrapped) key material.   
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
<a name="API_Decrypt_Examples"></a>

The following examples are formatted for legibility.

### Example Request
<a name="API_Decrypt_Example_1"></a>

This example illustrates one usage of Decrypt.

```
POST / HTTP/1.1
Host: kms.us-west-2.amazonaws.com
Content-Length: 293
X-Amz-Target: TrentService.Decrypt
X-Amz-Date: 20160517T204035Z
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256\
 Credential=AKIAI44QH8DHBEXAMPLE/20160517/us-west-2/kms/aws4_request,\
 SignedHeaders=content-type;host;x-amz-date;x-amz-target,\
 Signature=545b0c3bfd9223b8ef7e6293ef3ccac37a83d415ee3112d2e5c70727d2a49c46

{
  "KeyId": "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab",  
  "CiphertextBlob": "CiDPoCH188S65r5Cy7pAhIFJMXDlU7mewhSlYUpuQIVBrhKmAQEBAgB4z6Ah9fPEuua+Qsu6QISBSTFw5VO5nsIUpWFKbkCFQa4AAAB9MHsGCSqGSIb3DQEHBqBuMGwCAQAwZwYJKoZIhvcNAQcBMB4GCWCGSAFlAwQBLjARBAxLc9b6QThC9jB/ZjYCARCAOt8la8qXLO5wB3JH2NlwWWzWRU2RKqpO9A/0psE5UWwkK6CnwoeC3Zj9Q0A66apZkbRglFfY1lTY+Tc="
}
```

### Example Response
<a name="API_Decrypt_Example_2"></a>

This example illustrates one usage of Decrypt.

```
HTTP/1.1 200 OK
Server: Server
Date: Tue, 17 May 2016 20:40:40 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 146
Connection: keep-alive
x-amzn-RequestId: 9e02f41f-1c6f-11e6-af63-ab8791945da7

{
  "KeyId": "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab",
  "KeyMaterialId": "0b7fd7ddbac6eef27907413567cad8c810e2883dc8a7534067a82ee1142fc1e6",
  "Plaintext": "VGhpcyBpcyBEYXkgMSBmb3IgdGhlIEludGVybmV0Cg==",
  "EncryptionAlgorithm": "SYMMETRIC_DEFAULT" 
}
```

## See Also
<a name="API_Decrypt_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kms-2014-11-01/Decrypt) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kms-2014-11-01/Decrypt) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kms-2014-11-01/Decrypt) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kms-2014-11-01/Decrypt) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kms-2014-11-01/Decrypt) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kms-2014-11-01/Decrypt) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kms-2014-11-01/Decrypt) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kms-2014-11-01/Decrypt) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/kms-2014-11-01/Decrypt) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kms-2014-11-01/Decrypt)
