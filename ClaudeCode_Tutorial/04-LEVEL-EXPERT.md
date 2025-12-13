# Level 4: Expert
## Advanced Techniques and Power Features

```
+--------------------------------------------------+
|  LEVEL 4: EXPERT                                 |
|  XP Range: 600-999                               |
|  Status: [==========] ELITE TRAINING             |
+--------------------------------------------------+
```

---

## Level Objectives

By the end of this level, you will:
- [ ] Master model selection and switching
- [ ] Leverage advanced context management
- [ ] Use Claude Code for system administration
- [ ] Create automated workflows
- [ ] Handle edge cases and troubleshooting
- [ ] Understand Claude Code's capabilities and limits

**Prerequisites**: Completed Levels 1-3 (600+ XP)
**Estimated Time**: 3-4 hours
**XP Available**: 400 XP

---

## Chapter 1: Model Selection and Optimization

### Understanding Model Options

Claude Code can use different models with varying capabilities:

| Model | Strengths | Best For |
|-------|-----------|----------|
| claude-3-opus | Most capable, thoughtful | Complex analysis, nuanced tasks |
| claude-3-sonnet | Balanced speed/capability | General development work |
| claude-3-haiku | Fast, efficient | Quick queries, simple tasks |

### Switching Models

#### Via Command Line

```bash
claude --model claude-3-opus
claude --model claude-3-sonnet
claude --model claude-3-haiku
```

#### Via Slash Command (In Session)

```
> /model opus
> /model sonnet
> /model haiku
```

### Model Selection Strategy

```
Task Complexity
      ^
High  |  OPUS
      |    - Architecture decisions
      |    - Complex debugging
      |    - Code review (critical)
      |
Med   |  SONNET (Default)
      |    - General development
      |    - Feature implementation
      |    - Standard debugging
      |
Low   |  HAIKU
      |    - Syntax questions
      |    - Simple generation
      |    - Quick lookups
      +---------------------------------> Speed Priority
                Low        Med       High
```

### Cost-Performance Optimization

Different models have different costs. Optimize by:

1. **Start with Haiku** for exploration
2. **Switch to Sonnet** for implementation
3. **Use Opus** for critical decisions

**Achievement Unlocked: Model Strategist** (+5 XP)

---

### Practice Exercise 4.1: Model Comparison

**Difficulty**: Medium
**XP Reward**: +15 XP

**Task**: Compare model responses on the same task:

1. Start with: `claude --model haiku`
2. Ask: "Explain the singleton pattern with pros and cons"
3. Exit and try: `claude --model opus`
4. Ask the same question
5. Compare depth and nuance of responses

**Success Criteria**: Documented differences between model responses.

- [ ] Completed

---

## Chapter 2: Advanced Context Management

### Understanding Context Windows

Claude has a "context window" - the amount of information it can consider at once.

```
+----------------------------------------+
|           CONTEXT WINDOW               |
|                                        |
| System Prompt                          |
| + CLAUDE.md content                    |
| + Conversation history                 |
| + File contents you've shared          |
| + Your current prompt                  |
|                                        |
| = Total context used                   |
+----------------------------------------+
```

### Context Management Techniques

#### 1. Summarization

When context gets large:
```
> Summarize our discussion so far in 5 bullet points
> /compact
```

#### 2. Selective File Sharing

Don't share everything. Be strategic:

```
Bad:  "Read all files in the project"
Good: "Read only src/auth/login.py - I'm debugging the login function"
```

#### 3. Context Refresh

For very long sessions:
```
> Let's reset context. Here's what matters:
> 1. We're building [feature]
> 2. Key files: [list]
> 3. Current issue: [description]
```

### The /compact Command Deep Dive

```
> /compact
```

This command:
1. Analyzes the conversation history
2. Extracts key information
3. Creates a compressed summary
4. Frees up context space

**Use when**: Session is slowing down or responses seem to lose earlier context.

**Achievement Unlocked: Context Commander** (+5 XP)

---

### Practice Exercise 4.2: Context Optimization

**Difficulty**: Medium
**XP Reward**: +15 XP

**Task**: Practice context management:

1. Start a session and have a long conversation (10+ exchanges)
2. Ask Claude to summarize the key points
3. Use `/compact` to optimize context
4. Continue the conversation and verify context is preserved
5. Practice selective file sharing

**Success Criteria**: Successfully managed a long session without context loss.

- [ ] Completed

---

## Chapter 3: System Administration Tasks

