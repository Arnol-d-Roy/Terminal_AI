
```
 ______________________________________________________________________
|                                                                      |
|   L E V E L   3 :   J O U R N E Y M A N                             |
|                                                                      |
|   Optimizing Your Workflow                                           |
|                                                                      |
|   XP Range: 300-599  |  Status: ADVANCING                           |
|                                                                      |
|______________________________________________________________________|
```

======================================================================
                        LEVEL OBJECTIVES
======================================================================

By the end of this level, you will:

- [ ] Master workflow optimization techniques
- [ ] Configure Claude Code for your preferences
- [ ] Create and use custom commands
- [ ] Integrate Claude Code with your development workflow
- [ ] Handle complex, multi-step tasks efficiently

```
+--------------------------------+
|  Prerequisites: Level 1-2      |
|  (300+ XP)                     |
|  Estimated Time: 2-3 hours     |
|  XP Available: 220 XP          |
+--------------------------------+
```

----------------------------------------------------------------------


## Chapter 1: Workflow Analysis

### Understanding Your Workflow

Before optimizing, let's analyze how you work:

```
Typical Development Workflow

+-------------------+
|  1. Read/Explore  |  <-- Understanding existing code
+-------------------+
         |
         v
+-------------------+
|  2. Plan/Design   |  <-- Deciding what to build
+-------------------+
         |
         v
+-------------------+
|  3. Implement     |  <-- Writing code
+-------------------+
         |
         v
+-------------------+
|  4. Test/Debug    |  <-- Finding and fixing issues
+-------------------+
         |
         v
+-------------------+
|  5. Document      |  <-- Explaining what you built
+-------------------+
         |
         v
+-------------------+
|  6. Review/Ship   |  <-- Final checks and deployment
+-------------------+
```

Claude Code can accelerate **every single phase**.


### Where Time Goes

Most developers lose time on:

  1. **Context switching** between tools
  2. **Searching** for syntax and examples
  3. **Debugging** without direction
  4. **Writing boilerplate** code
  5. **Documenting** after the fact

Claude Code addresses all of these.

```
+----------------------------------------------------+
|  >>> ACHIEVEMENT UNLOCKED: Workflow Analyst        |
|      (+5 XP)                                       |
+----------------------------------------------------+
```

----------------------------------------------------------------------


## Chapter 2: Session Management

### Long-Running Sessions

For complex projects, you'll want sessions that persist across days
or weeks.


### The Session Lifecycle

```
Day 1: claude
  - Explain project context
  - Start working on Feature X
  - [Exit]

Day 2: claude -r
  - Claude remembers Feature X context
  - Continue implementation
  - [Exit]

Day 3: claude -r
  - Complete Feature X
  - Start Feature Y
  - [Exit]
```


### Managing Multiple Projects

**Problem**: You work on multiple projects. How do you maintain
separate contexts?

**Solution**: Use directory-aware sessions

```bash
# Project A
cd ~/projects/project-a
claude
# This session is tied to project-a

# Project B (different terminal or after exiting)
cd ~/projects/project-b
claude
# This session is tied to project-b

# Resume Project A
cd ~/projects/project-a
claude -r
# Resumes project-a context
```


### Session Best Practices

```
+---------------------------------------------------------------+
|  SESSION BEST PRACTICES                                       |
+---------------------------------------------------------------+
|  1. Start sessions from project root (max context)            |
|  2. Summarize before exiting (ask Claude to note decisions)   |
|  3. Use clear project descriptions early                      |
|  4. Keep sessions focused (one major task per session)        |
+---------------------------------------------------------------+
```

----------------------------------------------------------------------


### Practice Exercise 3.1: Session Strategy

```
+===========================================+
|  EXERCISE 3.1                             |
|-------------------------------------------|
|  Difficulty: Medium                       |
|  XP Reward: +15 XP                        |
+===========================================+
```

**Task**: Practice managing a multi-session workflow:

  1. Start a session in a project directory
  2. Ask Claude to summarize the project
  3. Begin discussing a feature or improvement
  4. Ask Claude: "Summarize what we've discussed for when I return"
  5. Exit the session
  6. Resume with `claude -r`
  7. Ask Claude what you were working on

