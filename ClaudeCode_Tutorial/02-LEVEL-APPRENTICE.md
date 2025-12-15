
```
 ______________________________________________________________________
|                                                                      |
|   L E V E L   2 :   A P P R E N T I C E                             |
|                                                                      |
|   Building Your Foundation                                           |
|                                                                      |
|   XP Range: 100-299  |  Status: LEARNING                            |
|                                                                      |
|______________________________________________________________________|
```

======================================================================
                        LEVEL OBJECTIVES
======================================================================

By the end of this level, you will:

- [ ] Master command-line flags and options
- [ ] Understand prompt modes and input methods
- [ ] Work effectively with files and code
- [ ] Configure basic settings
- [ ] Use Claude Code for real coding tasks

```
+--------------------------------+
|  Prerequisites: Level 1 (100+) |
|  Estimated Time: 1-2 hours     |
|  XP Available: 210 XP          |
+--------------------------------+
```

----------------------------------------------------------------------


## Chapter 1: Command-Line Flags Deep Dive

### What Are Flags?

Flags (also called options or switches) modify how Claude Code
behaves. They start with `-` (short form) or `--` (long form).

```bash
claude -r              # Short form
claude --resume        # Long form (same thing)
```


### The Flag Family

Here's your expanded toolkit:

```
+----------+-------------+-------------------------------------+
| Flag     | Long Form   | Purpose                             |
+----------+-------------+-------------------------------------+
| -r       | --resume    | Resume previous conversation        |
| -p       | --print     | Print mode (non-interactive)        |
| -c       | --continue  | Continue and add to conversation    |
|          | --help      | Show help information               |
|          | --version   | Show version number                 |
|          | --model     | Specify AI model to use             |
|          | --no-cache  | Don't use cached responses          |
+----------+-------------+-------------------------------------+
```


### Understanding Each Flag

#### The Resume Flag (-r, --resume)

You learned this in Level 1. It restores your previous conversation:

```bash
claude -r
```

**When to use**: Continuing a debugging session, ongoing project
work, multi-day tasks.


#### The Print Flag (-p, --print)

This is for quick, one-off questions without entering interactive
mode:

```bash
claude -p "What is a Python decorator?"
```

Claude answers and immediately returns to your shell. No
conversation mode.

**When to use**: Quick questions, scripting, piping output.

```
+----------------------------------------------------+
|  >>> ACHIEVEMENT UNLOCKED: Flag Bearer (+5 XP)     |
+----------------------------------------------------+
```

----------------------------------------------------------------------


### Practice Exercise 2.1: Flag Exploration

```
+===========================================+
|  EXERCISE 2.1                             |
|-------------------------------------------|
|  Difficulty: Easy                         |
|  XP Reward: +10 XP                        |
+===========================================+
```

**Task**: Try each of these commands and observe the difference:

```bash
# 1. Interactive mode
claude

# 2. Print mode with a question (exit interactive first!)
claude -p "Explain recursion in one sentence"

# 3. Check version
claude --version

# 4. View all options
claude --help
```

**Success Criteria**: You understand the difference between
interactive and print mode.

- [ ] Completed

----------------------------------------------------------------------


## Chapter 2: Print Mode Mastery

### The Power of -p

Print mode transforms Claude Code from a conversation partner
into a command-line tool.

```bash
claude -p "Your question or prompt here"
```


### Use Cases for Print Mode

#### 1. Quick Code Explanations

```bash
claude -p "What does the 'yield' keyword do in Python?"
```


#### 2. One-Line Code Generation

```bash
claude -p "Write a bash one-liner to find all .js files"
```


#### 3. Quick Syntax Reminders

```bash
claude -p "Show me the syntax for a JavaScript arrow function"
```


#### 4. Shell Integration

```bash
# Combine with other commands
claude -p "Generate 5 random project name ideas" >> project_ideas.txt
```


### Interactive vs Print Mode Comparison

```
+-------------------------------+-------------------------------+
|  INTERACTIVE MODE (claude)    |  PRINT MODE (claude -p)       |
+-------------------------------+-------------------------------+
|  - Ongoing conversation       |  - Single question            |
|  - Context builds up          |  - Immediate response         |
|  - Multi-turn dialogue        |  - No session state           |
|  - Exit when done             |  - Returns to shell           |
+-------------------------------+-------------------------------+
```

