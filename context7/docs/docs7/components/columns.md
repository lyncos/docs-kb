---
title: Columns
description: Arrange content in a responsive grid
product: Context7
section: docs
source_url: https://context7.com/docs/docs7/components/columns
fetched: '2026-09-26'
tags:
- context7
- docs
---

# Columns

> Arrange content in a responsive grid

Set `cols` from 1 to 4. `<CardGroup>` is the legacy name for `<Columns>`.

## Usage

```mdx
<Columns cols={2}>
  <Column>First column.</Column>
  <Column>Second column.</Column>
</Columns>
```

Cards do not need a `<Column>` wrapper.

## Example

<Columns cols={2}>
  <Column>First column.</Column>
  <Column>Second column.</Column>
</Columns>
