---
title: Integration Tests
description: Integration tests require no AWS credentials. They run the real CLI binary and assert on local files and stdout only.
product: Amazon Bedrock AgentCore
section: References / repo / agentcore-cli
source_url: https://github.com/aws/agentcore-cli/blob/805f342/docs/testing/integration-tests.md
fetched: '2026-09-26'
tags:
- agentcore
- agentcore-cli
- reference
---

# Integration Tests

Integration tests require no AWS credentials. They run the real CLI binary and assert on local files and stdout only.

## Running

```bash
npm run test:integ    # Run integration tests
```

## Test Organization

Integration tests live in `integ-tests/`:

```
integ-tests/
├── create-no-agent.test.ts
├── create-with-agent.test.ts
├── deploy.test.ts
└── ...
```

See [integ-tests/README.md](../../integ-tests/README.md) for full details.