----------------------------------------------------------------------


### Practice Exercise 2.2: Print Mode Workout

```
+===========================================+
|  EXERCISE 2.2                             |
|-------------------------------------------|
|  Difficulty: Easy                         |
|  XP Reward: +10 XP                        |
+===========================================+
```

**Task**: Use print mode to answer these questions (run each
as a separate command):

```bash
# 1. Get a quick definition
claude -p "Define 'API' in simple terms"

# 2. Generate a code snippet
claude -p "Write a Python function that reverses a string"

# 3. Get a command reminder
claude -p "How do I create a new git branch?"
```

**Success Criteria**: Successfully used print mode three times
without entering interactive mode.

- [ ] Completed

----------------------------------------------------------------------


## Chapter 3: Working with Files

### Claude Code's File Awareness

When you start Claude Code in a directory, it can see and
understand your files. This is where it becomes truly powerful.


### Asking About Files

In interactive mode:

```
> What files are in this directory?
> Explain the purpose of package.json
> Show me the main function in app.py
> What dependencies does this project have?
```


### Reading Specific Files

You can ask Claude to read and analyze files:

```
> Read the contents of config.yaml
> Analyze the main.py file and explain what it does
> Are there any bugs in utils.js?
```


### File Modification

Claude Code can also help modify files:

```
> Add error handling to the database connection in db.py
> Create a new file called helpers.py with utility functions
> Update the README with installation instructions
```

```
+=======================================================+
|  IMPORTANT: Claude will ask for permission before     |
|  making changes. Pay attention to what it proposes.   |
+=======================================================+
```

```
+----------------------------------------------------+
|  >>> ACHIEVEMENT UNLOCKED: File Whisperer (+5 XP)  |
+----------------------------------------------------+
```

----------------------------------------------------------------------


### Practice Exercise 2.3: File Interaction

```
+===========================================+
|  EXERCISE 2.3                             |
|-------------------------------------------|
|  Difficulty: Medium                       |
|  XP Reward: +15 XP                        |
+===========================================+
```

**Task**: Navigate to a project with code files and:

  1. Start Claude Code: `claude`
  2. Ask: "List all files and their purposes"
  3. Ask: "Explain the most important file in detail"
  4. Ask: "What improvements would you suggest?"

**Success Criteria**: Claude analyzed your project files and
provided insights.

- [ ] Completed

----------------------------------------------------------------------


## Chapter 4: The Dangerous Flag

### Understanding --dangerously-skip-permissions

```bash
claude -r --dangerously-skip-permissions
```

```
+=======================================================+
|  !!! WARNING: This flag should be used with caution!  |
+=======================================================+
```

### What It Does

Normally, Claude Code asks for permission before:

  * Modifying files
  * Running commands
  * Making system changes

The `--dangerously-skip-permissions` flag bypasses these safety
prompts.


### When to Use It

**Appropriate situations**:

  * Automated scripts where you've reviewed the workflow
  * Repetitive tasks you've done many times
  * Controlled environments (containers, VMs)
  * When you fully trust the operations

**Avoid when**:

  * Working on production systems
  * Running unfamiliar commands
  * Working with sensitive data
  * On your main development machine without backups


### The Risk-Reward Balance

```
               RISK
                ^
                |
       High     |     X --dangerously-skip-permissions
                |
                |
       Low      |  X Normal mode
                |
                +------------------------->
                    Low            High
                         SPEED
```

The flag trades safety for speed. Use wisely.

```
+----------------------------------------------------+
|  >>> ACHIEVEMENT UNLOCKED: Danger Zone             |
|      Awareness (+5 XP)                             |
+----------------------------------------------------+
```

----------------------------------------------------------------------


## Chapter 4.5: Understanding the Permission System

### How Permissions Work

Claude Code's permission system protects you from accidental or
malicious actions. Understanding it makes you both safer AND more
efficient.