### Claude Code for DevOps

Claude Code isn't just for coding - it's powerful for system administration.

### Common SysAdmin Tasks

#### Log Analysis

```
> Analyze /var/log/nginx/error.log for the last hour
> What errors are most common?
> Suggest fixes for the top 3 issues
```

#### Configuration Review

```
> Review my nginx.conf for security issues
> Check this Dockerfile for best practices
> Audit my .env.example for missing variables
```

#### Script Generation

```
> Write a bash script that:
> - Backs up the database
> - Compresses the backup
> - Uploads to S3
> - Cleans up old backups (keep last 7)
```

#### Service Troubleshooting

```
> My PostgreSQL database is running slow
> What metrics should I check?
> Generate commands to diagnose the issue
```

### Infrastructure as Code

Claude excels at reviewing and generating:
- Terraform configurations
- Kubernetes manifests
- Docker Compose files
- Ansible playbooks

```
> Review this Terraform file for AWS best practices
> Generate a Kubernetes deployment for a 3-replica web app
> Create a docker-compose.yml for local development
```

---

### Practice Exercise 4.3: SysAdmin Simulation

**Difficulty**: Hard
**XP Reward**: +25 XP

**Task**: Complete three system administration tasks:

1. **Log Analysis**: Share a log file (or create one) and ask Claude to analyze it
2. **Config Review**: Have Claude review a configuration file for issues
3. **Script Creation**: Have Claude generate a utility script for a task you do manually

**Success Criteria**: Completed all three tasks with actionable results.

- [ ] Completed

---

## Chapter 4: Automation and Scripting

### Building Automated Workflows

Combine Claude Code with shell scripting for powerful automation.

### Pattern: Quick Scripts

```bash
#!/bin/bash
# Generate changelog from git commits

commits=$(git log --oneline -20)
changelog=$(claude -p "Generate a changelog from these commits:\n$commits")
echo "$changelog" > CHANGELOG.md
```

### Pattern: Code Quality Pipeline

```bash
#!/bin/bash
# Pre-commit hook using Claude Code

# Get staged files
staged_files=$(git diff --cached --name-only --diff-filter=ACMR | grep -E '\.(py|js|ts)$')

for file in $staged_files; do
  review=$(claude -p "Quick security review of:\n$(cat $file)")
  if echo "$review" | grep -q "SECURITY ISSUE"; then
    echo "Security issue found in $file"
    echo "$review"
    exit 1
  fi
done
```

### Pattern: Documentation Generator

```bash
#!/bin/bash
# Auto-generate function documentation

for file in src/*.py; do
  echo "Processing $file..."
  claude -p "Generate docstrings for all functions in:\n$(cat $file)" > "${file%.py}_docs.md"
done
```

### Pattern: Error Monitor

```bash
#!/bin/bash
# Monitor logs and get AI analysis

tail -f /var/log/app/error.log | while read line; do
  if echo "$line" | grep -q "ERROR"; then
    analysis=$(claude -p "Analyze this error:\n$line")
    echo "$analysis" | mail -s "Error Analysis" admin@example.com
  fi
done
```

**Achievement Unlocked: Automation Architect** (+5 XP)

---

### Practice Exercise 4.4: Build an Automated Workflow

**Difficulty**: Hard
**XP Reward**: +25 XP

**Task**: Create a useful automated script that uses Claude Code:

Ideas:
- Commit message generator
- Code documentation generator
- Log analyzer
- Test case generator

Requirements:
1. Script uses `claude -p` for non-interactive AI calls
2. Script solves a real problem you have
3. Script is reusable (parameterized)

**Success Criteria**: Created a working automation script using Claude Code.

- [ ] Completed

---

## Chapter 5: Advanced Prompting Techniques

### Technique: Chain of Thought

Force Claude to reason step-by-step:

```
> Analyze this algorithm's time complexity.
> Think step by step:
> 1. Identify the loops
> 2. Determine iterations for each
> 3. Calculate nested complexity
> 4. Give the final Big O notation with explanation
```

### Technique: Role Playing

Assign Claude a specific perspective:

```
> Act as a senior security engineer.
> Review this authentication code.
> Focus on: OWASP Top 10, common attack vectors, best practices.
> Be critical - assume attackers will try to break this.
```

### Technique: Constraint Setting

Define output constraints:

```
> Refactor this function.
> Constraints:
> - No external dependencies
> - Must be backwards compatible
> - Maximum 30 lines
> - Include type hints
> - Add comprehensive error handling
```

