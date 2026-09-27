---
title: Accordions
description: Hide details until the reader opens them
product: Context7
section: docs
source_url: https://context7.com/docs/docs7/components/accordions
fetched: '2026-09-26'
tags:
- context7
- docs
---

# Accordions

> Hide details until the reader opens them

Use `<AccordionGroup>` when several accordions belong together.

## Usage

```mdx
<AccordionGroup>
  <Accordion title="Does Docs7 support MDX?">
    Yes.
  </Accordion>
  <Accordion title="Is this open by default?" defaultOpen>
    Yes.
  </Accordion>
</AccordionGroup>
```

`<Accordion>` also accepts `description`, `icon`, and `iconType`.

## Example

<AccordionGroup>
  <Accordion title="Does Docs7 support MDX?">
    Yes.
  </Accordion>
  <Accordion title="Is this open by default?" defaultOpen>
    Yes.
  </Accordion>
</AccordionGroup>
