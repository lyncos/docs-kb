---
title: open app
description: Open a workspace application.
product: Coder
section: reference
source_url: https://coder.com/docs/reference/cli/open_app
fetched: '2026-09-26'
tags:
- coder
- reference
---

<!-- DO NOT EDIT | GENERATED CONTENT -->

Open a workspace application.

## Usage

```console
coder open app [flags] <workspace> <app slug>
```

## Options

### --region

|             |                                     |
|-------------|-------------------------------------|
| Type        | <code>string</code>                 |
| Environment | <code>$CODER_OPEN_APP_REGION</code> |
| Default     | <code>primary</code>                |

Region to use when opening the app. By default, the app will be opened using the main Coder deployment (a.k.a. "primary").
