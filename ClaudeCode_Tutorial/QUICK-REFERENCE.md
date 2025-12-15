
```
 ______________________________________________________________________
|                                                                      |
|     C L A U D E   C O D E   C H E A T   S H E E T                    |
|                                                                      |
|     Quick Reference Card - Print and Keep Handy!                     |
|                                                                      |
|______________________________________________________________________|
```

======================================================================
                      ESSENTIAL COMMANDS
======================================================================

```
+---------------------------------------------------------------------+
|  STARTING CLAUDE CODE                                               |
+---------------------------------------------------------------------+
|  claude              Start new conversation                         |
|  claude -r           Resume previous conversation                   |
|  claude -p "..."     Quick question (non-interactive)               |
|  claude --help       Show all options                               |
|  claude --version    Show version number                            |
+---------------------------------------------------------------------+
```

----------------------------------------------------------------------


## Command-Line Flags

```
+----------+------------------+---------------------------------------+
| Flag     | Long Form        | Description                           |
+----------+------------------+---------------------------------------+
| -r       | --resume         | Resume previous conversation          |
| -p       | --print          | Print mode (non-interactive)          |
| -c       | --continue       | Continue and add to conversation      |
|          | --model          | Specify AI model                      |
|          | --help           | Show help information                 |
|          | --version        | Show version                          |
|          | --dangerously-   | Skip permission prompts               |
|          |   skip-perms     | (USE WITH CAUTION!)                   |
+----------+------------------+---------------------------------------+
```

----------------------------------------------------------------------


## Model Selection

```
+---------------------------------------------------------------------+
|  MODEL COMMANDS                                                     |
+---------------------------------------------------------------------+
|  claude --model opus       Most capable, slower                     |
|  claude --model sonnet     Balanced (default)                       |
|  claude --model haiku      Fastest, simpler tasks                   |
+---------------------------------------------------------------------+
|                                                                     |
|  IN-SESSION:  /model opus  |  /model sonnet  |  /model haiku       |
|                                                                     |
+---------------------------------------------------------------------+
```

```
+---------------------+---------------------------------------------+
| Task Type           | Recommended Model                           |
+---------------------+---------------------------------------------+
| Quick syntax        | Haiku                                       |
| Simple generation   | Haiku                                       |
| General dev work    | Sonnet                                      |
| Code review         | Sonnet                                      |
| Debugging           | Sonnet                                      |
| Architecture        | Opus                                        |
| Complex analysis    | Opus                                        |
| Security audit      | Opus                                        |
+---------------------+---------------------------------------------+
```

----------------------------------------------------------------------


## In-Session Slash Commands

```
+---------------------------------------------------------------------+
|  SLASH COMMANDS (use while in a Claude Code session)                |
+---------------------------------------------------------------------+
|  /help       Show available commands                                |
|  /exit       Exit Claude Code                                       |
|  /clear      Clear conversation history                             |
|  /undo       Undo last file change                                  |
|  /diff       Show file changes                                      |
|  /model      Switch AI model                                        |
|  /compact    Compress conversation context                          |
|  /init       Initialize Claude Code in current directory            |
|  /cost       Show token usage and estimated cost                    |
|  /settings   View/modify configuration                              |
|  /tasks      List background tasks (agents, shells)                 |
|  /bugs       Report issues to Claude Code team                      |
|  /version    Show Claude Code version info                          |
+---------------------------------------------------------------------+
```

----------------------------------------------------------------------


## Common Usage Patterns

### Quick Lookups (Non-Interactive)

```bash
# Syntax reminder
claude -p "Show Python list comprehension syntax"

# Command help
claude -p "How do I revert a git commit?"

# Quick explanation
claude -p "What does 'yield' do in Python?"
```


### Project Work (Interactive)

```bash
# Start in project directory
cd /path/to/project
claude

# Example prompts:
> Explain this project structure
> What does the main.py file do?
> Help me fix the bug in utils.py
```


### Resume Previous Work

```bash
# Continue where you left off
claude -r

# Resume with skip permissions (for automation)
claude -r --dangerously-skip-permissions
```

----------------------------------------------------------------------


## Effective Prompting

### Good Prompt Structure

```
I need to [task].
Context: [relevant information]
Requirements:
- [requirement 1]
- [requirement 2]
Please [specific output format].
```


### Quick Templates

```
+---------------------------------------------------------------------+
|  CODE REVIEW:                                                       |
|  Review [file] for: bugs, security, performance, style              |
|  Focus on [specific area].                                          |
+---------------------------------------------------------------------+
|  DEBUGGING:                                                         |
|  Error: [error message]                                             |
|  File: [filename]                                                   |
|  Expected: [expected behavior]                                      |
|  Actual: [actual behavior]                                          |
+---------------------------------------------------------------------+
|  CODE GENERATION:                                                   |
|  Create a [language] function that:                                 |
|  - [requirement 1]                                                  |
|  - [requirement 2]                                                  |
|  Include: error handling, comments, type hints                      |
+---------------------------------------------------------------------+
```

