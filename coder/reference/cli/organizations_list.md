---
title: organizations list
description: List all organizations
product: Coder
section: reference
source_url: https://coder.com/docs/reference/cli/organizations_list
fetched: '2026-09-26'
tags:
- coder
- reference
---

<!-- DO NOT EDIT | GENERATED CONTENT -->

List all organizations

Aliases:

* ls

## Usage

```console
coder organizations list [flags]
```

## Description

```console
List all organizations. Requires a role which grants ResourceOrganization: read.
```

## Options

### -c, --column

|         |                                                                                                                     |
|---------|---------------------------------------------------------------------------------------------------------------------|
| Type    | <code>[id\|name\|display name\|icon\|description\|created at\|updated at\|default\|default org member roles]</code> |
| Default | <code>name,display name,id,default</code>                                                                           |

Columns to display in table output.

### -o, --output

|         |                          |
|---------|--------------------------|
| Type    | <code>table\|json</code> |
| Default | <code>table</code>       |

Output format.
