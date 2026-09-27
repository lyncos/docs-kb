---
title: ✨ IP Address Filtering
description: Restrict which IP's can call the proxy endpoints.
product: LiteLLM
section: docs/proxy
source_url: https://docs.litellm.ai/docs/proxy/ip_address
fetched: '2026-09-26'
tags:
- docs-proxy
- litellm
---

# ✨ IP Address Filtering

<EnterpriseFeature />

Restrict which IP's can call the proxy endpoints.

```yaml
general_settings:
  allowed_ips: ["192.168.1.1"]
```

**Expected Response** (if IP not listed)

```bash
{
    "error": {
        "message": "Access forbidden: IP address not allowed.",
        "type": "auth_error",
        "param": "None",
        "code": 403
    }
}
```