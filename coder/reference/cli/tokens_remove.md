---
title: tokens remove
description: Expire or delete a token
product: Coder
section: reference
source_url: https://coder.com/docs/reference/cli/tokens_remove
fetched: '2026-09-26'
tags:
- coder
- reference
---

<!-- DO NOT EDIT | GENERATED CONTENT -->

Expire or delete a token

Aliases:

* delete
* rm

## Usage

```console
coder tokens remove [flags] <name|id|token>
```

## Description

```console
Remove a token by expiring it. Use --delete to permanently hard-delete the token instead.
```

## Options

### --delete

|      |                   |
|------|-------------------|
| Type | <code>bool</code> |

Permanently delete the token instead of expiring it. This removes the audit trail.
