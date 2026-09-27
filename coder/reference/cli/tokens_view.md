---
title: tokens view
description: Display detailed information about a token
product: Coder
section: reference
source_url: https://coder.com/docs/reference/cli/tokens_view
fetched: '2026-09-26'
tags:
- coder
- reference
---

<!-- DO NOT EDIT | GENERATED CONTENT -->

Display detailed information about a token

## Usage

```console
coder tokens view [flags] <name|id>
```

## Options

### -c, --column

|         |                                                                                       |
|---------|---------------------------------------------------------------------------------------|
| Type    | <code>[id\|name\|scopes\|allow list\|last used\|expires at\|created at\|owner]</code> |
| Default | <code>id,name,scopes,allow list,last used,expires at,created at,owner</code>          |

Columns to display in table output.

### -o, --output

|         |                          |
|---------|--------------------------|
| Type    | <code>table\|json</code> |
| Default | <code>table</code>       |

Output format.
