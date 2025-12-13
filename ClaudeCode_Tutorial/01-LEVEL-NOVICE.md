
```
 ______________________________________________________________________
|                                                                      |
|   L E V E L   1 :   N O V I C E                                     |
|                                                                      |
|   Your First Steps with Claude Code                                  |
|                                                                      |
|   XP Range: 0-99  |  Status: STARTING                               |
|                                                                      |
|______________________________________________________________________|
```

======================================================================
                        LEVEL OBJECTIVES
======================================================================

By the end of this level, you will:

- [ ] Understand what Claude Code is and why it matters
- [ ] Successfully launch Claude Code in your terminal
- [ ] Have your first conversation with Claude
- [ ] Learn basic interaction patterns
- [ ] Understand how to exit and resume sessions

```
+---------------------------+
|  Estimated Time: 30-45m   |
|  XP Available: 170 XP     |
+---------------------------+
```

----------------------------------------------------------------------


## Chapter 1: What is Claude Code?

### The Big Picture

Imagine having a brilliant coding partner who:

  * Never gets tired or frustrated
  * Has read virtually every programming book and documentation
  * Can understand your project context
  * Lives right in your terminal where you work

That's Claude Code.

**Claude Code** is a command-line interface (CLI) tool that brings
Claude, Anthropic's AI assistant, directly into your terminal.
Instead of switching between browser tabs and your code editor,
you can get AI assistance right where you're already working.


### Why Terminal-Based AI?

```
+-------------------------+----------------------------+
| Browser AI              | Claude Code (Terminal)     |
+-------------------------+----------------------------+
| Copy-paste code         | Direct file access         |
| Context switching       | Stay in your workflow      |
| Manual file sharing     | Automatic project aware    |
| Generic assistance      | Context-aware help         |
+-------------------------+----------------------------+
```

```
+----------------------------------------------------+
|  >>> ACHIEVEMENT UNLOCKED: Understanding the       |
|      Mission (+5 XP)                               |
+----------------------------------------------------+
```

----------------------------------------------------------------------


## Chapter 2: Installation Verification

Before we dive in, let's make sure Claude Code is properly installed.

### Quick Check

Open your terminal and run:

```bash
claude --version
```

**Expected Output**: You should see a version number (e.g., `1.0.x`)


### For WSL Users

If you're using Windows Subsystem for Linux:

```bash
# First, open your Ubuntu subsystem
wsl -d ubuntu

# Then verify Claude Code
claude --version
```


### Troubleshooting: Not Installed?

If you get "command not found":

```bash
# Install via npm (Node.js required)
npm install -g @anthropic-ai/claude-code

# Or check the official installation guide
# https://docs.anthropic.com/claude-code
```

----------------------------------------------------------------------


### Practice Exercise 1.1: Installation Check

```
+===========================================+
|  EXERCISE 1.1                             |
|-------------------------------------------|
|  Difficulty: Easy                         |
|  XP Reward: +10 XP                        |
+===========================================+
```

**Task**: Run the version check command and confirm Claude Code
is installed.

```bash
claude --version
```

**Success Criteria**: You see a version number displayed.

- [ ] Completed

----------------------------------------------------------------------


## Chapter 3: Your First Launch

### The Moment of Truth

Ready to meet Claude? It's as simple as:

```bash
claude
```

That's it. One word. Your terminal will transform into an
interactive AI conversation.


### What You'll See

When Claude Code starts, you'll see:

  1. A welcome message
  2. Context about your current directory
  3. A prompt waiting for your input

```
Claude Code v1.x.x
Current directory: /your/project/path
Type your message or /help for commands

>
```


### Your First Interaction

Try typing a simple greeting:

```
> Hello! Can you tell me what directory I'm in?
```

Claude will respond with awareness of your current location and
project context.

```
+----------------------------------------------------+
|  >>> ACHIEVEMENT UNLOCKED: First Contact (+5 XP)   |
+----------------------------------------------------+
```

----------------------------------------------------------------------


## Chapter 4: Basic Conversation

### How to Talk to Claude Code

Claude Code understands natural language. You don't need special
syntax or commands for basic interactions.

**Good examples**:

```
> What files are in this directory?
> Explain what this project does
> Help me understand the main.py file
> What programming language is this project using?
```


### The Power of Context

Unlike a regular chatbot, Claude Code can:

  1. **See your files**: It knows what's in your project directory
  2. **Read code**: It can examine and explain your source files
  3. **Understand structure**: It recognizes project patterns


### Try These Starter Prompts

```
> List all the files in the current directory
> What kind of project is this?
> Are there any README files I should read?
```

----------------------------------------------------------------------


### Practice Exercise 1.2: First Conversation

```
+===========================================+
|  EXERCISE 1.2                             |
|-------------------------------------------|
|  Difficulty: Easy                         |
|  XP Reward: +10 XP                        |
+===========================================+
```

