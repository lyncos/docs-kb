---
title: provisioner keys list
description: List provisioner keys in an organization
product: Coder
section: reference
source_url: https://coder.com/docs/reference/cli/provisioner_keys_list
fetched: '2026-09-26'
tags:
- coder
- reference
---

<!-- DO NOT EDIT | GENERATED CONTENT -->

List provisioner keys in an organization

Aliases:

* ls

## Usage

```console
coder provisioner keys list [flags]
```

## Options

### -O, --org

|             |                                  |
|-------------|----------------------------------|
| Type        | <code>string</code>              |
| Environment | <code>$CODER_ORGANIZATION</code> |

Select which organization (uuid or name) to use.

### -c, --column

|         |                                       |
|---------|---------------------------------------|
| Type    | <code>[created at\|name\|tags]</code> |
| Default | <code>created at,name,tags</code>     |

Columns to display in table output.

### -o, --output

|         |                          |
|---------|--------------------------|
| Type    | <code>table\|json</code> |
| Default | <code>table</code>       |

Output format.
