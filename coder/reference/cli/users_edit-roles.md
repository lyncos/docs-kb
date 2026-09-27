---
title: users edit-roles
description: Edit a user's roles by username or id
product: Coder
section: reference
source_url: https://coder.com/docs/reference/cli/users_edit-roles
fetched: '2026-09-26'
tags:
- coder
- reference
---

<!-- DO NOT EDIT | GENERATED CONTENT -->

Edit a user's roles by username or id

## Usage

```console
coder users edit-roles [flags] <username|user_id>
```

## Options

### -y, --yes

|      |                   |
|------|-------------------|
| Type | <code>bool</code> |

Bypass confirmation prompts.

### --roles

|      |                           |
|------|---------------------------|
| Type | <code>string-array</code> |

A list of roles to give to the user. This removes any existing roles the user may have.
