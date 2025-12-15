
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
|  XP Available: 270 XP          |
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


### Additional Slash Commands

Beyond the essentials, more specialized commands:

```
+-------------+-----------------------------------------------+
| Command     | Description                                   |
+-------------+-----------------------------------------------+
| /init       | Initialize Claude Code in current directory   |
| /cost       | Show token usage and estimated cost           |
| /settings   | View/modify configuration                     |
| /tasks      | List background tasks (agents*, shells)       |
| /bugs       | Report issues to Claude Code team             |
| /version    | Show Claude Code version info                 |
| /add-dir    | Add additional directory to workspace         |
| /rewind     | Rollback to previous checkpoint*              |
+-------------+-----------------------------------------------+

*See Glossary in 00-START-HERE.md for "agents" and "checkpoint"
```


### Using /add-dir

Expand your workspace mid-session:

```
> /add-dir ../other-project

# Claude now has access to both:
  - Current project
  - ../other-project

Use cases:
  - Multi-repository workflows
  - Shared libraries
  - Related microservices
```


### Using /rewind

Quickly undo changes (or press ESC ESC):

```
> /rewind

✓ Restored to previous checkpoint
  Files reverted: 3
  Changes undone: 12
```


### Using /init

Set up Claude Code for a new project:

```
> /init

Creates:
  - .claude/ directory
  - CLAUDE.md template
  - .gitignore entries
  - Project configuration
```


### Using /cost

Track your spending:

```
> /cost

Output:
  Session Tokens: 12,450
  Estimated Cost: $0.037
  Model: claude-sonnet-4

  Breakdown:
    Input tokens:  8,200 ($0.024)
    Output tokens: 4,250 ($0.013)
```


### Using /tasks

Monitor background operations:

```
> /tasks

Active Tasks:
  [1] Agent: Explore codebase (running, 45s)
  [2] Shell: npm install (running, 12s)
  [3] Agent: Security audit (completed)

Commands:
  /tasks kill 1    - Stop task #1
  /tasks output 3  - View task #3 output
```


### Using /settings

Configure Claude Code behavior:

```
> /settings

Shows current settings:
  Model: claude-sonnet-4
  Max Tokens: 4096
  Temperature: 0.7

Change settings:
  /settings model opus
  /settings max_tokens 8192
```


### Custom Slash Commands

Create your own commands in `.claude/commands/`:

```bash
# .claude/commands/review.md
Review the current PR for:
- Security issues
- Performance problems
- Code style violations
- Missing tests

Provide a detailed report.
```

Usage:
```
> /review

# Claude executes the prompt from review.md
```


### Slash Command Best Practices

```
+-----------------------------------------------------------+
| DO's                            | DON'Ts                  |
+---------------------------------+-------------------------+
| ✓ Use /diff before accepting    | ✗ Skip /diff for big    |
|   major changes                 |   changes               |
| ✓ Use /compact in long sessions | ✗ Let context fill up   |
| ✓ Use /undo for mistakes        | ✗ Manually revert files |
| ✓ Check /cost periodically      | ✗ Ignore token usage    |
| ✓ Create custom commands for    | ✗ Repeat same prompts   |
|   repeated tasks                |   manually              |
+---------------------------------+-------------------------+
```


### Advanced: Slash Command Chaining

Some workflows benefit from command sequences:

```bash
# In .claude/commands/deploy-check.md
Run these checks before deployment:

1. /diff - Show all changes
2. Run test suite
3. Check for TODOs
4. Verify environment configs
5. /cost - Confirm token usage is reasonable

Generate deployment checklist.
```

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


## Chapter 8: Memory and Conversation Persistence

### How Claude Code Remembers

Understanding conversation memory helps you work more effectively:

```
+--------------------------------------------------------------+
|  CONVERSATION LIFECYCLE                                       |
|--------------------------------------------------------------|
|                                                              |
|  Start Session  -->  Conversation  -->  Exit Session         |
|                          |                    |              |
|                          v                    v              |
|                    Memory Buffer        Save to Disk         |
|                                                              |
|  Resume (-r)  <--  Load from Disk                            |
|                                                              |
+--------------------------------------------------------------+
```


### Where Conversations Are Stored

```bash
# Conversation storage location
~/.config/claude-code/conversations/

# Each session gets a unique file
~/.config/claude-code/conversations/session-2025-01-15-143022.json
```


### Conversation File Structure

