---
title: GetPublicKey
description: Returns the public key of an asymmetric KMS key. Unlike the private key of a asymmetric KMS key, which never leaves AWS KMS unencrypted, callers with `kms:GetPublicKey` permission can download the public key of an asymmetric KMS key. You can share the public key to allow others t
product: Amazon Bedrock AgentCore
section: References / docs.aws.amazon.com
source_url: https://docs.aws.amazon.com/kms/latest/APIReference/API_GetPublicKey.html
fetched: '2026-09-26'
tags:
- agentcore
- docs-aws-amazon-com
- reference
- related
referenced_by:
- private-key-jwt.md
conversion: native-md
---

# GetPublicKey
<a name="API_GetPublicKey"></a>

Returns the public key of an asymmetric KMS key. Unlike the private key of a asymmetric KMS key, which never leaves AWS KMS unencrypted, callers with `kms:GetPublicKey` permission can download the public key of an asymmetric KMS key. You can share the public key to allow others to encrypt messages and verify signatures outside of AWS KMS. For information about asymmetric KMS keys, see [Asymmetric KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/symmetric-asymmetric.html) in the * AWS Key Management Service Developer Guide*.

You do not need to download the public key. Instead, you can use the public key within AWS KMS by calling the [Encrypt](API_Encrypt.md), [ReEncrypt](API_ReEncrypt.md), or [Verify](API_Verify.md) operations with the identifier of an asymmetric KMS key. When you use the public key within AWS KMS, you benefit from the authentication, authorization, and logging that are part of every AWS KMS operation. You also reduce of risk of encrypting data that cannot be decrypted. These features are not effective outside of AWS KMS.

