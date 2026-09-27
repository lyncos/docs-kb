---
title: ai-gateway keys list
description: List AI Gateway keys
product: Coder
section: reference
source_url: https://coder.com/docs/reference/cli/ai-gateway_keys_list
fetched: '2026-09-26'
tags:
- coder
- reference
---

<!-- DO NOT EDIT | GENERATED CONTENT -->

List AI Gateway keys

Aliases:

* ls

## Usage

```console
coder ai-gateway keys list [flags]
```

## Options

### -c, --column

|         |                                                                    |
|---------|--------------------------------------------------------------------|
| Type    | <code>[id\|name\|key prefix\|created at\|last heartbeat at]</code> |
| Default | <code>id,name,key prefix,last heartbeat at,created at</code>       |

Columns to display in table output.

### -o, --output

|         |                          |
|---------|--------------------------|
| Type    | <code>table\|json</code> |
| Default | <code>table</code>       |

Output format.
