---
title: Configure with API operations or an AWS SDK
description: Set your key configuration in a `SetTokenVaultCMK` API request. The following partial example request body sets the token vault to use the provided customer managed key.
product: Amazon Bedrock AgentCore
section: Developer Guide / api
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/api-configuration-encryption.html
fetched: '2026-09-26'
tags:
- agentcore
- api
---

# Configure with API operations or an AWS SDK
<a name="api-configuration-encryption"></a>

Set your key configuration in a `SetTokenVaultCMK` API request. The following partial example request body sets the token vault to use the provided customer managed key.

```
"KmsConfiguration": {
    "KeyType": "CUSTOMER_MANAGED_KEY",
    "KmsKeyArn": "arn:aws:kms:us-east-1:111122223333:key/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222"
}
```

The following partial example request body sets a token vault to use an AWS owned key.

```
"KmsConfiguration": {
    "KeyType": "AWS_OWNED_KEY"
}
```

If your `GetTokenVault` response doesn’t include a `KmsConfiguration` parameter, your token vault is configured to encrypt data at rest with an AWS owned key.