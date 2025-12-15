
```
 ______________________________________________________________________
|                                                                      |
|     _____ _                 _        _____          _                |
|    / ____| |               | |      / ____|        | |               |
|   | |    | | __ _ _   _  __| | ___ | |     ___   __| | ___           |
|   | |    | |/ _` | | | |/ _` |/ _ \| |    / _ \ / _` |/ _ \          |
|   | |____| | (_| | |_| | (_| |  __/| |___| (_) | (_| |  __/          |
|    \_____|_|\__,_|\__,_|\__,_|\___| \_____\___/ \__,_|\___|          |
|                                                                      |
|              M A S T E R Y   Q U E S T                               |
|                                                                      |
|______________________________________________________________________|
```

======================================================================
                     WELCOME, ADVENTURER!
======================================================================

You are about to embark on an epic journey to master Claude Code - a
powerful AI assistant that lives in your terminal. Whether you're
writing code, debugging complex issues, or automating workflows,
Claude Code will become your most trusted companion.

This tutorial system is designed like a video game progression.
You'll start as a NOVICE, earn experience through hands-on practice,
unlock achievements, and eventually reach MASTER status.

----------------------------------------------------------------------


## How This Tutorial Works

### The Level System

```
+-------+-------------+-------------+--------------------------------+
| Level | Title       | XP Required | Description                    |
+-------+-------------+-------------+--------------------------------+
|   1   | Novice      |     0 XP    | Just starting - the basics     |
|   2   | Apprentice  |   100 XP    | Building foundation            |
|   3   | Journeyman  |   300 XP    | Workflow optimization          |
|   4   | Expert      |   600 XP    | Advanced techniques            |
|   5   | Master      |  1000 XP    | Complete mastery               |
+-------+-------------+-------------+--------------------------------+
```

### Earning XP

```
+-------------------------------------------+----------+
| Activity                                  | XP       |
+-------------------------------------------+----------+
| Reading and understanding a section       | +5 XP    |
| Completing a practice exercise            | +10 XP   |
| Completing a challenge                    | +15-25   |
| Defeating a "Boss Battle" scenario        | +50 XP   |
| Discovering an Easter Egg tip             | +5 XP    |
+-------------------------------------------+----------+
```

### Achievement Badges

Throughout your journey, you'll unlock achievement badges. Track
them in your Progress Tracker!

----------------------------------------------------------------------


## Interactive Progress Tracking

**Run the unified tutorial system:**

```bash
python claude-tutorial.py
```

This gives you:

  * Browse and read tutorials by level
  * Toggle task completion with a keystroke
  * Instantly updates PROGRESS-TRACKER.md
  * See your XP in real-time
  * Works everywhere - no extensions needed!

### View Your Stats Anytime

```bash
python xp-calculator.py
```

Shows your complete progress dashboard:

```
+============================================================+
|  CLAUDE CODE MASTERY QUEST - XP CALCULATOR                 |
+============================================================+
|  Current Status:                                           |
|    Level: 2 - Apprentice                                   |
|    Total XP: 145 / 1390                                    |
|    Completion: 10.4%                                       |
|                                                            |
|    Progress: [====------------------------------------]    |
+============================================================+
```

----------------------------------------------------------------------


## Quick Navigation

### For Complete Beginners
> "I've never used Claude Code before"

  Start here --> Level 1: Novice (01-LEVEL-NOVICE.md)


### For Those With Some Experience
> "I know basic commands but want to learn more"

  Jump to --> Level 2: Apprentice (02-LEVEL-APPRENTICE.md)


### For Intermediate Users
> "I use Claude Code regularly but want to be faster"

  Continue at --> Level 3: Journeyman (03-LEVEL-JOURNEYMAN.md)


### For Advanced Users
> "I'm comfortable but want to master advanced features"

  Level up at --> Level 4: Expert (04-LEVEL-EXPERT.md)


### For Power Users
> "I want to know everything and help others"

  Achieve mastery --> Level 5: Master (05-LEVEL-MASTER.md)

----------------------------------------------------------------------


## Tutorial Files Overview

```
ClaudeCode_Tutorial/
|
|-- 00-START-HERE.md          <-- You are here!
|-- 01-LEVEL-NOVICE.md        <-- Level 1: The basics
|-- 02-LEVEL-APPRENTICE.md    <-- Level 2: Essential commands
|-- 03-LEVEL-JOURNEYMAN.md    <-- Level 3: Workflow optimization
|-- 04-LEVEL-EXPERT.md        <-- Level 4: Advanced techniques
|-- 05-LEVEL-MASTER.md        <-- Level 5: Mastery & teaching
|-- PROGRESS-TRACKER.md       <-- Track your XP and achievements
|-- QUICK-REFERENCE.md        <-- Cheat sheet for quick lookup
|-- claude-tutorial.py        <-- Main interactive script
|-- xp-calculator.py          <-- Auto-calculate XP
```

----------------------------------------------------------------------


## Your Starting Stats

```
+============================================================+
|                   ADVENTURER PROFILE                       |
+============================================================+
|                                                            |
|  Name: ____________________                                |
|  Date Started: ____________                                |
|                                                            |
|  Current Level: 1 (Novice)                                 |
|  Total XP: 0 / 1390                                        |
|                                                            |
|  Progress: [----------------------------------------] 0%   |
|                                                            |
|  Achievements Unlocked: 0 / 30                             |
|  Challenges Completed: 0 / 15                              |
|  Boss Battles Won: 0 / 5                                   |
|                                                            |
+============================================================+
```

----------------------------------------------------------------------


## Before You Begin: Prerequisites

### Required

- [ ] A terminal (WSL, macOS Terminal, or Linux)
- [ ] Claude Code installed and configured
- [ ] An Anthropic API key (or Claude Pro subscription)

### Recommended

- [ ] Basic familiarity with command line navigation
- [ ] A code editor installed (VS Code, etc.)
- [ ] A project to practice on

### Reference Setup (WSL Users)

```bash
# Open Ubuntu subsystem
wsl -d ubuntu

# Verify Claude Code is installed
claude --version
```

----------------------------------------------------------------------


## Essential Terms Glossary

Before you begin your journey, here are key terms you'll encounter.
Don't worry if they seem unfamiliar now - you'll learn them gradually!

### Basic Concepts

**Session**
A conversation with Claude Code from start to finish. When you run
`claude`, a new session starts. When you exit, the session ends (but
can be resumed later with `claude -r`).

**Flags**
Command-line options that modify how a program runs. For example,
`claude -r` uses the `-r` flag to resume your last conversation.
Flags usually start with `-` (short form) or `--` (long form).

**Print Mode**
A special way to use Claude Code that displays output directly to your
terminal without starting an interactive chat. Used with the `-p` flag,
like: `claude -p "explain this code" index.js`

**Context/Context Window**
The "memory" Claude Code has about your project. It includes files
you're working on, previous messages in the session, and project
structure. Think of it like Claude's "awareness" of your codebase.

**Tokens**
The units that AI models use to process text. Roughly, 1 token ≈ 4
characters. Important because API usage is measured in tokens. Don't
worry about the details - just know more tokens = higher API cost.

### Intermediate Concepts (Level 2-3)

**Checkpoint**
An automatic save point that Claude Code creates before making changes
to your files. Like a safety net - if something goes wrong, you can
rewind to the checkpoint and undo changes.

**.claudeignore File**
A file that tells Claude Code which files or folders to ignore (not
include in context). Similar to `.gitignore` for Git. Useful for
excluding large folders like `node_modules/` to save on token usage.

**Agents (or Subagents)**
Specialized AI assistants that Claude Code can launch to handle
specific tasks in parallel. Think of them as helpers that can work on
different parts of a complex problem simultaneously while you continue
working. They only read/analyze code, they don't modify files.

### Advanced Concepts (Level 4-5)

**MCP (Model Context Protocol)**
A standardized way for Claude Code to connect with external tools and
services. Like a universal adapter that lets Claude Code access
databases, GitHub, web content, and more. You configure MCP "servers"
to extend Claude Code's capabilities beyond file editing.

**Hooks**
Custom shell commands that automatically run at specific points in
Claude Code's workflow. For example, you could create a hook that
automatically formats code after every file edit, or runs tests before
accepting changes. Hooks let you customize and automate Claude Code's
behavior to match your workflow.

**Plugins**
Pre-packaged bundles that can include slash commands, agents, MCP
servers, and hooks all in one installation. Plugins make it easy to
add complex functionality to Claude Code without manual configuration.

### Quick Reference: When You'll Learn Each Term

```
+------------------+----------------------------------------+
| Level 1 (Novice) | Sessions, basic commands               |
| Level 2 (Appr.)  | Flags, print mode, context, tokens     |
| Level 3 (Journ.) | Checkpoints, .claudeignore, agents     |
| Level 4 (Expert) | MCP, hooks, advanced configuration     |
| Level 5 (Master) | Plugins, integration patterns          |
+------------------+----------------------------------------+
```

**Pro Tip**: Bookmark this section! Come back anytime you encounter
an unfamiliar term in the tutorials.

----------------------------------------------------------------------


## The Hero's Journey Begins

```
                    *
                 *  |  *
               *    |    *
             *      |      *
           *   YOUR QUEST   *
             *    FOR     *
               * MASTERY *
                 *     *
                   * *
                    *
```

Your journey of a thousand commands begins with a single keystroke.

**Ready to begin?**

  --> Start Level 1: Novice (01-LEVEL-NOVICE.md)

----------------------------------------------------------------------


## Quick Start (For the Impatient)

If you just want to start using Claude Code right now:

```bash
# Start a new conversation
claude

# Resume your last conversation
claude -r

# Get help
claude --help
```

But trust us - taking the time to complete this tutorial will make
you 10x more productive. The investment pays off!

----------------------------------------------------------------------


## Resources

  * Reference Video: https://www.youtube.com/watch?v=MsQACpcuTkU
  * Official Documentation: https://docs.anthropic.com
  * Quick Reference: QUICK-REFERENCE.md

----------------------------------------------------------------------


## A Note on Learning

> "The expert in anything was once a beginner."

Don't rush. Take your time with each level. Practice the exercises.
The goal isn't to finish quickly - it's to build genuine mastery
that will serve you for years to come.

Every command you learn, every shortcut you master, is XP in your
real-world developer skills.

**Your adventure awaits!**

======================================================================
  Tutorial Version: 1.0  |  Last Updated: December 2024
  Created for: Claude Code CLI Users
======================================================================
