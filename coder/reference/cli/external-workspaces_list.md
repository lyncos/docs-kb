---
title: external-workspaces list
description: List external workspaces
product: Coder
section: reference
source_url: https://coder.com/docs/reference/cli/external-workspaces_list
fetched: '2026-09-26'
tags:
- coder
- reference
---

<!-- DO NOT EDIT | GENERATED CONTENT -->

List external workspaces

Aliases:

* ls

## Usage

```console
coder external-workspaces list [flags]
```

## Options

### -a, --all

|      |                   |
|------|-------------------|
| Type | <code>bool</code> |

Specifies whether all workspaces will be listed or not.

### --search

|         |                      |
|---------|----------------------|
| Type    | <code>string</code>  |
| Default | <code>user:me</code> |

Search for a workspace with a query.

### -c, --column

|         |                                                                                                                                                                                                       |
|---------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Type    | <code>[favorite\|workspace\|organization id\|organization name\|template\|status\|healthy\|last built\|current version\|outdated\|starts at\|starts next\|stops after\|stops next\|daily cost]</code> |
| Default | <code>workspace,template,status,healthy,last built,current version,outdated</code>                                                                                                                    |

Columns to display in table output.

### -o, --output

|         |                          |
|---------|--------------------------|
| Type    | <code>table\|json</code> |
| Default | <code>table</code>       |

Output format.