```
+--------------------------------------------------------------+
|  PERMISSION FLOW                                              |
|--------------------------------------------------------------|
|                                                              |
|  You request action                                          |
|        ↓                                                     |
|  Claude analyzes request                                     |
|        ↓                                                     |
|  Action requires permission? ----NO---> Execute immediately  |
|        |                                                     |
|       YES                                                    |
|        ↓                                                     |
|  Show permission prompt                                      |
|        ↓                                                     |
|  You approve/deny                                            |
|        ↓                                                     |
|  Execute if approved                                         |
|                                                              |
+--------------------------------------------------------------+
```


### Types of Permissions

Claude Code requests permission for different action types:

```
+------------------+------------------------------+-------------+
| Permission Type  | Examples                     | Risk Level  |
+------------------+------------------------------+-------------+
| File Read        | Read source code             | Low         |
| File Write       | Edit/create files            | Medium      |
| File Delete      | Remove files                 | High        |
| Command Execute  | Run shell commands           | High        |
| Network Access   | API calls, downloads         | Medium      |
| System Changes   | Install packages, config     | Very High   |
+------------------+------------------------------+-------------+
```


### What Triggers Permission Prompts

Specific actions that require approval:

  1. **File Modifications**
     - Editing existing files
     - Creating new files
     - Deleting files
     - Moving/renaming files

  2. **Command Execution**
     - Running shell commands via Bash tool
     - Installing dependencies (npm, pip, etc.)
     - Git operations (commit, push)
     - System administration tasks

  3. **External Access**
     - Network requests
     - API calls
     - Downloading files
     - MCP tool usage


### Permission Prompt Example

When permission is needed, you'll see:

```
┌────────────────────────────────────────────────┐
│ 🔐 PERMISSION REQUIRED                          │
├────────────────────────────────────────────────┤
│ Claude wants to:                               │
│   • Edit file: src/main.py                     │
│   • Changes: Add error handling (15 lines)     │
│                                                │
│ [A]pprove  [D]eny  [V]iew Changes  [?]Help     │
└────────────────────────────────────────────────┘
```


### Safe Approval Practices

```
+-----------------------------------------------------------+
|  BEFORE APPROVING, CHECK:                                  |
|-----------------------------------------------------------|
|  [ ] Do I understand what action will be taken?           |
|  [ ] Is this action what I requested?                     |
|  [ ] Are the affected files correct?                      |
|  [ ] Is the scope reasonable? (not too many files)        |
|  [ ] Do I have backups? (for risky operations)            |
+-----------------------------------------------------------+
```


### Viewing Proposed Changes

Before approving file modifications, review:

```
Permission prompt shows:
  [V] View Changes

Shows diff:
  + Lines to be added (green)
  - Lines to be removed (red)
  ~ Lines to be modified (yellow)
```


### Permission Modes

Claude Code can operate in different permission modes:

```
+-------------------+------------------------+------------------+
| Mode              | Behavior               | Use Case         |
+-------------------+------------------------+------------------+
| Normal (default)  | Prompt for each action | Safe development |
| Trusted Project   | Remember approvals     | Known codebase   |
| Skip Permissions  | No prompts (dangerous) | Automation only  |
| Read-Only         | Never modify files     | Code review      |
+-------------------+------------------------+------------------+
```


### Corporate/Enterprise Settings

For teams with security policies:

```
# Organization can set permission policies
~/.config/claude-code/policy.json

{
  "permissions": {
    "file_write": "always_prompt",
    "command_exec": "deny",
    "network": "always_prompt"
  },
  "allowed_paths": ["/workspace"],
  "blocked_commands": ["rm -rf", "dd", "format"]
}
```


### Sandbox Mode

For maximum safety:

```bash
# Run Claude in sandbox mode
claude --sandbox

# Limitations in sandbox:
  - Cannot access files outside project directory
  - Cannot run system commands
  - Cannot install packages
  - Can only suggest changes
```


### Understanding Permission Errors

```
Common error: "Permission denied to write file"

Causes:
  1. File is outside allowed paths
  2. Policy blocks this action type
  3. File system permissions issue
  4. Read-only mode enabled

Solution:
  - Check policy configuration
  - Verify file permissions
  - Use appropriate mode
```


