---
title: Persistent Notes Skill
description: A skill that saves notes to a local `/mnt/workspace/notes.json` file.
product: Amazon Bedrock AgentCore
section: References / repo / agentcore-samples
source_url: https://github.com/awslabs/agentcore-samples/blob/e1a55b3/06-workshops/01-AgentCore-runtime/10-managed-session-storage/persistent-notes/README.md
fetched: '2026-09-26'
tags:
- agentcore
- agentcore-samples
- reference
---

# Persistent Notes Skill

A skill that saves notes to a local `/mnt/workspace/notes.json` file.

## Usage

```bash
python3 persistent-notes/scripts/note_manager.py "Your note here"
```

## What it does

- Saves notes to `/mnt/workspace/notes.json` in the current directory
- Appends new notes to existing ones
- Each note has content and timestamp
- Returns JSON confirmation

## Example

```bash
python3 persistent-notes/scripts/note_manager.py "Remember to deploy on Friday"
```

## File Structure

```
persistent-notes/
├── SKILL.md              # Skill documentation
├── README.md             # This file
└── scripts/
    └── note_manager.py   # Note saving script
```

## Notes Format

Notes are stored as JSON array in `notes.json`:

```json
[
  {
    "content": "Your note content",
    "timestamp": "2026-03-19T10:30:00.123456"
  }
]
```

That's it! Simple note saving with persistence.
