---
title: AWS Key Management V1
description: '[BETA] AWS Key Management v2 is on the enterprise tier. Go here for docs'
product: LiteLLM
section: docs/secret_managers
source_url: https://docs.litellm.ai/docs/secret_managers/aws_kms
fetched: '2026-09-26'
tags:
- docs-secret-managers
- litellm
---

# AWS Key Management V1

<EnterpriseFeature />

:::tip

[BETA] AWS Key Management v2 is on the enterprise tier. Go [here for docs](../enterprise.md)

:::

Use AWS KMS to storing a hashed copy of your Proxy Master Key in the environment. 

```bash
export LITELLM_MASTER_KEY="djZ9xjVaZ..." # 👈 ENCRYPTED KEY
export AWS_REGION_NAME="us-west-2"
```

```yaml
general_settings:
  key_management_system: "aws_kms"
  key_management_settings:
    hosted_keys: ["LITELLM_MASTER_KEY"] # 👈 WHICH KEYS ARE STORED ON KMS
```

[**See Decryption Code**](https://github.com/BerriAI/litellm/blob/a2da2a8f168d45648b61279d4795d647d94f90c9/litellm/utils.py#L10182)

