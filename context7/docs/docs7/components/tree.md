---
title: Tree
description: Show a file and folder structure
product: Context7
section: docs
source_url: https://context7.com/docs/docs7/components/tree
fetched: '2026-09-26'
tags:
- context7
- docs
---

# Tree

> Show a file and folder structure

Use nested folder and file components.

## Usage

```mdx
<Tree>
  <Tree.Folder name="src" defaultOpen>
    <Tree.File name="index.ts" highlight />
  </Tree.Folder>
  <Tree.File name="package.json" />
</Tree>
```

Folders accept `defaultOpen`, `openable`, and `highlight`. `<FileTree>` is an alias for `<Tree>`.

## Example

<Tree>
  <Tree.Folder name="src" defaultOpen>
    <Tree.File name="index.ts" highlight />
  </Tree.Folder>
  <Tree.File name="package.json" />
</Tree>