To help you use the public key safely outside of AWS KMS, `GetPublicKey` returns important information about the public key in the response, including:
+  [KeySpec](https://docs.aws.amazon.com/kms/latest/APIReference/API_GetPublicKey.html#KMS-GetPublicKey-response-KeySpec): The type of key material in the public key, such as `RSA_4096` or `ECC_NIST_P521`.
+  [KeyUsage](https://docs.aws.amazon.com/kms/latest/APIReference/API_GetPublicKey.html#KMS-GetPublicKey-response-KeyUsage): Whether the key is used for encryption, signing, or deriving a shared secret.
+  [EncryptionAlgorithms](https://docs.aws.amazon.com/kms/latest/APIReference/API_GetPublicKey.html#KMS-GetPublicKey-response-EncryptionAlgorithms), [KeyAgreementAlgorithms](https://docs.aws.amazon.com/kms/latest/APIReference/API_GetPublicKey.html#KMS-GetPublicKey-response-KeyAgreementAlgorithms), or [SigningAlgorithms](https://docs.aws.amazon.com/kms/latest/APIReference/API_GetPublicKey.html#KMS-GetPublicKey-response-SigningAlgorithms): A list of the encryption algorithms, key agreement algorithms, or signing algorithms for the key.

Although AWS KMS cannot enforce these restrictions on external operations, it is crucial that you use this information to prevent the public key from being used improperly. For example, you can prevent a public signing key from being used encrypt data, or prevent a public key from being used with an encryption algorithm that is not supported by AWS KMS. You can also avoid errors, such as using the wrong signing algorithm in a verification operation.

To verify a signature outside of AWS KMS with an SM2 public key (China Regions only), you must specify the distinguishing ID. By default, AWS KMS uses `1234567812345678` as the distinguishing ID. For more information, see [Offline verification with SM2 key pairs](https://docs.aws.amazon.com/kms/latest/developerguide/offline-operations.html#key-spec-sm-offline-verification).

The KMS key that you use for this operation must be in a compatible key state. For details, see [Key states of AWS KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html) in the * AWS Key Management Service Developer Guide*.

 **Cross-account use**: Yes. To perform this operation with a KMS key in a different AWS account, specify the key ARN or alias ARN in the value of the `KeyId` parameter.

 **Required permissions**: [kms:GetPublicKey](https://docs.aws.amazon.com/kms/latest/developerguide/kms-api-permissions-reference.html) (key policy)

 **Related operations**: [CreateKey](API_CreateKey.md) 

 **Eventual consistency**: The AWS KMS API follows an eventual consistency model. For more information, see [AWS KMS eventual consistency](https://docs.aws.amazon.com/kms/latest/developerguide/accessing-kms.html#programming-eventual-consistency).

## Request Syntax
<a name="API_GetPublicKey_RequestSyntax"></a>

```
{
   "GrantTokens": [ "{{string}}" ],
   "KeyId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetPublicKey_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**  
In the following list, the required parameters are described first.

 ** [KeyId](#API_GetPublicKey_RequestSyntax) **   <a name="KMS-GetPublicKey-request-KeyId"></a>
Identifies the asymmetric KMS key that includes the public key.  
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

 ** [GrantTokens](#API_GetPublicKey_RequestSyntax) **   <a name="KMS-GetPublicKey-request-GrantTokens"></a>
A list of grant tokens.  
Use a grant token when your permission to call this operation comes from a new grant that has not yet achieved *eventual consistency*. For more information, see [Grant token](https://docs.aws.amazon.com/kms/latest/developerguide/grants.html#grant_token) and [Using a grant token](https://docs.aws.amazon.com/kms/latest/developerguide/using-grant-token.html) in the * AWS Key Management Service Developer Guide*.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 10 items.  
Length Constraints: Minimum length of 1. Maximum length of 8192.  
Required: No

## Response Syntax
<a name="API_GetPublicKey_ResponseSyntax"></a>

```
{
   "CustomerMasterKeySpec": "string",
   "EncryptionAlgorithms": [ "string" ],
   "KeyAgreementAlgorithms": [ "string" ],
   "KeyId": "string",
   "KeySpec": "string",
   "KeyUsage": "string",
   "PublicKey": blob,
   "SigningAlgorithms": [ "string" ]
}
```

## Response Elements
<a name="API_GetPublicKey_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CustomerMasterKeySpec](#API_GetPublicKey_ResponseSyntax) **   <a name="KMS-GetPublicKey-response-CustomerMasterKeySpec"></a>
 *This parameter has been deprecated.*   
Instead, use the `KeySpec` field in the `GetPublicKey` response.  
The `KeySpec` and `CustomerMasterKeySpec` fields have the same value. We recommend that you use the `KeySpec` field in your code. However, to avoid breaking changes, AWS KMS supports both fields.  
Type: String  
Valid Values: `RSA_2048 | RSA_3072 | RSA_4096 | ECC_NIST_P256 | ECC_NIST_P384 | ECC_NIST_P521 | ECC_SECG_P256K1 | SYMMETRIC_DEFAULT | HMAC_224 | HMAC_256 | HMAC_384 | HMAC_512 | SM2` 

 ** [EncryptionAlgorithms](#API_GetPublicKey_ResponseSyntax) **   <a name="KMS-GetPublicKey-response-EncryptionAlgorithms"></a>
The encryption algorithms that AWS KMS supports for this key.   
This information is critical. If a public key encrypts data outside of AWS KMS by using an unsupported encryption algorithm, the ciphertext cannot be decrypted.   
This field appears in the response only when the `KeyUsage` of the public key is `ENCRYPT_DECRYPT`.  
Type: Array of strings  
Valid Values: `SYMMETRIC_DEFAULT | RSAES_OAEP_SHA_1 | RSAES_OAEP_SHA_256 | SM2PKE` 

 ** [KeyAgreementAlgorithms](#API_GetPublicKey_ResponseSyntax) **   <a name="KMS-GetPublicKey-response-KeyAgreementAlgorithms"></a>
The key agreement algorithm used to derive a shared secret. This field is present only when the KMS key has a `KeyUsage` value of `KEY_AGREEMENT`.  
Type: Array of strings  
Valid Values: `ECDH` 

 ** [KeyId](#API_GetPublicKey_ResponseSyntax) **   <a name="KMS-GetPublicKey-response-KeyId"></a>
The Amazon Resource Name ([key ARN](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN)) of the asymmetric KMS key from which the public key was downloaded.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [KeySpec](#API_GetPublicKey_ResponseSyntax) **   <a name="KMS-GetPublicKey-response-KeySpec"></a>
The type of the of the public key that was downloaded.  
Type: String  
Valid Values: `RSA_2048 | RSA_3072 | RSA_4096 | ECC_NIST_P256 | ECC_NIST_P384 | ECC_NIST_P521 | ECC_SECG_P256K1 | SYMMETRIC_DEFAULT | HMAC_224 | HMAC_256 | HMAC_384 | HMAC_512 | SM2 | ML_DSA_44 | ML_DSA_65 | ML_DSA_87 | ECC_NIST_EDWARDS25519` 

 ** [KeyUsage](#API_GetPublicKey_ResponseSyntax) **   <a name="KMS-GetPublicKey-response-KeyUsage"></a>
The permitted use of the public key. Valid values for asymmetric key pairs are `ENCRYPT_DECRYPT`, `SIGN_VERIFY`, and `KEY_AGREEMENT`.   
This information is critical. For example, if a public key with `SIGN_VERIFY` key usage encrypts data outside of AWS KMS, the ciphertext cannot be decrypted.   
Type: String  
Valid Values: `SIGN_VERIFY | ENCRYPT_DECRYPT | GENERATE_VERIFY_MAC | KEY_AGREEMENT` 

 ** [PublicKey](#API_GetPublicKey_ResponseSyntax) **   <a name="KMS-GetPublicKey-response-PublicKey"></a>
The exported public key.   
The value is a DER-encoded X.509 public key, also known as `SubjectPublicKeyInfo` (SPKI), as defined in [RFC 5280](https://tools.ietf.org/html/rfc5280). When you use the HTTP API or the AWS CLI, the value is Base64-encoded. Otherwise, it is not Base64-encoded.  
  
Type: Base64-encoded binary data object  
Length Constraints: Minimum length of 1. Maximum length of 8192.

 ** [SigningAlgorithms](#API_GetPublicKey_ResponseSyntax) **   <a name="KMS-GetPublicKey-response-SigningAlgorithms"></a>
The signing algorithms that AWS KMS supports for this key.  
This field appears in the response only when the `KeyUsage` of the public key is `SIGN_VERIFY`.  
Type: Array of strings  
Valid Values: `RSASSA_PSS_SHA_256 | RSASSA_PSS_SHA_384 | RSASSA_PSS_SHA_512 | RSASSA_PKCS1_V1_5_SHA_256 | RSASSA_PKCS1_V1_5_SHA_384 | RSASSA_PKCS1_V1_5_SHA_512 | ECDSA_SHA_256 | ECDSA_SHA_384 | ECDSA_SHA_512 | SM2DSA | ML_DSA_SHAKE_256 | ED25519_SHA_512 | ED25519_PH_SHA_512` 

## Errors
<a name="API_GetPublicKey_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DependencyTimeoutException **   
The system timed out while trying to fulfill the request. You can retry the request.  
HTTP Status Code: 500

 ** DisabledException **   
The request was rejected because the specified KMS key is not enabled.  
HTTP Status Code: 400

 ** InvalidArnException **   
The request was rejected because a specified ARN, or an ARN in a key policy, is not valid.  
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

 ** UnsupportedOperationException **   
The request was rejected because a specified parameter is not supported or a specified resource is not valid for this operation.  
HTTP Status Code: 400

## See Also
<a name="API_GetPublicKey_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kms-2014-11-01/GetPublicKey) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kms-2014-11-01/GetPublicKey) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kms-2014-11-01/GetPublicKey) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kms-2014-11-01/GetPublicKey) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kms-2014-11-01/GetPublicKey) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kms-2014-11-01/GetPublicKey) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kms-2014-11-01/GetPublicKey) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kms-2014-11-01/GetPublicKey) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/kms-2014-11-01/GetPublicKey) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kms-2014-11-01/GetPublicKey)
