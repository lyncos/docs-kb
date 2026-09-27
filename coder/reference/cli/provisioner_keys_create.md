---
title: provisioner keys create
description: Create a new provisioner key
product: Coder
section: reference
source_url: https://coder.com/docs/reference/cli/provisioner_keys_create
fetched: '2026-09-26'
tags:
- coder
- reference
---

<!-- DO NOT EDIT | GENERATED CONTENT -->

Create a new provisioner key

## Usage

```console
coder provisioner keys create [flags] <name>
```

## Options

### -t, --tag

|             |                                       |
|-------------|---------------------------------------|
| Type        | <code>string-array</code>             |
| Environment | <code>$CODER_PROVISIONERD_TAGS</code> |

Tags to filter provisioner jobs by.

### -O, --org

|             |                                  |
|-------------|----------------------------------|
| Type        | <code>string</code>              |
| Environment | <code>$CODER_ORGANIZATION</code> |

Select which organization (uuid or name) to use.