### Best Practices by Environment

#### Development Machine

```
✓ Use normal permission mode
✓ Review changes for important files
✓ Auto-approve for generated code/tests
✗ Don't skip permissions without review
```


#### Production Systems

```
✓ Use read-only mode for investigation
✓ Require approval for ALL changes
✓ Use audit logging
✗ NEVER use --dangerously-skip-permissions
```


#### CI/CD Pipelines

```
✓ Use --dangerously-skip-permissions (reviewed)
✓ Run in isolated containers
✓ Log all actions
✓ Review logs after execution
```


### Advanced: Custom Permission Handlers

Create custom approval flows:

```bash
# ~/.config/claude-code/hooks/permission.sh
#!/bin/bash

action="$1"
files="$2"

case "$action" in
  "file_write")
    # Custom logic: auto-approve test files
    if [[ "$files" == *"test_"* ]]; then
      exit 0  # Approve
    fi
    ;;
  "command_exec")
    # Log all commands
    echo "$(date): $files" >> ~/claude-commands.log
    ;;
esac

exit 1  # Deny by default (show prompt)
```


### Permission Audit Log

Enable logging to track all permissions:

```bash
# Enable audit log
export CLAUDE_AUDIT_LOG=~/.claude-audit.log

# View recent permissions
tail -f ~/.claude-audit.log

# Example log entry:
2025-01-15 14:30:22 | APPROVED | file_write | src/api.py
2025-01-15 14:31:05 | DENIED   | command_exec | rm -rf temp/
2025-01-15 14:32:18 | APPROVED | file_create | tests/test_api.py
```

```
+----------------------------------------------------+
|  >>> ACHIEVEMENT UNLOCKED: Security Conscious      |
|      (+5 XP)                                       |
+----------------------------------------------------+
```

----------------------------------------------------------------------


## Chapter 5: Combining Flags

### Flag Combinations

Flags can be combined for customized behavior:

```bash
# Resume with a specific model
claude -r --model claude-3-opus

# Print mode without cache
claude -p --no-cache "What's the weather API syntax?"
```


### Common Combinations

```
+------------------------------------------+------------------------+
| Combination                              | Use Case               |
+------------------------------------------+------------------------+
| claude -r                                | Continue work          |
| claude -p "question"                     | Quick lookup           |
| claude -r --dangerously-skip-permissions | Automated workflows    |
| claude --model opus                      | Use specific model     |
+------------------------------------------+------------------------+
```


### Order Doesn't Matter

```bash
claude -r --model opus
claude --model opus -r
# Both work the same way
```

----------------------------------------------------------------------


### Practice Exercise 2.4: Flag Combinations

```
+===========================================+
|  EXERCISE 2.4                             |
|-------------------------------------------|
|  Difficulty: Medium                       |
|  XP Reward: +15 XP                        |
+===========================================+
```

**Task**: Practice these flag combinations:

```bash
# 1. Start a session, exit, then resume
claude
# (have a conversation, exit)
claude -r

# 2. Quick question without entering interactive mode
claude -p "What is the difference between == and === in JavaScript?"

# 3. View all available flags
claude --help
```

**Success Criteria**: Successfully used at least 3 different
flag combinations.

- [ ] Completed

----------------------------------------------------------------------


## Chapter 6: Effective Prompting

### The Art of Good Prompts

The quality of Claude's responses depends heavily on how you
ask questions.


### Prompting Principles

#### 1. Be Specific

```
Bad:  "Fix my code"
Good: "Fix the null pointer exception in the getData()
       function on line 45 of utils.py"
```


#### 2. Provide Context

```
Bad:  "How do I sort this?"
Good: "I have an array of user objects with 'name' and 'age'
       fields. How do I sort them by age in descending order
       in JavaScript?"
```


#### 3. State Your Goal

```
Bad:  "Look at my function"
Good: "Review the processOrder function for potential bugs.
       I'm concerned about edge cases with empty orders."
```


#### 4. Specify Format

```
"Explain this in bullet points"
"Give me a code example"
"Keep the explanation under 100 words"
```


