---
title: users list
description: Prints the list of users.
product: Coder
section: reference
source_url: https://coder.com/docs/reference/cli/users_list
fetched: '2026-09-26'
tags:
- coder
- reference
---

<!-- DO NOT EDIT | GENERATED CONTENT -->

Prints the list of users.

Aliases:

* ls

## Usage

```console
coder users list [flags]
```

## Options

### --github-user-id

|      |                  |
|------|------------------|
| Type | <code>int</code> |

Filter users by their GitHub user ID.

### -c, --column

|         |                                                                          |
|---------|--------------------------------------------------------------------------|
| Type    | <code>[id\|username\|name\|email\|created at\|updated at\|status]</code> |
| Default | <code>username,email,created at,status</code>                            |

Columns to display in table output.

### -o, --output

|         |                          |
|---------|--------------------------|
| Type    | <code>table\|json</code> |
| Default | <code>table</code>       |

Output format.