**Success Criteria**: Claude accurately recalled the context from
the previous session.

- [ ] Completed

----------------------------------------------------------------------


## Chapter 3: The CLAUDE.md File

### Project-Specific Configuration

The `CLAUDE.md` file is a powerful way to give Claude persistent
context about your project.


### What is CLAUDE.md?

It's a markdown file in your project root that Claude reads
automatically when starting a session.


### Creating Your CLAUDE.md

```bash
# In your project root
touch CLAUDE.md
```


### CLAUDE.md Template

```markdown
# CLAUDE.md

This file provides guidance to Claude Code when working with
this project.

## Project Overview

[Brief description of what this project does]

## Tech Stack

- Language: [e.g., Python 3.11]
- Framework: [e.g., FastAPI]
- Database: [e.g., PostgreSQL]
- Testing: [e.g., pytest]

## Project Structure

src/
  - api/        # API endpoints
  - models/     # Data models
  - services/   # Business logic
  - utils/      # Helper functions
tests/          # Test files

## Coding Conventions

- Follow PEP 8 style guide
- Use type hints for all functions
- Write docstrings for public methods
- Keep functions under 50 lines

## Important Notes

- [Any quirks or important context]
- [Security considerations]
- [Performance concerns]

## Common Tasks

- Run tests: `pytest tests/`
- Start dev server: `python -m uvicorn src.main:app --reload`
- Build: `./scripts/build.sh`
```


### Why CLAUDE.md Matters

```
Without CLAUDE.md:
+-----------------------------------------------+
| > How do I run the tests?                     |
| Claude: I'd need to look at your project...   |
+-----------------------------------------------+

With CLAUDE.md:
+-----------------------------------------------+
| > How do I run the tests?                     |
| Claude: Based on your CLAUDE.md, run          |
|         `pytest tests/`                       |
+-----------------------------------------------+
```

```
+----------------------------------------------------+
|  >>> ACHIEVEMENT UNLOCKED: Configuration Master    |
|      (+5 XP)                                       |
+----------------------------------------------------+
```

----------------------------------------------------------------------


### Practice Exercise 3.2: Create Your CLAUDE.md

```
+===========================================+
|  EXERCISE 3.2                             |
|-------------------------------------------|
|  Difficulty: Medium                       |
|  XP Reward: +15 XP                        |
+===========================================+
```

**Task**: Create a CLAUDE.md file for one of your projects:

  1. Navigate to a project
  2. Create a CLAUDE.md file
  3. Include:
     - Project overview
     - Tech stack
     - At least 3 coding conventions
     - At least 2 common commands
  4. Start a Claude Code session
  5. Ask a question that CLAUDE.md should answer

**Success Criteria**: Claude referenced information from your
CLAUDE.md file.

- [ ] Completed

----------------------------------------------------------------------


## Chapter 4: Slash Commands

### Built-in Commands

While in a Claude Code session, you have access to powerful slash
commands.


### Essential Slash Commands

```
+----------+--------------------------------------------+
| Command  | Description                                |
+----------+--------------------------------------------+
| /help    | Show available commands                    |
| /clear   | Clear conversation history                 |
| /exit    | Exit the session                           |
| /undo    | Undo the last change                       |
| /diff    | Show file changes                          |
| /model   | Switch AI models                           |
| /compact | Condense conversation context              |
+----------+--------------------------------------------+
```


### Using /undo

Made a change you don't like? Undo it:

```
> /undo
```

This reverts the last file modification Claude made.


### Using /diff

See what changed:

```
> /diff
```

Shows a diff of files Claude has modified in this session.


### Using /compact

For long sessions, conversation context can get large. Compact it:

```
> /compact
```

This summarizes the conversation to free up context space.

----------------------------------------------------------------------


### Practice Exercise 3.3: Slash Command Mastery

```
+===========================================+
|  EXERCISE 3.3                             |
|-------------------------------------------|
|  Difficulty: Easy                         |
|  XP Reward: +10 XP                        |
+===========================================+
```

