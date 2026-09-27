---
title: organizations roles show
description: Show role(s)
product: Coder
section: reference
source_url: https://coder.com/docs/reference/cli/organizations_roles_show
fetched: '2026-09-26'
tags:
- coder
- reference
---

<!-- DO NOT EDIT | GENERATED CONTENT -->

Show role(s)

## Usage

```console
coder organizations roles show [flags] [role_names ...]
```

## Options

### -c, --column

|         |                                                                                                                  |
|---------|------------------------------------------------------------------------------------------------------------------|
| Type    | <code>[name\|display name\|organization id\|site permissions\|organization permissions\|user permissions]</code> |
| Default | <code>name,display name,site permissions,organization permissions,user permissions</code>                        |

Columns to display in table output.

### -o, --output

|         |                          |
|---------|--------------------------|
| Type    | <code>table\|json</code> |
| Default | <code>table</code>       |

Output format.