**Task**: Start Claude Code and have a 3-message conversation.

  1. Launch Claude Code with `claude`
  2. Ask Claude what directory you're in
  3. Ask Claude to list the files
  4. Ask Claude to explain any file it finds

**Success Criteria**: You received helpful responses to all
three questions.

- [ ] Completed

----------------------------------------------------------------------


## Chapter 5: Essential Commands

### In-Session Commands

While chatting with Claude, you can use special commands that
start with `/`:

```
+----------+------------------------------------+
| Command  | What It Does                       |
+----------+------------------------------------+
| /help    | Shows available commands           |
| /clear   | Clears the conversation history    |
| /exit    | Exits Claude Code                  |
| Ctrl+C   | Also exits Claude Code             |
+----------+------------------------------------+
```


### Using /help

Type `/help` anytime to see available commands:

```
> /help
```

This displays all available slash commands and their descriptions.


### Exiting Claude Code

When you're done with your session:

  * Type `/exit`
  * Or press `Ctrl+C`
  * Or press `Ctrl+D`

```
+=======================================================+
|  PRO TIP: Your conversation isn't lost when you       |
|  exit! You can resume it later with: claude -r        |
+=======================================================+
```

```
+----------------------------------------------------+
|  >>> ACHIEVEMENT UNLOCKED: Command Discovery       |
|      (+5 XP)                                       |
+----------------------------------------------------+
```

----------------------------------------------------------------------


### Practice Exercise 1.3: Command Practice

```
+===========================================+
|  EXERCISE 1.3                             |
|-------------------------------------------|
|  Difficulty: Easy                         |
|  XP Reward: +10 XP                        |
+===========================================+
```

**Task**: Practice using in-session commands.

  1. Start Claude Code
  2. Use `/help` to see available commands
  3. Have a brief conversation
  4. Use `/clear` to reset the conversation
  5. Exit using `/exit`

**Success Criteria**: Successfully used all three commands.

- [ ] Completed

----------------------------------------------------------------------


## Chapter 6: Resuming Sessions

### The Magic of `-r`

One of Claude Code's most useful features is conversation
resumption. Your previous context is saved!

```bash
# Resume your last conversation
claude -r
```


### Why This Matters

Imagine you're:

  * Debugging a complex issue
  * In the middle of explaining your project
  * Working through a multi-step task

You need to take a break. No problem! Just exit and later:

```bash
claude -r
```

Claude remembers everything from your previous session.


### Understanding Conversation Memory

```
Session 1                    [Exit]
    |
    v
[Time passes - hours, days]
    |
    v
Session 2: claude -r         [Continues where you left off!]
```

----------------------------------------------------------------------


### Practice Exercise 1.4: Resume a Conversation

```
+===========================================+
|  EXERCISE 1.4                             |
|-------------------------------------------|
|  Difficulty: Easy                         |
|  XP Reward: +10 XP                        |
+===========================================+
```

**Task**: Test the resume functionality.

  1. Start Claude Code: `claude`
  2. Tell Claude something memorable
     (e.g., "Remember that my favorite color is blue")
  3. Exit Claude Code
  4. Resume with `claude -r`
  5. Ask Claude "What's my favorite color?"

**Success Criteria**: Claude remembers what you told it in the
previous session.

- [ ] Completed

```
+----------------------------------------------------+
|  >>> ACHIEVEMENT UNLOCKED: Time Traveler (+5 XP)   |
+----------------------------------------------------+
```

----------------------------------------------------------------------


## Chapter 7: Getting Help

### The --help Flag

Need a quick reminder of available options? Use the help flag:

```bash
claude --help
```

This displays:

  * All available command-line flags
  * Brief descriptions of each option
  * Usage examples


### Reading Help Output

```bash
$ claude --help

Usage: claude [options] [prompt]

Options:
  -r, --resume       Resume the previous conversation
  -p, --print        Print response without interactive mode
  --help             Show this help message
  ...
```

```
+=======================================================+
|  TIP: Help output is your friend. Refer to it often   |
|  as you learn new features!                           |
+=======================================================+
```

----------------------------------------------------------------------


## Level 1 Challenge: The Newcomer's Trial

```
+======================================================================+
|  CHALLENGE: THE NEWCOMER'S TRIAL                                     |
|----------------------------------------------------------------------|
|  Difficulty: Medium                                                  |
|  XP Reward: +20 XP                                                   |
+======================================================================+
```

### The Scenario

You've just cloned a mysterious project from GitHub. Your mission
is to use Claude Code to understand what it is.


### Your Tasks

  1. Navigate to any project directory on your computer
  2. Start Claude Code
  3. Ask Claude to:
     - Identify what kind of project it is
     - Find the main entry point file
     - Explain the project structure
  4. Exit properly
  5. Resume the conversation and verify context is preserved


