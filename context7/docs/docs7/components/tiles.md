---
title: Tiles
description: Create a link with a large visual preview
product: Context7
section: docs
source_url: https://context7.com/docs/docs7/components/tiles
fetched: '2026-09-26'
tags:
- context7
- docs
---

# Tiles

> Create a link with a large visual preview

`<Tile>` needs an `href`. Its children appear in the preview area.

## Usage

```mdx
<Tile href="/docs7/quickstart" title="Quickstart" description="Preview and publish your docs">
  <Icon icon="book" size={48} />
</Tile>
```

Place tiles inside [Columns](/docs7/components/columns) to create a grid.

## Example

<Tile href="/docs7/quickstart" title="Quickstart" description="Preview and publish your docs">
  <Icon icon="book" size={48} />
</Tile>
