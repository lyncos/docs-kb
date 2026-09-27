---
title: whoami
description: Fetch authenticated user info for Coder deployment
product: Coder
section: reference
source_url: https://coder.com/docs/reference/cli/whoami
fetched: '2026-09-26'
tags:
- coder
- reference
---

<!-- DO NOT EDIT | GENERATED CONTENT -->

Fetch authenticated user info for Coder deployment

## Usage

```console
coder whoami [flags]
```

## Options

### -c, --column

|         |                                               |
|---------|-----------------------------------------------|
| Type    | <code>[URL\|Username\|ID\|Orgs\|Roles]</code> |
| Default | <code>url,username,id</code>                  |

Columns to display in table output.

### -o, --output

|         |                                |
|---------|--------------------------------|
| Type    | <code>text\|json\|table</code> |
| Default | <code>text</code>              |

Output format.