### Success Criteria

- [ ] Launched Claude Code in a project directory
- [ ] Received a project overview from Claude
- [ ] Successfully exited and resumed
- [ ] Context was preserved after resuming

----------------------------------------------------------------------


## Level 1 Boss Battle: The Configuration Quest

```
+======================================================================+
|                                                                      |
|  *** BOSS BATTLE: THE CONFIGURATION QUEST ***                        |
|                                                                      |
|----------------------------------------------------------------------|
|  Difficulty: Hard                                                    |
|  XP Reward: +50 XP                                                   |
+======================================================================+
```

### The Challenge

Complete ALL of the following in a single session (you can resume
if needed):

  1. **Scout the Territory**: Ask Claude to analyze your current
     directory structure

  2. **Gather Intelligence**: Have Claude explain 3 different
     files in detail

  3. **Test Communication**: Use at least 5 different
     conversational prompts

  4. **Master the Tools**: Use `/help` and `/clear` appropriately

  5. **Prove Persistence**: Exit, resume with `-r`, and continue
     seamlessly


### Victory Conditions

Document your session by noting:

  * What directory you explored
  * What files Claude explained
  * How the resume feature worked

```
+----------------------------------------------------+
|  >>> ACHIEVEMENT UNLOCKED: Novice No More (+5 XP)  |
+----------------------------------------------------+
```

----------------------------------------------------------------------


## Level 1 Summary

### What You Learned

  1. **Claude Code Basics**: What it is and why it's useful
  2. **Launching**: Simply type `claude`
  3. **Conversing**: Natural language interaction
  4. **Commands**: `/help`, `/clear`, `/exit`
  5. **Resuming**: Use `claude -r` to continue previous sessions
  6. **Getting Help**: `claude --help` for options


### Essential Commands Quick Reference

```
+-------------------+-------------------------------------+
| Command           | Description                         |
+-------------------+-------------------------------------+
| claude            | Start new conversation              |
| claude -r         | Resume last conversation            |
| claude --help     | Show help                           |
| /help             | In-session help                     |
| /clear            | Clear conversation                  |
| /exit             | Exit (or Ctrl+C)                    |
+-------------------+-------------------------------------+
```

----------------------------------------------------------------------


## Level Completion Checklist

### Core Skills

- [ ] Can launch Claude Code
- [ ] Can have a basic conversation
- [ ] Know how to exit properly
- [ ] Can resume a previous conversation
- [ ] Can use in-session commands


### Exercises Completed

- [ ] Exercise 1.1: Installation Check (+10 XP)
- [ ] Exercise 1.2: First Conversation (+10 XP)
- [ ] Exercise 1.3: Command Practice (+10 XP)
- [ ] Exercise 1.4: Resume a Conversation (+10 XP)


### Challenges Completed

- [ ] The Newcomer's Trial (+20 XP)
- [ ] Boss Battle: The Configuration Quest (+50 XP)


### Achievements Earned

- [ ] Understanding the Mission (+5 XP)
- [ ] First Contact (+5 XP)
- [ ] Command Discovery (+5 XP)
- [ ] Time Traveler (+5 XP)
- [ ] Novice No More (+5 XP)

----------------------------------------------------------------------


## XP Calculation

```
+----------------------------------+---------+
| Item                             | XP      |
+----------------------------------+---------+
| Reading Chapters (7 x 5 XP)      | 35      |
| Exercises (4 x 10 XP)            | 40      |
| Challenge                        | 20      |
| Boss Battle                      | 50      |
| Achievements (5 x 5 XP)          | 25      |
+----------------------------------+---------+
| MAXIMUM AVAILABLE                | 170     |
| Required for Level 2             | 100     |
+----------------------------------+---------+
```

----------------------------------------------------------------------


## Ready for Level 2?

If you've completed the core skills and at least the exercises,
you have enough XP to proceed!

```
+============================================================+
|  Level 1 Complete!                                         |
|  XP Earned: ___ / 170 possible                             |
|  New Total: ___ XP                                         |
|                                                            |
|  [==========] LEVEL UP AVAILABLE!                          |
+============================================================+
```

  --> Continue to Level 2: Apprentice (02-LEVEL-APPRENTICE.md)

----------------------------------------------------------------------


## Quick Tips Before You Go

  1. **Practice makes permanent**: Use Claude Code daily, even
     for small tasks

  2. **Be specific**: The more context you give Claude, the better
     help you'll receive

  3. **Experiment freely**: You can't break anything by asking
     questions

  4. **Resume often**: The `-r` flag is your friend for ongoing
     projects

======================================================================
  Level 1 Complete - You are now a Claude Code Novice!
======================================================================

  <-- Back to Start (00-START-HERE.md)
  --> Level 2: Apprentice (02-LEVEL-APPRENTICE.md)