**Task**: Use these slash commands in a session:

  1. Start Claude Code
  2. Use `/help` to see all commands
  3. Ask Claude to make a small file change
  4. Use `/diff` to see the change
  5. Use `/undo` to revert it
  6. Use `/clear` to reset conversation

**Success Criteria**: Successfully used at least 4 different slash
commands.

- [ ] Completed

----------------------------------------------------------------------


## Chapter 5: Multi-Step Task Management

### Breaking Down Complex Tasks

The key to handling complex tasks is decomposition.


### The Task Decomposition Pattern

```
Complex Task: "Build a user authentication system"

Step 1: Define requirements
  > "What authentication method should we use? List the options."

Step 2: Plan the implementation
  > "Create a plan for implementing JWT authentication."

Step 3: Implement incrementally
  > "Let's start with Step 1: Create the User model."
  > "Now implement Step 2: Create the login endpoint."

Step 4: Test each piece
  > "Write tests for the login endpoint."

Step 5: Integrate
  > "Now let's connect the pieces together."
```


### Prompts for Multi-Step Tasks

#### Planning Prompt

```
I need to [describe task].
Please break this down into numbered steps.
For each step, estimate the complexity (low/medium/high).
```


#### Implementation Prompt

```
Let's work on step [N]: [description]
First, explain what we'll do.
Then, implement it.
Finally, verify it works.
```


#### Review Prompt

```
We've completed steps 1-[N].
Summarize what we've built.
What are the next steps?
Any issues we should address?
```

```
+----------------------------------------------------+
|  >>> ACHIEVEMENT UNLOCKED: Task Commander (+5 XP)  |
+----------------------------------------------------+
```

----------------------------------------------------------------------


### Practice Exercise 3.4: Multi-Step Project

```
+===========================================+
|  EXERCISE 3.4                             |
|-------------------------------------------|
|  Difficulty: Hard                         |
|  XP Reward: +25 XP                        |
+===========================================+
```

**Task**: Complete a multi-step task with Claude:

  1. Choose a small project (e.g., "Create a command-line todo app")
  2. Ask Claude to break it into 5+ steps
  3. Implement at least 3 steps with Claude's help
  4. Use the review prompt to assess progress

**Success Criteria**: Completed at least 3 steps of a multi-step
project.

- [ ] Completed

----------------------------------------------------------------------


## Chapter 6: Integration with Development Tools

### Git Integration

Claude Code works beautifully with Git:

```
> Show me the changes since yesterday
> Write a commit message for these changes
> Explain what this pull request does
> Review the diff for potential issues
```


### Git Workflow Examples

#### Pre-Commit Review

```
> Show me all modified files
> Review each change for bugs
> Suggest better variable names
```


#### Commit Message Generation

```
> Generate a conventional commit message for these changes
> Make it follow the pattern: type(scope): description
```


#### Code Review Assistance

```
> I'm reviewing PR #42. Summarize the changes.
> What are the risks of these changes?
> Suggest improvements.
```


### IDE Integration Tips

While Claude Code is terminal-based, it complements your IDE:

```
+----------------------------+----------------------------+
|  Terminal (Claude Code)    |  IDE (VS Code, etc.)       |
+----------------------------+----------------------------+
|  - Ask questions           |  - Edit files              |
|  - Get explanations        |  - Run debugger            |
|  - Generate code           |  - View structure          |
|  - Review changes          |  - Navigate code           |
+----------------------------+----------------------------+
```

**Workflow**: Keep Claude Code in a split terminal while coding
in your IDE.

----------------------------------------------------------------------


### Practice Exercise 3.5: Git Workflow

```
+===========================================+
|  EXERCISE 3.5                             |
|-------------------------------------------|
|  Difficulty: Medium                       |
|  XP Reward: +15 XP                        |
+===========================================+
```

**Task**: Use Claude Code for a Git-assisted workflow:

  1. Make some changes to a file in a Git repository
  2. Start Claude Code
  3. Ask: "What files have I changed?"
  4. Ask: "Write a commit message for these changes"
  5. Ask: "Is there anything I should review before committing?"

