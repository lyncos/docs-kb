---
title: Development
description: 'The SRE Agent includes comprehensive test coverage to ensure reliability:'
product: Amazon Bedrock AgentCore
section: References / repo / agentcore-samples
source_url: https://github.com/awslabs/agentcore-samples/blob/e1a55b3/02-use-cases/01-conversational-agents/SRE-agent/docs/development.md
fetched: '2026-09-26'
tags:
- agentcore
- agentcore-samples
- reference
---

# Development

## Running Tests

The SRE Agent includes comprehensive test coverage to ensure reliability:

```bash
# Run all tests
pytest

# Run tests with coverage report
pytest --cov=sre_agent --cov-report=html
open htmlcov/index.html  # View coverage report

# Run specific test categories
pytest tests/unit/          # Fast unit tests
pytest tests/integration/   # Integration tests with mocked APIs
pytest tests/e2e/          # End-to-end tests with demo backend

# Run tests in parallel for speed
pytest -n auto

# Run with verbose output for debugging
pytest -vv -s
```

## Code Quality

Maintain code quality using automated tools:

```bash
# Check type hints with mypy
mypy sre_agent/

# Lint code with ruff
ruff check sre_agent/

# Run all quality checks
make quality
```

