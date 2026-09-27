---
title: licenses list
description: List licenses (including expired)
product: Coder
section: reference
source_url: https://coder.com/docs/reference/cli/licenses_list
fetched: '2026-09-26'
tags:
- coder
- reference
---

<!-- DO NOT EDIT | GENERATED CONTENT -->

List licenses (including expired)

Aliases:

* ls

## Usage

```console
coder licenses list [flags]
```

## Options

### -c, --column

|         |                                                                   |
|---------|-------------------------------------------------------------------|
| Type    | <code>[id\|uuid\|uploaded at\|features\|expires at\|trial]</code> |
| Default | <code>ID,UUID,Expires At,Uploaded At,Features</code>              |

Columns to display in table output.

### -o, --output

|         |                          |
|---------|--------------------------|
| Type    | <code>table\|json</code> |
| Default | <code>table</code>       |

Output format.
