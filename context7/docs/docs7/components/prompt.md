---
title: Prompt
description: Present a prompt that readers can copy or open in Cursor
product: Context7
section: docs
source_url: https://context7.com/docs/docs7/components/prompt
fetched: '2026-09-26'
tags:
- context7
- docs
---

# Prompt

> Present a prompt that readers can copy or open in Cursor

The default action is `copy`.

## Usage

```mdx
<Prompt description="Copy this prompt" actions={["copy", "cursor"]}>
  Explain this API in one paragraph.
</Prompt>
```

Set `actions={[]}` to hide the actions. `icon` and `iconType` are optional.

## Example

<Prompt description="Copy this prompt" actions={["copy", "cursor"]}>
  Explain this API in one paragraph.
</Prompt>