**Success Criteria**: Used Claude Code to assist with Git workflow.

- [ ] Completed

----------------------------------------------------------------------


## Chapter 7: Efficiency Techniques

### Technique 1: Template Prompts

Create reusable prompt templates for common tasks:


#### Bug Report Analysis

```
Analyze this bug report:
[paste bug report]

Please:
1. Summarize the issue
2. Identify likely causes
3. Suggest investigation steps
4. Propose fixes
```


#### Code Review Template

```
Review this code for:
1. Logic errors
2. Security vulnerabilities
3. Performance issues
4. Style improvements
5. Missing edge cases

Code:
[paste code]
```


### Technique 2: Batch Operations

Process multiple items at once:

```
> Review all Python files in src/ for PEP 8 violations
> Check all JavaScript files for console.log statements
> List all TODO comments in the codebase
```


### Technique 3: Progressive Refinement

Start broad, then narrow down:

```
Round 1: "Explain the authentication system"
Round 2: "Focus on the JWT validation logic"
Round 3: "Explain line 45-60 in auth.py specifically"
```


### Technique 4: Context Anchoring

Establish context at the start of sessions:

```
First prompt of session:
"I'm working on [project name], specifically [component].
My goal today is [objective].
The relevant files are in [directory].
Let's start by [first task]."
```

```
+----------------------------------------------------+
|  >>> ACHIEVEMENT UNLOCKED: Efficiency Expert       |
|      (+5 XP)                                       |
+----------------------------------------------------+
```

----------------------------------------------------------------------


## Level 3 Challenge: The Workflow Warrior

```
+======================================================================+
|  CHALLENGE: THE WORKFLOW WARRIOR                                     |
|----------------------------------------------------------------------|
|  Difficulty: Medium                                                  |
|  XP Reward: +30 XP                                                   |
+======================================================================+
```

### The Scenario

Optimize your personal development workflow using everything
you've learned.


### Your Mission

  1. **Create a CLAUDE.md** for your main project
  2. **Document your workflow** (what you do daily)
  3. **Identify 3 areas** Claude Code can help most
  4. **Create template prompts** for each area
  5. **Test the templates** in real sessions
  6. **Measure improvement** (even subjectively)


### Deliverables

  * A complete CLAUDE.md file
  * 3 reusable prompt templates
  * Notes on how they improved your workflow

- [ ] Completed

----------------------------------------------------------------------


## Level 3 Boss Battle: The Integration Gauntlet

```
+======================================================================+
|                                                                      |
|  *** BOSS BATTLE: THE INTEGRATION GAUNTLET ***                       |
|                                                                      |
|----------------------------------------------------------------------|
|  Difficulty: Hard                                                    |
|  XP Reward: +50 XP                                                   |
+======================================================================+
```

### The Ultimate Challenge

Complete a full development cycle using Claude Code at every stage:


#### Stage 1: Planning (25 points)

- [ ] Define a feature to build
- [ ] Have Claude break it into tasks
- [ ] Review and refine the plan


#### Stage 2: Implementation (25 points)

- [ ] Implement at least 3 components with Claude's help
- [ ] Use slash commands (/diff, /undo) appropriately
- [ ] Ask Claude to review each component


#### Stage 3: Testing (20 points)

- [ ] Have Claude write tests
- [ ] Run tests and fix issues with Claude's help


#### Stage 4: Documentation (15 points)

- [ ] Create or update documentation with Claude
- [ ] Generate helpful comments


#### Stage 5: Git Integration (15 points)

- [ ] Stage changes appropriately
- [ ] Generate commit messages with Claude
- [ ] Review the full diff before committing


### Victory Conditions

- [ ] All 5 stages completed
- [ ] Used at least 5 different slash commands
- [ ] Created or updated CLAUDE.md
- [ ] Session(s) spanned multiple days using resume

----------------------------------------------------------------------


## Level 3 Summary

