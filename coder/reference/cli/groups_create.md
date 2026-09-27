---
title: groups create
description: Create a user group
product: Coder
section: reference
source_url: https://coder.com/docs/reference/cli/groups_create
fetched: '2026-09-26'
tags:
- coder
- reference
---

<!-- DO NOT EDIT | GENERATED CONTENT -->

Create a user group

## Usage

```console
coder groups create [flags] <name>
```

## Options

### -u, --avatar-url

|             |                                |
|-------------|--------------------------------|
| Type        | <code>string</code>            |
| Environment | <code>$CODER_AVATAR_URL</code> |

Set an avatar for a group.

### --display-name

|             |                                  |
|-------------|----------------------------------|
| Type        | <code>string</code>              |
| Environment | <code>$CODER_DISPLAY_NAME</code> |

Optional human friendly name for the group.

### -O, --org

|             |                                  |
|-------------|----------------------------------|
| Type        | <code>string</code>              |
| Environment | <code>$CODER_ORGANIZATION</code> |

Select which organization (uuid or name) to use.
