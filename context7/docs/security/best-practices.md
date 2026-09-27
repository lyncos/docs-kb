---
title: Best Practices for Users
description: Recommendations for using Context7 securely across credentials, repository access, and network usage
product: Context7
section: docs
source_url: https://context7.com/docs/security/best-practices
fetched: '2026-09-26'
tags:
- context7
- docs
---

# Best Practices for Users

> Recommendations for using Context7 securely across credentials, repository access, and network usage

These recommendations cover how to use Context7 securely across credentials, repository access, and network usage.

## Secure Your API Keys

- Never commit API keys to version control
- Use environment variables for key storage
- Rotate keys regularly
- Use different keys for different environments
- Revoke unused or compromised keys immediately

## Private Repositories

For private repository access:

- Only grant minimum required permissions
- Use dedicated API keys for private repos
- Regularly audit access permissions
- Consider using GitHub Apps with fine-grained permissions

## Network Security

- Use HTTPS for all API communications (enforced)
- Configure proxy settings securely if behind a firewall
- Monitor API usage for unusual patterns
- Implement request timeouts and retries