```json
{
  "session_id": "abc123",
  "created_at": "2025-01-15T14:30:22Z",
  "model": "claude-sonnet-4",
  "messages": [
    {
      "role": "user",
      "content": "Help me debug this function",
      "timestamp": "2025-01-15T14:30:25Z"
    },
    {
      "role": "assistant",
      "content": "I'll analyze that function...",
      "timestamp": "2025-01-15T14:30:28Z"
    }
  ],
  "context": {
    "files_accessed": ["src/main.py", "tests/test_main.py"],
    "working_directory": "/home/user/project"
  }
}
```


### Managing Multiple Conversations

Different strategies for different projects:

```
Strategy 1: One Conversation Per Project
  /project-a --> conversation-a.json
  /project-b --> conversation-b.json

Strategy 2: One Conversation Per Feature
  Feature branch --> New conversation
  Merge complete --> Archive conversation

Strategy 3: Daily Conversations
  Monday --> conversation-monday.json
  Tuesday --> conversation-tuesday.json
```


### Resume Behavior

What happens when you resume:

```bash
claude -r

# Claude loads:
  ✓ Previous conversation history
  ✓ Files that were accessed
  ✓ Context about the project
  ✓ Your preferences from session

# Claude does NOT load:
  ✗ Files that have changed since
  ✗ New files created
  ✗ External state changes
```


### Memory Limits and Context Windows

Understanding limits helps you work within them:

```
+----------------------------------+
| Model Context Limits              |
+----------------------------------+
| Claude Sonnet: ~200K tokens      |
| Claude Opus:   ~200K tokens      |
| Claude Haiku:  ~200K tokens      |
+----------------------------------+

Typical conversation:
  - 100 messages: ~50K tokens
  - Large codebase context: ~100K tokens
  - Room for responses: ~50K tokens
```


### When to Use /compact

Compact when:

```
✓ Long session (100+ exchanges)
✓ Context feels "full" (slower responses)
✓ Working on new subtask
✓ Want to "reset" focus

Example:
  > We've discussed authentication for 50 messages.
  > Let's /compact and move to the payment system.
```


### Clearing vs Compacting

```
+---------------------+--------------------+-------------------+
| Action              | What Happens       | When to Use       |
+---------------------+--------------------+-------------------+
| /clear              | Delete all history | Fresh start       |
|                     | Lose all context   | New topic         |
|                     |                    | Privacy concern   |
+---------------------+--------------------+-------------------+
| /compact            | Summarize history  | Long session      |
|                     | Keep key context   | Reduce tokens     |
|                     | Continue working   | Stay on topic     |
+---------------------+--------------------+-------------------+
```


### Privacy Considerations

Your conversations contain sensitive information:

```
Conversations Include:
  - Code snippets
  - File paths
  - Project structure
  - API keys (if mentioned)
  - Business logic
  - Error messages

Best Practices:
  ✓ Don't share API keys in conversations
  ✓ Use environment variables for secrets
  ✓ Be mindful in shared environments
  ✓ Clear sensitive conversations when done
```


### Archiving Conversations

For long-term reference:

```bash
# Export a conversation
claude --export-session session-abc123 > project-notes.md

# Archive old conversations
mv ~/.config/claude-code/conversations/old-* ~/claude-archives/

# Search archived conversations
grep -r "authentication" ~/claude-archives/
```


### Cross-Project Context

Carry insights between projects:

```
Pattern: Start new session with context from old one

Session A (Project 1):
  > How should I structure API error handling?
  [Good discussion and solution]

Session B (Project 2):
  > I previously learned a good pattern for API error handling.
  > Apply that pattern to this new project.
  [Claude uses general knowledge from training, not Session A]

Note: Claude doesn't access old sessions, but you can
      reference patterns you learned.
```


### Checkpoints and Rewind

Claude Code automatically saves your code state before each change:

```
+--------------------------------------------------------------+
|  CHECKPOINT SYSTEM                                            |
|--------------------------------------------------------------|
|                                                              |
|  Before edit  -->  Checkpoint saved  -->  Edit applied       |
|                           |                                  |
|                           v                                  |
|                    Rewind available                          |
|                                                              |
+--------------------------------------------------------------+
```


#### Using /rewind

Instantly rollback changes:

```bash
> /rewind

# Or press Esc twice
ESC ESC

# Claude shows:
⏪ Rewinding to previous checkpoint...
✓ Restored: src/main.py (2 changes reverted)
```


#### Why Checkpoints Matter

```
Without Checkpoints:
  "Undo that last change..."
  "Wait, undo the one before that too..."
  "Actually, go back 5 changes..."
  😰 Manual tracking, error-prone

With Checkpoints:
  ESC ESC
  ✅ Instant rewind, always safe to experiment
```


