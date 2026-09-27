---
title: server dbcrypt delete
description: Delete all encrypted data from the database. THIS IS A DESTRUCTIVE OPERATION.
product: Coder
section: reference
source_url: https://coder.com/docs/reference/cli/server_dbcrypt_delete
fetched: '2026-09-26'
tags:
- coder
- reference
---

<!-- DO NOT EDIT | GENERATED CONTENT -->

Delete all encrypted data from the database. THIS IS A DESTRUCTIVE OPERATION.

Aliases:

* rm

## Usage

```console
coder server dbcrypt delete [flags]
```

## Options

### --postgres-url

|             |                                                            |
|-------------|------------------------------------------------------------|
| Type        | <code>string</code>                                        |
| Environment | <code>$CODER_EXTERNAL_TOKEN_ENCRYPTION_POSTGRES_URL</code> |

The connection URL for the Postgres database.

### --postgres-connection-auth

|             |                                        |
|-------------|----------------------------------------|
| Type        | <code>password\|awsiamrds</code>       |
| Environment | <code>$CODER_PG_CONNECTION_AUTH</code> |
| Default     | <code>password</code>                  |

Type of auth to use when connecting to postgres.

### -y, --yes

|      |                   |
|------|-------------------|
| Type | <code>bool</code> |

Bypass confirmation prompts.
