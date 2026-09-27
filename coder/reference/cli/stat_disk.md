---
title: stat disk
description: Show disk usage, in gigabytes.
product: Coder
section: reference
source_url: https://coder.com/docs/reference/cli/stat_disk
fetched: '2026-09-26'
tags:
- coder
- reference
---

<!-- DO NOT EDIT | GENERATED CONTENT -->

Show disk usage, in gigabytes.

## Usage

```console
coder stat disk [flags]
```

## Options

### --path

|         |                     |
|---------|---------------------|
| Type    | <code>string</code> |
| Default | <code>/</code>      |

Path for which to check disk usage.

### --prefix

|         |                             |
|---------|-----------------------------|
| Type    | <code>Ki\|Mi\|Gi\|Ti</code> |
| Default | <code>Gi</code>             |

SI Prefix for disk measurement.

### -o, --output

|         |                         |
|---------|-------------------------|
| Type    | <code>text\|json</code> |
| Default | <code>text</code>       |

Output format.