### Prompt Templates

#### For Code Review

```
Review [filename] for:
- Potential bugs
- Performance issues
- Code style improvements
Focus on the [specific function/section].
```


#### For Debugging

```
I'm getting [error message] when running [command/function].
The relevant code is in [file].
Expected behavior: [what should happen]
Actual behavior: [what is happening]
```


#### For Learning

```
Explain [concept] with:
- A simple analogy
- A code example
- Common mistakes to avoid
```

```
+----------------------------------------------------+
|  >>> ACHIEVEMENT UNLOCKED: Prompt Architect        |
|      (+5 XP)                                       |
+----------------------------------------------------+
```

----------------------------------------------------------------------


### Practice Exercise 2.5: Prompt Crafting

```
+===========================================+
|  EXERCISE 2.5                             |
|-------------------------------------------|
|  Difficulty: Medium                       |
|  XP Reward: +15 XP                        |
+===========================================+
```

**Task**: Rewrite these bad prompts as good prompts, then test them:

**Bad Prompt 1**: "Help with git"
**Your Better Version**: _______________

**Bad Prompt 2**: "Why doesn't this work?"
**Your Better Version**: _______________

**Bad Prompt 3**: "Write some code"
**Your Better Version**: _______________

**Success Criteria**: You created specific, context-rich prompts
that got better responses.

- [ ] Completed

----------------------------------------------------------------------


## Chapter 7: Real-World Coding Tasks

### Task 1: Code Explanation

```
> Explain this code block step by step:
> [paste your code]
> Focus on what a beginner might find confusing.
```


### Task 2: Bug Hunting

```
> I have a bug where users can submit the form multiple times.
> The form handler is in src/handlers/form.js
> Help me find and fix the issue.
```


### Task 3: Code Generation

```
> Create a Python class called 'TaskManager' that:
> - Stores tasks with title, description, and status
> - Has methods to add, remove, and update tasks
> - Can export tasks to JSON
> Include type hints and docstrings.
```


### Task 4: Refactoring

```
> Refactor the processData function in utils.py to:
> - Be more readable
> - Handle edge cases
> - Follow PEP 8 style guidelines
> Explain each change you make.
```


### Task 5: Test Writing

```
> Write unit tests for the Calculator class in math_ops.py
> Use pytest framework
> Cover edge cases and error conditions
```

----------------------------------------------------------------------


## Level 2 Challenge: The Code Companion

```
+======================================================================+
|  CHALLENGE: THE CODE COMPANION                                       |
|----------------------------------------------------------------------|
|  Difficulty: Medium                                                  |
|  XP Reward: +25 XP                                                   |
+======================================================================+
```

### The Scenario

You're starting a new feature and need Claude Code's help
throughout the process.


### Your Mission

  1. Navigate to a project directory
  2. Use Claude Code to:
     - Understand the existing code structure
     - Get suggestions for implementing a new feature
     - Have Claude write a small code snippet
     - Review the snippet for issues
  3. Use at least 3 different flags during this session
  4. Practice good prompting techniques


### Document Your Session

Note down:

  * What flags you used and why
  * Your best prompt
  * What you learned

----------------------------------------------------------------------


## Level 2 Boss Battle: The Multi-Modal Master

```
+======================================================================+
|                                                                      |
|  *** BOSS BATTLE: THE MULTI-MODAL MASTER ***                         |
|                                                                      |
|----------------------------------------------------------------------|
|  Difficulty: Hard                                                    |
|  XP Reward: +50 XP                                                   |
+======================================================================+
```

### The Ultimate Challenge

Complete a full coding workflow using everything you've learned:


#### Phase 1: Project Analysis

  1. Start Claude Code in a project directory
  2. Use effective prompts to understand the codebase
  3. Identify at least one area for improvement


#### Phase 2: Implementation

  1. Ask Claude to help implement an improvement
  2. Review the suggested changes carefully
  3. Have Claude explain why each change was made


#### Phase 3: Documentation

  1. Ask Claude to update or create documentation
  2. Use print mode to generate a quick summary
  3. Use the resume flag to continue if needed


