---
title: state push
description: Push a Terraform state file to a workspace.
product: Coder
section: reference
source_url: https://coder.com/docs/reference/cli/state_push
fetched: '2026-09-26'
tags:
- coder
- reference
---

<!-- DO NOT EDIT | GENERATED CONTENT -->

Push a Terraform state file to a workspace.

## Usage

```console
coder state push [flags] <workspace> <file>
```

## Options

### -b, --build

|      |                  |
|------|------------------|
| Type | <code>int</code> |

Specify a workspace build to target by name. Defaults to latest.

### -n, --no-build

|      |                   |
|------|-------------------|
| Type | <code>bool</code> |

Update the state without triggering a workspace build. Useful for state-only migrations.