### Technique: Few-Shot Examples

Provide examples of desired output:

```
> Generate API documentation.
>
> Example format:
> ## GET /users
> **Description**: Retrieves all users
> **Parameters**:
>   - page (int): Page number
> **Response**: JSON array of user objects
>
> Now document these endpoints:
> [your endpoints]
```

### Technique: Iterative Refinement

Build up through iterations:

```
Round 1: "Write a basic user class"
Round 2: "Add validation to the email field"
Round 3: "Add password hashing"
Round 4: "Add serialization methods"
Round 5: "Add comprehensive tests"
```

**Achievement Unlocked: Prompt Wizard** (+5 XP)

---

### Practice Exercise 4.5: Advanced Prompting

**Difficulty**: Medium
**XP Reward**: +20 XP

**Task**: Practice each advanced technique:

1. **Chain of Thought**: Have Claude analyze something step-by-step
2. **Role Playing**: Assign Claude a specific expert role
3. **Constraints**: Give Claude specific output constraints
4. **Few-Shot**: Provide examples for Claude to follow

**Success Criteria**: Used all four techniques and got improved results.

- [ ] Completed

---

## Chapter 6: Troubleshooting and Edge Cases

### Common Issues and Solutions

#### Issue: Claude Seems to Lose Context

**Symptoms**: Claude forgets earlier discussion, repeats questions

**Solutions**:
1. Use `/compact` to optimize context
2. Provide a summary of key points
3. Keep sessions focused on single topics
4. Use CLAUDE.md for persistent context

#### Issue: Responses Are Too Verbose

**Symptoms**: Long responses when you need quick answers

**Solutions**:
```
> Answer in 3 sentences or less
> Give me only the code, no explanation
> TL;DR version please
```

#### Issue: Code Suggestions Don't Work

**Symptoms**: Generated code has errors or doesn't fit your codebase

**Solutions**:
1. Provide more context about your environment
2. Share relevant existing code
3. Specify versions/frameworks explicitly
4. Ask Claude to explain assumptions

#### Issue: Claude Makes Unwanted File Changes

**Symptoms**: Unexpected modifications to files

**Solutions**:
1. Don't use `--dangerously-skip-permissions`
2. Use `/diff` before confirming changes
3. Use `/undo` to revert mistakes
4. Be specific about what should change

### Understanding Limitations

Claude Code cannot:
- Access the internet in real-time
- Run arbitrary code execution without permission
- Access files outside your working directory
- Remember across completely new sessions (use `-r`)
- Guarantee 100% accuracy (always verify critical code)

**Achievement Unlocked: Troubleshooter** (+5 XP)

---

## Chapter 7: Performance Optimization

### Optimizing Response Speed

#### 1. Use the Right Model

```bash
# Fast for simple queries
claude --model haiku -p "What's the syntax for Python f-strings?"

# Balanced for most work
claude --model sonnet

# Powerful for complex tasks (slower)
claude --model opus
```

#### 2. Be Concise in Prompts

```
Slow: "I was wondering if you could possibly help me understand
       what this code does, if you have time and it's not too
       much trouble..."

Fast: "Explain this code briefly: [code]"
```

#### 3. Batch Related Questions

```
Slow:
  > What is a decorator?
  > How do you use decorators?
  > Show me an example

Fast:
  > Explain decorators:
  > 1. What they are
  > 2. How to use them
  > 3. Give an example
```

### Optimizing Token Usage

Tokens = cost. Minimize unnecessary usage:

1. **Don't re-share unchanged files**
2. **Use /compact for long sessions**
3. **Be specific about what you need**
4. **Use Haiku for simple lookups**

---

## Level 4 Challenge: The Automation Architect

**Difficulty**: Hard
**XP Reward**: +35 XP

### The Scenario

Build a comprehensive automation system using Claude Code.

### Your Mission

Create a development automation suite with at least 3 scripts:

1. **Code Quality Script**:
   - Analyzes code for issues
   - Uses Claude for intelligent review
   - Outputs a report

2. **Documentation Script**:
   - Generates docs for a codebase
   - Uses appropriate model for the task
   - Creates readable output

3. **Helper Script**:
   - Solves a real problem in your workflow
   - Uses Claude Code automation
   - Is parameterized and reusable

### Deliverables

- [ ] 3 working scripts
- [ ] Documentation for each script
- [ ] Notes on model selection choices

---

## Level 4 Boss Battle: The Production Gauntlet