#### Phase 4: Review

  1. Have Claude review the changes made
  2. Ask for any potential issues
  3. Get suggestions for future improvements


### Victory Conditions

- [ ] Used interactive mode effectively
- [ ] Used print mode at least twice
- [ ] Used resume flag at least once
- [ ] Practiced good prompting throughout
- [ ] Completed a real coding task with Claude's help

----------------------------------------------------------------------


## Level 2 Summary

### New Skills Acquired

  1. **Flag Mastery**: `-r`, `-p`, `--dangerously-skip-permissions`
  2. **Print Mode**: Quick, non-interactive queries
  3. **File Operations**: Reading, understanding, modifying code
  4. **Effective Prompting**: Specific, contextual, goal-oriented
  5. **Real Tasks**: Code review, debugging, generation, refactoring


### Command Reference Update

```
+----------------------------------------+-----------------------------+
| Level 1 Commands                       | Level 2 Commands (NEW)      |
+----------------------------------------+-----------------------------+
| claude          # Start conversation   | claude -p "prompt" # Print  |
| claude -r       # Resume conversation  | claude --help      # Help   |
| /help           # In-session help      | claude --version   # Ver    |
| /exit           # Exit session         | --dangerously-skip-perms    |
+----------------------------------------+-----------------------------+
```

----------------------------------------------------------------------


## Level Completion Checklist

### Core Skills

- [ ] Understand all common flags
- [ ] Can use print mode effectively
- [ ] Can work with project files
- [ ] Understand the dangerous flag
- [ ] Can combine flags
- [ ] Practice effective prompting


### Exercises Completed

- [ ] Exercise 2.1: Flag Exploration (+10 XP)
- [ ] Exercise 2.2: Print Mode Workout (+10 XP)
- [ ] Exercise 2.3: File Interaction (+15 XP)
- [ ] Exercise 2.4: Flag Combinations (+15 XP)
- [ ] Exercise 2.5: Prompt Crafting (+15 XP)


### Challenges Completed

- [ ] The Code Companion (+25 XP)
- [ ] Boss Battle: The Multi-Modal Master (+50 XP)


### Achievements Earned

- [ ] Flag Bearer (+5 XP)
- [ ] File Whisperer (+5 XP)
- [ ] Danger Zone Awareness (+5 XP)
- [ ] Prompt Architect (+5 XP)
- [ ] Apprentice Graduate (+5 XP)

----------------------------------------------------------------------


## XP Calculation

```
+----------------------------------+---------+
| Item                             | XP      |
+----------------------------------+---------+
| Reading Chapters (8 x 5 XP)      | 40      |
| Exercises (5 total)              | 65      |
| Challenge                        | 25      |
| Boss Battle                      | 50      |
| Achievements (6 x 5 XP)          | 30      |
+----------------------------------+---------+
| MAXIMUM AVAILABLE                | 210     |
| Required for Level 3             | 300     |
+----------------------------------+---------+
```

----------------------------------------------------------------------


## Ready for Level 3?

If your total XP (Level 1 + Level 2) is 300 or more, you're ready!

```
+============================================================+
|  Level 2 Complete!                                         |
|  Level 2 XP Earned: ___ / 210 possible                     |
|  Total XP: ___ (Level 1) + ___ (Level 2) = ___            |
|                                                            |
|  [==========] JOURNEYMAN AWAITS!                           |
+============================================================+
```

  --> Continue to Level 3: Journeyman (03-LEVEL-JOURNEYMAN.md)

----------------------------------------------------------------------


## Power-Up Tips

```
+============================================================+
|  EASTER EGG #1: Pipe content into Claude                   |
|  cat error.log | claude -p "What's causing these errors?"  |
+============================================================+

+============================================================+
|  EASTER EGG #2: Chain print mode commands                  |
|  claude -p "List 5 project ideas" | head -1 |              |
|  claude -p "Elaborate on this idea"                        |
+============================================================+
```

======================================================================
  Level 2 Complete - You are now a Claude Code Apprentice!
======================================================================

  <-- Level 1: Novice (01-LEVEL-NOVICE.md)
  --> Level 3: Journeyman (03-LEVEL-JOURNEYMAN.md)
