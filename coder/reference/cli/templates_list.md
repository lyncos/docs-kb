---
title: templates list
description: List all the templates available for the organization
product: Coder
section: reference
source_url: https://coder.com/docs/reference/cli/templates_list
fetched: '2026-09-26'
tags:
- coder
- reference
---

<!-- DO NOT EDIT | GENERATED CONTENT -->

List all the templates available for the organization

Aliases:

* ls

## Usage

```console
coder templates list [flags]
```

## Options

### -c, --column

|         |                                                                                                                                         |
|---------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Type    | <code>[name\|created at\|last updated\|organization id\|organization name\|provisioner\|active version id\|used by\|default ttl]</code> |
| Default | <code>name,organization name,last updated,used by</code>                                                                                |

Columns to display in table output.

### -o, --output

|         |                          |
|---------|--------------------------|
| Type    | <code>table\|json</code> |
| Default | <code>table</code>       |

Output format.