----------------------------------------------------------------------


## CLAUDE.md Template

Create this file in your project root for persistent context:

```markdown
# CLAUDE.md

## Project Overview
[Brief description]

## Tech Stack
- Language: [e.g., Python 3.11]
- Framework: [e.g., FastAPI]
- Database: [e.g., PostgreSQL]

## Project Structure
src/
  api/      # API endpoints
  models/   # Data models
  services/ # Business logic
tests/      # Test files

## Coding Conventions
- [Convention 1]
- [Convention 2]

## Common Commands
- Run tests: `[command]`
- Start dev: `[command]`
```

----------------------------------------------------------------------


## Keyboard Shortcuts

```
+---------------------------------------------------------------------+
|  KEYBOARD SHORTCUTS                                                 |
+---------------------------------------------------------------------+
|  Ctrl+C       Cancel/Exit                                           |
|  Ctrl+D       Exit                                                  |
|  Ctrl+L       Clear screen                                          |
|  Up Arrow     Previous command                                      |
+---------------------------------------------------------------------+
```

----------------------------------------------------------------------


## Automation Patterns

### Quick Script Template

```bash
#!/bin/bash
result=$(claude -p "Your prompt here")
echo "$result"
```


### Pipe Input

```bash
# Pipe file content
cat file.py | claude -p "Review this code"

# Pipe command output
git diff | claude -p "Summarize these changes"

# Pipe logs
tail -100 error.log | claude -p "Analyze these errors"
```


### Chain Commands

```bash
# Generate and save
claude -p "Write a README template" > README.md

# Analyze and filter
claude -p "List all TODOs: $(cat main.py)" | grep "HIGH"
```

----------------------------------------------------------------------


## Troubleshooting Quick Fixes

```
+---------------------------------------------------------------------+
|  PROBLEM                    |  SOLUTION                             |
+---------------------------------------------------------------------+
|  Claude loses context       |  Use /compact or summarize            |
|  Responses too long         |  Add: "Under 100 words" to prompt     |
|  Code doesn't work          |  Provide more context/versions        |
|  Session feels slow         |  Use /compact or switch to Haiku      |
|  Unwanted file changes      |  Use /diff before confirming          |
|  Need to undo               |  Use /undo immediately                |
+---------------------------------------------------------------------+
```

----------------------------------------------------------------------


## XP Quick Reference

```
+---------------------------------------------------------------------+
|  LEVEL THRESHOLDS                                                   |
+---------------------------------------------------------------------+
|  Level 1: Novice        0 XP                                        |
|  Level 2: Apprentice    100 XP                                      |
|  Level 3: Journeyman    300 XP                                      |
|  Level 4: Expert        600 XP                                      |
|  Level 5: Master        1000 XP                                     |
+---------------------------------------------------------------------+
|                                                                     |
|  EARNING XP:                                                        |
|  Read chapter: +5      Exercise: +10-25     Challenge: +20-35      |
|  Boss battle: +50-100  Achievement: +5-25                          |
+---------------------------------------------------------------------+
```

----------------------------------------------------------------------


## Emergency Commands

```
+---------------------------------------------------------------------+
|  EMERGENCY REFERENCE                                                |
+---------------------------------------------------------------------+
|  Something went wrong?      /undo                                   |
|  Session acting strange?    /clear                                  |
|  Need to exit fast?         Ctrl+C                                  |
|  Want to save context?      > "Summarize what we discussed"         |
|                             then exit and use claude -r later       |
+---------------------------------------------------------------------+
```

----------------------------------------------------------------------


## Pro Tips

```
+---------------------------------------------------------------------+
|  TOP 8 POWER USER TIPS                                              |
+---------------------------------------------------------------------+
|  1. Start sessions from project root (max context awareness)        |
|  2. Use CLAUDE.md for persistent project context                    |
|  3. Resume often - claude -r preserves your work                    |
|  4. Match model to task (Haiku: quick, Opus: complex)               |
|  5. Be specific - better prompts = better results                   |
|  6. Use print mode for scripts: claude -p for automation            |
|  7. Check diffs before confirming: /diff is your friend             |
|  8. Compact long sessions: /compact when things slow down           |
+---------------------------------------------------------------------+
```

----------------------------------------------------------------------


## Quick Links

```
+---------------------------------------------------------------------+
|  TUTORIAL FILES                                                     |
+---------------------------------------------------------------------+
|  00-START-HERE.md         Tutorial home                             |
|  01-LEVEL-NOVICE.md       Beginner guide                            |
|  02-LEVEL-APPRENTICE.md   Intermediate guide                        |
|  03-LEVEL-JOURNEYMAN.md   Advanced guide                            |
|  04-LEVEL-EXPERT.md       Expert guide                              |
|  05-LEVEL-MASTER.md       Mastery guide                             |
|  PROGRESS-TRACKER.md      Track your progress                       |
+---------------------------------------------------------------------+
```

======================================================================
  Keep this reference handy as you master Claude Code!
======================================================================
