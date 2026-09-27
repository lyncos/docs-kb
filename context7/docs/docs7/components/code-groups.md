---
title: Code groups
description: Show code examples in tabs
product: Context7
section: docs
source_url: https://context7.com/docs/docs7/components/code-groups
fetched: '2026-09-26'
tags:
- context7
- docs
---

# Code groups

> Show code examples in tabs

Place titled code fences inside `<CodeGroup>`. Use `<CodeBlock>` when code comes from an MDX component.

## Usage

````mdx
<CodeGroup>
```js JavaScript
console.log("hello")
```

```py Python
print("hello")
```
</CodeGroup>

<CodeBlock language="ts" filename="index.ts" lines>
  {"const ready = true"}
</CodeBlock>
````

`<CodeBlock>` also accepts `icon`, `highlight`, `focus`, `wrap`, and `expandable`.

## Example

<CodeGroup>
```js JavaScript
console.log("hello")
```

```py Python
print("hello")
```
</CodeGroup>

<CodeBlock language="ts" filename="index.ts" lines>
  {"const ready = true"}
</CodeBlock>
