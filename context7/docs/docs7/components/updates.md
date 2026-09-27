---
title: Updates
description: Build a changelog from dated entries
product: Context7
section: docs
source_url: https://context7.com/docs/docs7/components/updates
fetched: '2026-09-26'
tags:
- context7
- docs
---

# Updates

> Build a changelog from dated entries

`<Update>` requires a `label`. Use ISO dates when the page also publishes an RSS feed.

## Usage

```mdx
<Update label="2026-08-24" tags={["New"]}>
  Added branch previews.
</Update>
```

`description` adds a short label beside the date. Readers can filter entries by `tags`.

## Example

<Update label="2026-08-24" tags={["New"]}>
  Added branch previews.
</Update>