### New Skills Acquired

  1. **Session Management**: Multi-day workflows, project switching
  2. **CLAUDE.md**: Project-specific configuration
  3. **Slash Commands**: /undo, /diff, /compact, /model
  4. **Multi-Step Tasks**: Decomposition and execution
  5. **Tool Integration**: Git, IDE workflows
  6. **Efficiency Techniques**: Templates, batching, refinement


### Command Reference Update

```
+----------------------------------+----------------------------------+
|  Previous Levels                 |  Level 3 Additions               |
+----------------------------------+----------------------------------+
|  claude           # Start        |  /undo    # Undo last change     |
|  claude -r        # Resume       |  /diff    # Show file changes    |
|  claude -p "..."  # Print mode   |  /model   # Switch models        |
|  /help            # Show cmds    |  /compact # Condense context     |
|  /clear           # Clear hist   |                                  |
|  /exit            # Exit         |  CLAUDE.md # Project config      |
+----------------------------------+----------------------------------+
```

----------------------------------------------------------------------


## Level Completion Checklist

### Core Skills

- [ ] Can manage long-running sessions
- [ ] Created and use CLAUDE.md
- [ ] Know and use slash commands
- [ ] Can break down complex tasks
- [ ] Integrate Claude Code with Git
- [ ] Use efficiency techniques


### Exercises Completed

- [ ] Exercise 3.1: Session Strategy (+15 XP)
- [ ] Exercise 3.2: Create Your CLAUDE.md (+15 XP)
- [ ] Exercise 3.3: Slash Command Mastery (+10 XP)
- [ ] Exercise 3.4: Multi-Step Project (+25 XP)
- [ ] Exercise 3.5: Git Workflow (+15 XP)


### Challenges Completed

- [ ] The Workflow Warrior (+30 XP)
- [ ] Boss Battle: The Integration Gauntlet (+50 XP)


### Achievements Earned

- [ ] Workflow Analyst (+5 XP)
- [ ] Configuration Master (+5 XP)
- [ ] Task Commander (+5 XP)
- [ ] Efficiency Expert (+5 XP)
- [ ] Journeyman Complete (+5 XP)

----------------------------------------------------------------------


## XP Calculation

```
+----------------------------------+---------+
| Item                             | XP      |
+----------------------------------+---------+
| Reading Chapters (7 x 5 XP)      | 35      |
| Exercises (5 total)              | 80      |
| Challenge                        | 30      |
| Boss Battle                      | 50      |
| Achievements (5 x 5 XP)          | 25      |
+----------------------------------+---------+
| MAXIMUM AVAILABLE                | 220     |
| Required for Level 4             | 600     |
+----------------------------------+---------+
```

----------------------------------------------------------------------


## Ready for Level 4?

If your total XP (Level 1 + Level 2 + Level 3) is 600 or more,
you're ready!

```
+============================================================+
|  Level 3 Complete!                                         |
|  Level 3 XP Earned: ___ / 220 possible                     |
|  New Total: ___ XP                                         |
|                                                            |
|  [==========] EXPERT TRAINING BEGINS!                      |
+============================================================+
```

  --> Continue to Level 4: Expert (04-LEVEL-EXPERT.md)

----------------------------------------------------------------------


## Power-Up Tips

```
+============================================================+
|  EASTER EGG #3: Create a .claude/ directory for            |
|  project-specific templates:                               |
|                                                            |
|  .claude/                                                  |
|    prompts/                                                |
|      code-review.md                                        |
|      bug-fix.md                                            |
|      documentation.md                                      |
+============================================================+

+============================================================+
|  EASTER EGG #4: Use environment variables for common       |
|  configurations:                                           |
|                                                            |
|  export CLAUDE_MODEL=opus                                  |
|  export CLAUDE_EDITOR=vim                                  |
+============================================================+
```

======================================================================
  Level 3 Complete - You are now a Claude Code Journeyman!
======================================================================

  <-- Level 2: Apprentice (02-LEVEL-APPRENTICE.md)
  --> Level 4: Expert (04-LEVEL-EXPERT.md)
