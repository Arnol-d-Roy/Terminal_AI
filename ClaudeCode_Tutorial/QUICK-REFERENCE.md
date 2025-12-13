# Claude Code Quick Reference
## Cheat Sheet for All Levels

```
+--------------------------------------------------+
|           CLAUDE CODE CHEAT SHEET                |
|                                                   |
|  Print this out. Keep it handy.                  |
+--------------------------------------------------+
```

---

## Essential Commands

### Starting Claude Code

```bash
# Start a new conversation
claude

# Resume previous conversation
claude -r

# Quick question (non-interactive)
claude -p "your question here"

# Show help
claude --help

# Show version
claude --version
```

---

## Command-Line Flags

| Flag | Long Form | Description |
|------|-----------|-------------|
| `-r` | `--resume` | Resume previous conversation |
| `-p` | `--print` | Print mode (non-interactive) |
| `-c` | `--continue` | Continue and add to conversation |
| | `--model` | Specify AI model |
| | `--help` | Show help information |
| | `--version` | Show version |
| | `--dangerously-skip-permissions` | Skip permission prompts (use with caution!) |

### Model Selection

```bash
claude --model opus      # Most capable, slower
claude --model sonnet    # Balanced (default)
claude --model haiku     # Fastest, simpler tasks
```

---

## In-Session Slash Commands

| Command | Description |
|---------|-------------|
| `/help` | Show available commands |
| `/exit` | Exit Claude Code |
| `/clear` | Clear conversation history |
| `/undo` | Undo last file change |
| `/diff` | Show file changes |
| `/model` | Switch AI model |
| `/compact` | Compress conversation context |

---

## Common Usage Patterns

### Quick Lookups

```bash
# Syntax reminder
claude -p "Show Python list comprehension syntax"

# Command help
claude -p "How do I revert a git commit?"

# Quick explanation
claude -p "What does the 'yield' keyword do in Python?"
```

### Project Work (Interactive)

```bash
# Start session in project directory
cd /path/to/project
claude

# In session:
> Explain this project structure
> What does the main.py file do?
> Help me fix the bug in utils.py
```

### Resume Previous Work

```bash
# Continue where you left off
claude -r

# Resume with skip permissions (automation)
claude -r --dangerously-skip-permissions
```

---

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

### Prompt Templates

#### Code Review
```
Review [file] for:
- Bugs
- Security issues
- Performance problems
- Style improvements
Focus on [specific area].
```

#### Debugging
```
I'm getting this error: [error]
In file: [filename]
When I: [action]
Expected: [expected behavior]
Actual: [actual behavior]
```

#### Code Generation
```
Create a [language] function that:
- [requirement 1]
- [requirement 2]
Include: error handling, comments, type hints
```

#### Explanation
```
Explain [concept/code] to someone who knows [background].
Include:
- Simple analogy
- Code example
- Common mistakes
```

---

## CLAUDE.md Template

Create this file in your project root:

```markdown
# CLAUDE.md

## Project Overview
[Brief description]

## Tech Stack
- Language: [e.g., Python 3.11]
- Framework: [e.g., FastAPI]
- Database: [e.g., PostgreSQL]

## Project Structure
```
src/
  api/      # API endpoints
  models/   # Data models
  services/ # Business logic
tests/      # Test files
```

## Coding Conventions
- [Convention 1]
- [Convention 2]

## Common Commands
- Run tests: `[command]`
- Start dev: `[command]`
- Build: `[command]`
```

---

## Model Selection Guide

| Task Type | Recommended Model |
|-----------|-------------------|
| Quick syntax questions | Haiku |
| Simple code generation | Haiku |
| General development | Sonnet |
| Code review | Sonnet |
| Debugging | Sonnet |
| Architecture decisions | Opus |
| Complex analysis | Opus |
| Security audit | Opus |

---

## Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Ctrl+C` | Cancel/Exit |
| `Ctrl+D` | Exit |
| `Ctrl+L` | Clear screen |
| Up Arrow | Previous command |

---

## Automation Patterns

### Quick Script Template

```bash
#!/bin/bash
# Use Claude Code in scripts

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
claude -p "List all TODOs in this code: $(cat main.py)" | grep "HIGH"
```

---

## Troubleshooting

### Claude Loses Context
```
Solution: Use /compact or summarize conversation
```

### Responses Too Long
```
Add to prompt: "Keep response under 100 words"
Or: "Answer in bullet points only"
```

### Code Doesn't Work
```
Provide more context:
- Exact error message
- Environment details
- What you've tried
```

### Session Feels Slow
```
- Use /compact to reduce context
- Switch to Haiku for simple tasks
- Start fresh session for new topic
```

---

## XP Quick Reference

### Level Thresholds

| Level | Title | XP Required |
|-------|-------|-------------|
| 1 | Novice | 0 |
| 2 | Apprentice | 100 |
| 3 | Journeyman | 300 |
| 4 | Expert | 600 |
| 5 | Master | 1000 |

### Earning XP

- Read chapter: +5 XP
- Complete exercise: +10-25 XP
- Complete challenge: +20-35 XP
- Boss battle: +50-100 XP
- Achievement: +5-25 XP

---

## Quick Links

| Document | Description |
|----------|-------------|
| [00-START-HERE.md](./00-START-HERE.md) | Tutorial home |
| [01-LEVEL-NOVICE.md](./01-LEVEL-NOVICE.md) | Beginner guide |
| [02-LEVEL-APPRENTICE.md](./02-LEVEL-APPRENTICE.md) | Intermediate guide |
| [03-LEVEL-JOURNEYMAN.md](./03-LEVEL-JOURNEYMAN.md) | Advanced guide |
| [04-LEVEL-EXPERT.md](./04-LEVEL-EXPERT.md) | Expert guide |
| [05-LEVEL-MASTER.md](./05-LEVEL-MASTER.md) | Mastery guide |
| [PROGRESS-TRACKER.md](./PROGRESS-TRACKER.md) | Track your progress |

---

## Emergency Commands

```bash
# Something went wrong?
/undo                    # Revert last change

# Session acting strange?
/clear                   # Reset conversation

# Need to exit fast?
Ctrl+C                   # Cancel and exit

# Want to save context?
> "Summarize what we've discussed"
# Then exit and use claude -r later
```

---

## Pro Tips

1. **Start sessions from project root** - Maximum context awareness

2. **Use CLAUDE.md** - Persistent project context

3. **Resume often** - `claude -r` preserves your work

4. **Match model to task** - Haiku for quick, Opus for complex

5. **Be specific** - Better prompts = better results

6. **Use print mode for scripts** - `claude -p` for automation

7. **Check diffs before confirming** - `/diff` is your friend

8. **Compact long sessions** - `/compact` when things slow down

---

*Keep this reference handy as you master Claude Code!*
