---
title: stat mem
description: Show memory usage, in gigabytes.
product: Coder
section: reference
source_url: https://coder.com/docs/reference/cli/stat_mem
fetched: '2026-09-26'
tags:
- coder
- reference
---

<!-- DO NOT EDIT | GENERATED CONTENT -->

Show memory usage, in gigabytes.

## Usage

```console
coder stat mem [flags]
```

## Options

### --host

|      |                   |
|------|-------------------|
| Type | <code>bool</code> |

Force host memory measurement.

### --prefix

|         |                             |
|---------|-----------------------------|
| Type    | <code>Ki\|Mi\|Gi\|Ti</code> |
| Default | <code>Gi</code>             |

SI Prefix for memory measurement.

### -o, --output

|         |                         |
|---------|-------------------------|
| Type    | <code>text\|json</code> |
| Default | <code>text</code>       |

Output format.
