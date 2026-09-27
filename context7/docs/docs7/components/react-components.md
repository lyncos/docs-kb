---
title: React components
description: Define a small custom component in MDX
product: Context7
section: docs
source_url: https://context7.com/docs/docs7/components/react-components
fetched: '2026-09-26'
tags:
- context7
- docs
---

# React components

> Define a small custom component in MDX

Define the component with an ESM export, then use it in the page.

## Usage

```mdx
export const Status = ({ children }) => (
  <Badge color="green">{children}</Badge>
)

The API is <Status>ready</Status>.
```

Keep custom components small. Use a shared MDX or JSX snippet when several pages need the same component.

## Example

export const ExampleStatus = ({ children }) => (
  <Badge color="green">{children}</Badge>
)

The API is <ExampleStatus>ready</ExampleStatus>.
