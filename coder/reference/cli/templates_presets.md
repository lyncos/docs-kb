---
title: templates presets
description: Manage presets of the specified template
product: Coder
section: reference
source_url: https://coder.com/docs/reference/cli/templates_presets
fetched: '2026-09-26'
tags:
- coder
- reference
---

<!-- DO NOT EDIT | GENERATED CONTENT -->

Manage presets of the specified template

Aliases:

* preset

## Usage

```console
coder templates presets
```

## Description

```console
  - List presets for the active version of a template:

     $ coder templates presets list my-template

  - List presets for a specific version of a template:

     $ coder templates presets list my-template --template-version my-template-version
```

## Subcommands

| Name                                             | Purpose                                                                              |
|--------------------------------------------------|--------------------------------------------------------------------------------------|
| [<code>list</code>](./templates_presets_list.md) | List all presets of the specified template. Defaults to the active template version. |
