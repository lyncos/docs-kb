---
title: InitScript
description: '`GET /api/v2/init-script/{os}/{arch}`'
product: Coder
section: reference
source_url: https://coder.com/docs/reference/api/initscript
fetched: '2026-09-26'
tags:
- coder
- reference
---

<!-- DO NOT EDIT | GENERATED CONTENT -->

## Get agent init script

### Code samples

```sh
# Example request using curl
curl -X GET http://coder-server:8080/api/v2/init-script/{os}/{arch}

```

`GET /api/v2/init-script/{os}/{arch}`

### Parameters

| Name   | In   | Type   | Required | Description      |
|--------|------|--------|----------|------------------|
| `os`   | path | string | true     | Operating system |
| `arch` | path | string | true     | Architecture     |

### Responses

| Status | Meaning                                                 | Description | Schema |
|--------|---------------------------------------------------------|-------------|--------|
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Success     |        |
