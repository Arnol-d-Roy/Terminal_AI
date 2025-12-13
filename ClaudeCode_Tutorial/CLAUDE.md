# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an **interactive, gamified tutorial system** for learning Claude Code from beginner to expert level. The tutorial uses a progressive level system (Novice → Apprentice → Journeyman → Expert → Master) with XP tracking, achievements, and boss battles.

## Repository Structure

```
ClaudeCode_Tutorial/
├── 00-START-HERE.md           # Entry point and navigation
├── 01-LEVEL-NOVICE.md         # Level 1: Basics (0-99 XP)
├── 02-LEVEL-APPRENTICE.md     # Level 2: Essential commands (100-299 XP)
├── 03-LEVEL-JOURNEYMAN.md     # Level 3: Workflow optimization (300-599 XP)
├── 04-LEVEL-EXPERT.md         # Level 4: Advanced techniques (600-999 XP)
├── 05-LEVEL-MASTER.md         # Level 5: Complete mastery (1000+ XP)
├── PROGRESS-TRACKER.md        # Interactive checklist with XP tracking
├── QUICK-REFERENCE.md         # Command cheat sheet
├── HOW-TO-USE-CHECKBOXES.md   # Guide for interactive features
├── xp-calculator.py           # Auto-calculates XP from checked boxes
└── CLAUDE.md                  # This file
```

## Key Commands

### Tutorial Usage
```bash
# Start the tutorial
# Open 00-START-HERE.md in VS Code or your preferred viewer

# Track progress interactively
# Open PROGRESS-TRACKER.md and check boxes as you complete tasks

# Calculate your XP automatically
python3 xp-calculator.py
```

### WSL/Claude Code Setup
From parent directory's `Readme.md`:
- `claude` - runs Claude Code on the terminal
- `claude -r` - resumes a previous conversation
- `claude -r --dangerously-skip-permissions` - resumes without permission checks
- `gemini` - runs Gemini on the terminal
- `gemini -p "<prompt>"` - runs a Gemini prompt without the CLI

Reference video: https://www.youtube.com/watch?v=MsQACpcuTkU&t=147s

## Interactive Features

### Checkbox System
The PROGRESS-TRACKER.md file uses interactive markdown checkboxes:
- Click checkboxes in VS Code preview mode (Ctrl+Shift+V) to toggle completion
- Works in GitHub's rendered view too
- Format: `- [ ]` (unchecked) or `- [x]` (checked)

### XP Calculator
The `xp-calculator.py` script:
- Scans PROGRESS-TRACKER.md for checked boxes
- Calculates total XP earned
- Shows current level and progress percentage
- Displays visual progress bar with colors
- Tracks achievements, boss battles, and Easter eggs
- Provides motivational messages

### Gamification Elements
- **5 Levels**: Progressive difficulty from Novice to Master
- **1,125+ Total XP**: Earned through reading, exercises, and challenges
- **30 Achievement Badges**: Unlockable accomplishments
- **5 Boss Battles**: Complex real-world scenarios
- **6 Easter Eggs**: Hidden tips and tricks to discover

## Tutorial Content

### Topics Covered
- Basic Claude Code commands and usage
- Command-line flags and options
- Print mode and non-interactive usage
- CLAUDE.md configuration files
- Slash commands (/help, /diff, /undo, etc.)
- Model selection (Opus, Sonnet, Haiku)
- Workflow optimization and automation
- Git integration and development workflows
- Advanced prompting techniques
- System administration tasks
- Teaching and mentoring others

### Learning Approach
Each level includes:
1. Multiple chapters with progressive content
2. Hands-on practice exercises (rated Easy/Medium/Hard)
3. Challenge quests for application
4. Boss battle scenarios for mastery demonstration
5. Achievement unlocks for milestones
6. Clear completion criteria

## Development Notes

This repository is part of the Terminal_AI project and serves as the official tutorial for learning Claude Code in a gamified, engaging way. The tutorial is designed to be:
- **Self-paced**: Users progress at their own speed
- **Interactive**: Checkboxes and auto-calculation make progress tangible
- **Motivating**: XP, levels, and achievements encourage completion
- **Comprehensive**: Covers beginner to expert topics
- **Practical**: Focuses on real-world usage and workflows