### Context Filtering with .claudeignore

Exclude files from Claude's context to improve performance:

```bash
# Create .claudeignore in project root
touch .claudeignore
```


#### Example .claudeignore

```
# Dependencies
node_modules/
venv/
__pycache__/

# Build artifacts
dist/
build/
*.pyc
*.o

# Large data files
*.csv
*.db
data/

# Sensitive files
.env
secrets/
*.key

# Generated files
coverage/
.next/
```


#### Why Use .claudeignore

```
+----------------------------------+
| Benefits of .claudeignore         |
+----------------------------------+
| ✓ Faster context loading         |
| ✓ Reduced token usage            |
| ✓ Better performance             |
| ✓ Privacy protection             |
| ✓ Focus on relevant code         |
+----------------------------------+

Example Impact:
  Before: 500K tokens (with node_modules)
  After:   50K tokens (with .claudeignore)
  Savings: 90% reduction!
```


#### Syntax

```
# Patterns work like .gitignore:

# Ignore directory
logs/

# Ignore file type
*.log

# Ignore specific file
config/production.json

# Negative pattern (don't ignore)
!important.log

# Ignore everywhere
**/*.test.js
```


#### Team .claudeignore

Commit to version control for team consistency:

```bash
# .claudeignore
# Generated by team for Claude Code optimization

# Large dependencies
node_modules/
vendor/

# Build outputs
dist/
target/

# Test coverage
coverage/
.nyc_output/
```

```
+----------------------------------------------------+
|  >>> ACHIEVEMENT UNLOCKED: Memory Master (+5 XP)   |
+----------------------------------------------------+
```

----------------------------------------------------------------------


## Chapter 9: Vision and Image Capabilities

### Claude Code Can See

Claude Code's vision capabilities enable visual debugging and design
review:

```
+--------------------------------------------------------------+
|  VISUAL CAPABILITIES                                          |
|--------------------------------------------------------------|
|                                                              |
|  ✓ Screenshots                                               |
|  ✓ UI mockups                                                |
|  ✓ Diagrams and flowcharts                                   |
|  ✓ Error message screenshots                                 |
|  ✓ Design files (exported as images)                         |
|  ✓ Data visualizations                                       |
|                                                              |
+--------------------------------------------------------------+
```


### Sharing Images with Claude

Multiple methods:

```bash
# Method 1: Direct path (if supported)
claude
> Analyze this screenshot: ~/Desktop/error-screenshot.png

# Method 2: Drag and drop (in supported terminals)
claude
> [Drag image into terminal]
> What's wrong with this UI?

# Method 3: Base64 encoding (universal)
base64 screenshot.png | claude -p "Analyze this image"
```


### Use Case 1: Visual Debugging

```
Scenario: Application crashes with visual error

You:
  1. Take screenshot of error
  2. Share with Claude
  3. Ask for analysis

Claude analyzes:
  - Error message text
  - Stack trace
  - UI state
  - Visual indicators
```


### Use Case 2: UI/UX Review

```bash
claude
> Review this UI screenshot: app-mockup.png
>
> Check for:
> - Layout issues
> - Accessibility concerns
> - Alignment problems
> - Color contrast
> - Usability issues

Claude provides:
  - Visual feedback
  - Specific suggestions
  - Accessibility notes
  - Design improvements
```


### Use Case 3: Diagram Analysis

```
You: [Share flowchart image]
> Convert this flowchart into Python code

Claude:
  1. Analyzes diagram structure
  2. Identifies logic flow
  3. Generates corresponding code
  4. Explains the translation
```


### Use Case 4: Design Implementation

```
Workflow:
  1. Designer sends mockup (PNG/JPG)
  2. You share with Claude
  3. "Implement this design in React/HTML/CSS"

Claude:
  - Identifies layout structure
  - Suggests component breakdown
  - Generates code matching design
  - Notes design details (colors, spacing, fonts)
```


### Use Case 5: Documentation

```bash
> I have this architecture diagram (diagram.png).
> Create documentation explaining the system architecture.

Claude:
  - Describes components
  - Explains relationships
  - Documents data flow
  - Generates markdown docs
```


### Limitations of Vision

```
+---------------------------+---------------------------+
| Can Do                    | Cannot Do                 |
+---------------------------+---------------------------+
| Read text in images       | Edit images               |
| Identify UI elements      | Create images from scratch|
| Analyze layout            | Pixel-perfect measurements|
| Detect colors             | Access image metadata     |
| Recognize patterns        | Handle very large images  |
| Understand diagrams       | Real-time video           |
+---------------------------+---------------------------+
```


