---
title: reset-password
description: Directly connect to the database to reset a user's password
product: Coder
section: reference
source_url: https://coder.com/docs/reference/cli/reset-password
fetched: '2026-09-26'
tags:
- coder
- reference
---

<!-- DO NOT EDIT | GENERATED CONTENT -->

Directly connect to the database to reset a user's password

## Usage

```console
coder reset-password [flags] <username>
```

## Options

### --postgres-url

|             |                                       |
|-------------|---------------------------------------|
| Type        | <code>string</code>                   |
| Environment | <code>$CODER_PG_CONNECTION_URL</code> |

URL of a PostgreSQL database to connect to.

### --postgres-connection-auth

|             |                                        |
|-------------|----------------------------------------|
| Type        | <code>password\|awsiamrds</code>       |
| Environment | <code>$CODER_PG_CONNECTION_AUTH</code> |
| Default     | <code>password</code>                  |

Type of auth to use when connecting to postgres.
