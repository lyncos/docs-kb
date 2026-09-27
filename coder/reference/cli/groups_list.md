---
title: groups list
description: List user groups
product: Coder
section: reference
source_url: https://coder.com/docs/reference/cli/groups_list
fetched: '2026-09-26'
tags:
- coder
- reference
---

<!-- DO NOT EDIT | GENERATED CONTENT -->

List user groups

## Usage

```console
coder groups list [flags]
```

## Options

### -c, --column

|         |                                                                         |
|---------|-------------------------------------------------------------------------|
| Type    | <code>[name\|display name\|organization id\|members\|avatar url]</code> |
| Default | <code>name,display name,organization id,members,avatar url</code>       |

Columns to display in table output.

### -o, --output

|         |                          |
|---------|--------------------------|
| Type    | <code>table\|json</code> |
| Default | <code>table</code>       |

Output format.

### -O, --org

|             |                                  |
|-------------|----------------------------------|
| Type        | <code>string</code>              |
| Environment | <code>$CODER_ORGANIZATION</code> |

Select which organization (uuid or name) to use.
