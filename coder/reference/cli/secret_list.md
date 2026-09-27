---
title: secret list
description: List secrets, or show one by name
product: Coder
section: reference
source_url: https://coder.com/docs/reference/cli/secret_list
fetched: '2026-09-26'
tags:
- coder
- reference
---

<!-- DO NOT EDIT | GENERATED CONTENT -->

List secrets, or show one by name

Aliases:

* ls

## Usage

```console
coder secret list [flags] [name]
```

## Description

```console
Secret values are omitted from the output.
```

## Options

### -c, --column

|         |                                                                        |
|---------|------------------------------------------------------------------------|
| Type    | <code>[created\|name\|updated\|env\|file\|enabled\|description]</code> |
| Default | <code>name,created,updated,env,file,enabled,description</code>         |

Columns to display in table output.

### -o, --output

|         |                          |
|---------|--------------------------|
| Type    | <code>table\|json</code> |
| Default | <code>table</code>       |

Output format.
