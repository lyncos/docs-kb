---
title: Expandables
description: Document nested object properties
product: Context7
section: docs
source_url: https://context7.com/docs/docs7/components/expandables
fetched: '2026-09-26'
tags:
- context7
- docs
---

# Expandables

> Document nested object properties

Place `<Expandable>` inside a field.

## Usage

```mdx
<ResponseField name="user" type="object">
  A user record.
  <Expandable title="properties" defaultOpen>
    <ResponseField name="id" type="string" required />
    <ResponseField name="name" type="string" />
  </Expandable>
</ResponseField>
```

The default title is `properties`.

## Example

<ResponseField name="user" type="object">
  A user record.
  <Expandable title="properties" defaultOpen>
    <ResponseField name="id" type="string" required />
    <ResponseField name="name" type="string" />
  </Expandable>
</ResponseField>