### Best Practices for Visual Tasks

```
+-----------------------------------------------------------+
| DO's                            | DON'Ts                  |
+---------------------------------+-------------------------+
| ✓ Use clear, high-res images    | ✗ Send blurry screenshots|
| ✓ Crop to relevant area         | ✗ Include unnecessary    |
|                                 |   parts                 |
| ✓ Provide context with image    | ✗ Assume Claude knows    |
|                                 |   full context          |
| ✓ Ask specific questions        | ✗ Ask vague "what is     |
|                                 |   this?" questions      |
| ✓ Use for debugging visual      | ✗ Use for extracting     |
|   issues                        |   large amounts of text |
+---------------------------------+-------------------------+
```


### Advanced: Multi-Image Analysis

Compare designs or track changes:

```bash
> Compare these two screenshots:
> - before.png (old design)
> - after.png (new design)
>
> What changed? Is it an improvement?

Claude analyzes:
  - Visual differences
  - Design improvements/regressions
  - User experience impact
```

```
+----------------------------------------------------+
|  >>> ACHIEVEMENT UNLOCKED: Visual Thinker (+10 XP) |
+----------------------------------------------------+
```

----------------------------------------------------------------------


## Chapter 10: Cost Management and Optimization

### Understanding Tokens and Costs

Every Claude Code interaction has a cost:

```
+--------------------------------------------------------------+
|  TOKEN ECONOMICS                                              |
|--------------------------------------------------------------|
|                                                              |
|  Your Input  -->  Tokenized  -->  Processed  -->  Response   |
|  (Prompt)        (~1K tokens)    (Claude)      (~2K tokens)  |
|                                                              |
|  Total: ~3K tokens × $0.003/1K = $0.009 per exchange        |
|                                                              |
+--------------------------------------------------------------+
```


### What Are Tokens?

```
Tokens are pieces of text:
  - 1 word ≈ 1-2 tokens
  - 100 words ≈ 75 tokens
  - 1 line of code ≈ 5-15 tokens

Examples:
  "Hello" = 1 token
  "Hello, world!" = 4 tokens
  "function calculateTotal()" = 5 tokens
```


### Cost by Model

```
+---------------+-------------+-------------+---------------+
| Model         | Input ($/1M)| Output($/1M)| When to Use   |
+---------------+-------------+-------------+---------------+
| Haiku         | $0.25       | $1.25       | Quick queries |
| Sonnet        | $3.00       | $15.00      | General work  |
| Opus          | $15.00      | $75.00      | Complex tasks |
+---------------+-------------+-------------+---------------+
```


### Estimating Session Costs

```bash
# Use /cost command
> /cost

Session Summary:
  Input tokens:   15,420
  Output tokens:   8,350
  Total tokens:   23,770

Cost breakdown (Sonnet):
  Input:  15,420 × $3.00/1M  = $0.046
  Output:  8,350 × $15.00/1M = $0.125
  Total:                       $0.171
```


### Cost Optimization Strategies

#### 1. Choose the Right Model

```bash
# Don't do this:
claude --model opus -p "What's 2+2?"  # $$$

# Do this:
claude --model haiku -p "What's 2+2?" # $

# Model selection guide:
Quick questions     --> Haiku
Standard coding     --> Sonnet
Complex reasoning   --> Opus
```


#### 2. Be Concise in Prompts

```
Expensive:
  "I was wondering if you could possibly help me understand
   this concept if you have time and it wouldn't be too much
   trouble to explain..."
  (40 tokens)

Cheap:
  "Explain this concept concisely"
  (5 tokens)
```


#### 3. Use Context Wisely

```bash
# Expensive: Re-sharing unchanged files
> Here's the entire codebase again [100K tokens]
> Now make a small change

# Cheap: Reference already-shared files
> Make that change to the file we discussed
```


#### 4. Compact Long Sessions

```
Session at 50K tokens:
  - Each response costs more (context is reprocessed)
  - Use /compact to reduce

After /compact (10K tokens):
  - Responses cost 80% less in input tokens
  - Keep working efficiently
```


### Tracking Usage

```bash
# Method 1: Built-in tracking
> /cost

# Method 2: Export usage logs
claude --usage-report > usage.csv

# Method 3: Environment variable logging
export CLAUDE_LOG_USAGE=true
```


### Setting Budget Limits

```bash
# Set monthly budget alert
export CLAUDE_BUDGET_LIMIT=50.00  # $50/month

# Claude warns you:
"⚠️  Budget: $45/$50 used this month"
```


### Cost-Effective Workflows

#### Pattern 1: Haiku for Exploration, Sonnet for Implementation