**Difficulty**: Very Hard
**XP Reward**: +75 XP

### The Ultimate Expert Challenge

Simulate a production incident response using Claude Code:

#### Phase 1: Incident Detection (20 points)
- [ ] Have Claude analyze a log file for anomalies
- [ ] Identify the severity of issues found
- [ ] Prioritize findings

#### Phase 2: Root Cause Analysis (25 points)
- [ ] Use chain-of-thought prompting for analysis
- [ ] Have Claude examine relevant code
- [ ] Document the likely root cause

#### Phase 3: Solution Implementation (25 points)
- [ ] Have Claude propose fixes
- [ ] Review the proposed changes carefully
- [ ] Implement using appropriate slash commands

#### Phase 4: Prevention (20 points)
- [ ] Generate tests that would catch this issue
- [ ] Create monitoring suggestions
- [ ] Document lessons learned

#### Phase 5: Documentation (10 points)
- [ ] Create an incident report with Claude's help
- [ ] Include timeline, cause, and resolution

### Victory Conditions

- [ ] Used at least 3 different models strategically
- [ ] Applied advanced prompting techniques
- [ ] Managed context effectively throughout
- [ ] Created reusable artifacts (scripts, docs)
- [ ] Demonstrated expert-level Claude Code usage

---

## Level 4 Summary

### New Skills Acquired

1. **Model Selection**: Strategic use of Opus/Sonnet/Haiku
2. **Context Management**: /compact, summarization, optimization
3. **System Administration**: Logs, configs, infrastructure
4. **Automation**: Shell scripts with Claude Code
5. **Advanced Prompting**: Chain of thought, roles, constraints, few-shot
6. **Troubleshooting**: Edge cases and limitations

### Command Reference Update

```bash
# Model Selection
claude --model opus     # Most capable
claude --model sonnet   # Balanced (default)
claude --model haiku    # Fast

# In-Session Model Switch
/model opus
/model sonnet
/model haiku

# Context Management
/compact                # Compress context

# Automation Pattern
claude -p "prompt"      # Non-interactive for scripts
```

---

## Level Completion Checklist

### Core Skills

- [ ] Can select and switch models strategically
- [ ] Manage context in long sessions
- [ ] Use Claude for system administration
- [ ] Build automated workflows
- [ ] Apply advanced prompting techniques
- [ ] Troubleshoot common issues

### Exercises Completed

- [ ] Exercise 4.1: Model Comparison (+15 XP)
- [ ] Exercise 4.2: Context Optimization (+15 XP)
- [ ] Exercise 4.3: SysAdmin Simulation (+25 XP)
- [ ] Exercise 4.4: Build an Automated Workflow (+25 XP)
- [ ] Exercise 4.5: Advanced Prompting (+20 XP)

### Challenges Completed

- [ ] The Automation Architect (+35 XP)
- [ ] Boss Battle: The Production Gauntlet (+75 XP)

### Achievements Earned

- [ ] Model Strategist (+5 XP)
- [ ] Context Commander (+5 XP)
- [ ] Automation Architect (+5 XP)
- [ ] Prompt Wizard (+5 XP)
- [ ] Troubleshooter (+5 XP)
- [ ] Expert Elite (+10 XP)

---

## XP Calculation

| Item | XP |
|------|-----|
| Reading Chapters (7 x 5 XP) | 35 |
| Exercises (5 total) | 100 |
| Challenge | 35 |
| Boss Battle | 75 |
| Achievements (6 total) | 35 |
| **Maximum Available** | **280** |
| **Required for Level 5** | **1000 total** |

---

## Ready for Level 5?

If your total XP is 1000 or more, you're ready for Master level!

**Your Current Progress**:
```
Level 4 Complete!
Level 4 XP Earned: ___ / 280 possible
Total XP: ___

[==========] MASTERY AWAITS!
```

[Continue to Level 5: Master -->](./05-LEVEL-MASTER.md)

---

## Power-Up Tips

**Easter Egg #5**: Pipe complex inputs to Claude:
```bash
git diff HEAD~5 | claude -p "Summarize all changes made in the last 5 commits"
```

**Easter Egg #6**: Use environment variables for defaults:
```bash
export ANTHROPIC_MODEL=opus
# Now Claude Code will use opus by default
```

---

*Level 4 Complete - You are now a Claude Code Expert!*

[<-- Level 3: Journeyman](./03-LEVEL-JOURNEYMAN.md) | [Level 5: Master -->](./05-LEVEL-MASTER.md)
