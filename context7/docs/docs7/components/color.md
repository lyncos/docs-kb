---
title: Color
description: Show click-to-copy color swatches
product: Context7
section: docs
source_url: https://context7.com/docs/docs7/components/color
fetched: '2026-09-26'
tags:
- context7
- docs
---

# Color

> Show click-to-copy color swatches

Add one `<Color.Item>` for each swatch.

## Usage

```mdx
<Color>
  <Color.Item name="Primary" value="#10B981" />
  <Color.Item
    name="Surface"
    value={{ light: "#FFFFFF", dark: "#18181B" }}
  />
</Color>
```

Use `variant="table"` with `<Color.Row title="...">` to group a larger palette.

## Example

<Color>
  <Color.Item name="Primary" value="#10B981" />
  <Color.Item
    name="Surface"
    value={{ light: "#FFFFFF", dark: "#18181B" }}
  />
</Color>