```bash
# Phase 1: Explore with Haiku (cheap)
claude --model haiku -p "List all API endpoints in this project"

# Phase 2: Implement with Sonnet (when you know what to do)
claude --model sonnet
> Implement the user authentication endpoint
```


#### Pattern 2: Batch Questions

```bash
# Expensive: Multiple sessions
Session 1: "How does auth work?"
Session 2: "How does DB work?"
Session 3: "How does API work?"

# Cheap: One session
Session 1:
  "Explain:
   1. How auth works
   2. How DB works
   3. How API works"
```


### Hidden Costs

Be aware of:

```
+----------------------------------+
| What Increases Costs              |
+----------------------------------+
| ✗ Very long conversations        |
| ✗ Sharing entire large files     |
| ✗ Repeating context              |
| ✗ Using Opus for simple tasks    |
| ✗ Not using /compact             |
+----------------------------------+
```


### ROI Calculation

Is Claude Code worth it?

```
Monthly Cost: $30-100 (typical developer)

Value Provided:
  - 2 hours saved per week = 8 hours/month
  - At $50/hour = $400/month value
  - ROI: 400% to 1,300%

Cost per task:
  - Simple query: $0.01
  - Code generation: $0.10
  - Full feature: $1.00
```

```
+----------------------------------------------------+
|  >>> ACHIEVEMENT UNLOCKED: Budget Conscious (+5 XP)|
+----------------------------------------------------+
```

----------------------------------------------------------------------


## Chapter 11: Advanced GitHub Integration

### GitHub CLI (gh) Integration

Claude Code works seamlessly with GitHub's CLI:

```bash
# Check if gh is installed
which gh

# If not, install it
# (instructions at cli.github.com)
```


### Use Case 1: PR Creation

```bash
claude
> Create a PR for my current branch

# Claude:
1. Analyzes your changes (git diff)
2. Generates PR title and description
3. Runs: gh pr create --title "..." --body "..."
```


### Use Case 2: PR Review

```bash
# Review a pull request
claude
> Review PR #234

# Claude:
1. Fetches PR: gh pr view 234
2. Analyzes code changes
3. Provides detailed review
4. Suggests improvements
```


### Use Case 3: Issue Management

```bash
> List open issues related to authentication

# Claude runs:
gh issue list --label auth --state open

> Create an issue for the bug I just found

# Claude creates issue with:
  - Descriptive title
  - Reproduction steps
  - Relevant code snippets
  - Labels
```


### Advanced Git Workflows

#### Workflow 1: Feature Branch Management

```
Complete workflow:
  1. Create feature branch
  2. Implement feature with Claude
  3. Have Claude write tests
  4. Claude reviews changes (git diff)
  5. Claude generates commit message
  6. Push and create PR
  7. Claude analyzes PR checks
```


#### Workflow 2: Code Review Assistance

```bash
# Get Claude's review before requesting human review
> Review my changes before I create PR

Claude checks:
  - Code quality
  - Security issues
  - Test coverage
  - Documentation
  - Commit message quality
```


#### Workflow 3: Rebase Interactive

```bash
> Help me clean up my commit history

# Claude suggests:
1. Which commits to squash
2. Improved commit messages
3. Logical grouping of changes

# Then guides you through:
git rebase -i HEAD~5
```


### GitHub Actions Integration

```bash
> Check why the CI pipeline failed

# Claude:
1. Runs: gh run list --limit 1
2. Gets failure details
3. Analyzes error logs
4. Suggests fixes
```


### Best Practices

```
+-----------------------------------------------------------+
| DO's                            | DON'Ts                  |
+---------------------------------+-------------------------+
| ✓ Let Claude analyze diffs      | ✗ Create PRs without    |
|   before committing             |   review                |
| ✓ Use Claude for commit msgs    | ✗ Commit secrets to Git |
| ✓ Review PR checks with Claude  | ✗ Force push to main    |
| ✓ Have Claude check for         | ✗ Skip CI checks        |
|   sensitive data                |                         |
+---------------------------------+-------------------------+
```

```
+----------------------------------------------------+
|  >>> ACHIEVEMENT UNLOCKED: Git Master (+10 XP)     |
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
| Reading Chapters (11 x 5 XP)     | 55      |
| Exercises (5 total)              | 80      |
| Challenge                        | 30      |
| Boss Battle                      | 50      |
| Achievements (9 total)           | 55      |
+----------------------------------+---------+
| MAXIMUM AVAILABLE                | 270     |
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
|  Level 3 XP Earned: ___ / 270 possible                     |
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
