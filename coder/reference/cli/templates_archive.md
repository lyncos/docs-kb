---
title: templates archive
description: Archive unused or failed template versions from a given template(s)
product: Coder
section: reference
source_url: https://coder.com/docs/reference/cli/templates_archive
fetched: '2026-09-26'
tags:
- coder
- reference
---

<!-- DO NOT EDIT | GENERATED CONTENT -->

Archive unused or failed template versions from a given template(s)

## Usage

```console
coder templates archive [flags] [template-name...] 
```

## Options

### -y, --yes

|      |                   |
|------|-------------------|
| Type | <code>bool</code> |

Bypass confirmation prompts.

### --all

|      |                   |
|------|-------------------|
| Type | <code>bool</code> |

Include all unused template versions. By default, only failed template versions are archived.

### -O, --org

|             |                                  |
|-------------|----------------------------------|
| Type        | <code>string</code>              |
| Environment | <code>$CODER_ORGANIZATION</code> |

Select which organization (uuid or name) to use.
