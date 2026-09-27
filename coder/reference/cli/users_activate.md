---
title: users activate
description: Update a user's status to 'active'. Active users can fully interact with the platform
product: Coder
section: reference
source_url: https://coder.com/docs/reference/cli/users_activate
fetched: '2026-09-26'
tags:
- coder
- reference
---

<!-- DO NOT EDIT | GENERATED CONTENT -->

Update a user's status to 'active'. Active users can fully interact with the platform

Aliases:

* active

## Usage

```console
coder users activate [flags] <username|user_id>
```

## Description

```console
 coder users activate example_user
```

## Options

### -c, --column

|         |                                                    |
|---------|----------------------------------------------------|
| Type    | <code>[username\|email\|created at\|status]</code> |
| Default | <code>username,email,created at,status</code>      |

Specify a column to filter in the table.
