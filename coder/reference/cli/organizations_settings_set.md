---
title: organizations settings set
description: Update specified organization setting.
product: Coder
section: reference
source_url: https://coder.com/docs/reference/cli/organizations_settings_set
fetched: '2026-09-26'
tags:
- coder
- reference
---

<!-- DO NOT EDIT | GENERATED CONTENT -->

Update specified organization setting.

## Usage

```console
coder organizations settings set
```

## Description

```console
  - Update group sync settings.:

     $ coder organization settings set groupsync < input.json
```

## Subcommands

| Name                                                                                | Purpose                                                                  |
|-------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| [<code>group-sync</code>](./organizations_settings_set_group-sync.md)               | Group sync settings to sync groups from an IdP.                          |
| [<code>role-sync</code>](./organizations_settings_set_role-sync.md)                 | Role sync settings to sync organization roles from an IdP.               |
| [<code>organization-sync</code>](./organizations_settings_set_organization-sync.md) | Organization sync settings to sync organization memberships from an IdP. |
| [<code>workspace-sharing</code>](./organizations_settings_set_workspace-sharing.md) | Workspace sharing settings for the organization.                         |
