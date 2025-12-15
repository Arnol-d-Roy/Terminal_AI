
```
 ______________________________________________________________________
|                                                                      |
|   L E V E L   4 :   E X P E R T                                     |
|                                                                      |
|   Advanced Techniques and Power Features                             |
|                                                                      |
|   XP Range: 600-999  |  Status: ELITE TRAINING                      |
|                                                                      |
|______________________________________________________________________|
```

======================================================================
                        LEVEL OBJECTIVES
======================================================================

By the end of this level, you will:

- [ ] Master model selection and switching
- [ ] Leverage advanced context management
- [ ] Use Claude Code for system administration
- [ ] Create automated workflows
- [ ] Handle edge cases and troubleshooting
- [ ] Understand Claude Code's capabilities and limits

```
+--------------------------------+
|  Prerequisites: Level 1-3      |
|  (600+ XP)                     |
|  Estimated Time: 3-4 hours     |
|  XP Available: 360 XP          |
+--------------------------------+
```

----------------------------------------------------------------------


## Chapter 1: Model Selection and Optimization

### Understanding Model Options

Claude Code can use different models with varying capabilities:

```
+----------------+------------------------+---------------------------+
| Model          | Strengths              | Best For                  |
+----------------+------------------------+---------------------------+
| claude-3-opus  | Most capable,          | Complex analysis,         |
|                | thoughtful             | nuanced tasks             |
+----------------+------------------------+---------------------------+
| claude-3-sonnet| Balanced speed         | General development       |
|                | and capability         | work                      |
+----------------+------------------------+---------------------------+
| claude-3-haiku | Fast, efficient        | Quick queries,            |
|                |                        | simple tasks              |
+----------------+------------------------+---------------------------+
```


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

```
+----------------------------------------------------+
|  >>> ACHIEVEMENT UNLOCKED: Model Strategist        |
|      (+5 XP)                                       |
+----------------------------------------------------+
```

----------------------------------------------------------------------


### Practice Exercise 4.1: Model Comparison

```
+===========================================+
|  EXERCISE 4.1                             |
|-------------------------------------------|
|  Difficulty: Medium                       |
|  XP Reward: +15 XP                        |
+===========================================+
```

**Task**: Compare model responses on the same task:

  1. Start with: `claude --model haiku`
  2. Ask: "Explain the singleton pattern with pros and cons"
  3. Exit and try: `claude --model opus`
  4. Ask the same question
  5. Compare depth and nuance of responses

**Success Criteria**: Documented differences between model responses.

- [ ] Completed

----------------------------------------------------------------------


## Chapter 2: Advanced Context Management

### Understanding Context Windows

Claude has a "context window" - the amount of information it can
consider at once.

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

**Use when**: Session is slowing down or responses seem to lose
earlier context.

```
+----------------------------------------------------+
|  >>> ACHIEVEMENT UNLOCKED: Context Commander       |
|      (+5 XP)                                       |
+----------------------------------------------------+
```

----------------------------------------------------------------------


### Practice Exercise 4.2: Context Optimization

```
+===========================================+
|  EXERCISE 4.2                             |
|-------------------------------------------|
|  Difficulty: Medium                       |
|  XP Reward: +15 XP                        |
+===========================================+
```

**Task**: Practice context management:

  1. Start a session and have a long conversation (10+ exchanges)
  2. Ask Claude to summarize the key points
  3. Use `/compact` to optimize context
  4. Continue the conversation and verify context is preserved
  5. Practice selective file sharing

**Success Criteria**: Successfully managed a long session without
context loss.

- [ ] Completed

----------------------------------------------------------------------


## Chapter 3: System Administration Tasks

### Claude Code for DevOps

Claude Code isn't just for coding - it's powerful for system
administration.


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

  * Terraform configurations
  * Kubernetes manifests
  * Docker Compose files
  * Ansible playbooks

```
> Review this Terraform file for AWS best practices
> Generate a Kubernetes deployment for a 3-replica web app
> Create a docker-compose.yml for local development
```

----------------------------------------------------------------------


### Practice Exercise 4.3: SysAdmin Simulation

```
+===========================================+
|  EXERCISE 4.3                             |
|-------------------------------------------|
|  Difficulty: Hard                         |
|  XP Reward: +25 XP                        |
+===========================================+
```

**Task**: Complete three system administration tasks:

  1. **Log Analysis**: Share a log file (or create one) and ask
     Claude to analyze it
  2. **Config Review**: Have Claude review a configuration file
     for issues
  3. **Script Creation**: Have Claude generate a utility script
     for a task you do manually

**Success Criteria**: Completed all three tasks with actionable
results.

- [ ] Completed

----------------------------------------------------------------------


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
staged_files=$(git diff --cached --name-only --diff-filter=ACMR \
  | grep -E '\.(py|js|ts)$')

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
  claude -p "Generate docstrings for all functions in:\n$(cat $file)" \
    > "${file%.py}_docs.md"
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

```
+----------------------------------------------------+
|  >>> ACHIEVEMENT UNLOCKED: Automation Architect    |
|      (+5 XP)                                       |
+----------------------------------------------------+
```

----------------------------------------------------------------------


### Practice Exercise 4.4: Build an Automated Workflow

```
+===========================================+
|  EXERCISE 4.4                             |
|-------------------------------------------|
|  Difficulty: Hard                         |
|  XP Reward: +25 XP                        |
+===========================================+
```

**Task**: Create a useful automated script that uses Claude Code:

**Ideas**:
  * Commit message generator
  * Code documentation generator
  * Log analyzer
  * Test case generator

**Requirements**:

  1. Script uses `claude -p` for non-interactive AI calls
  2. Script solves a real problem you have
  3. Script is reusable (parameterized)

**Success Criteria**: Created a working automation script using
Claude Code.

- [ ] Completed

----------------------------------------------------------------------


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

```
+----------------------------------------------------+
|  >>> ACHIEVEMENT UNLOCKED: Prompt Wizard (+5 XP)   |
+----------------------------------------------------+
```

----------------------------------------------------------------------


### Practice Exercise 4.5: Advanced Prompting

```
+===========================================+
|  EXERCISE 4.5                             |
|-------------------------------------------|
|  Difficulty: Medium                       |
|  XP Reward: +20 XP                        |
+===========================================+
```

**Task**: Practice each advanced technique:

  1. **Chain of Thought**: Have Claude analyze something step-by-step
  2. **Role Playing**: Assign Claude a specific expert role
  3. **Constraints**: Give Claude specific output constraints
  4. **Few-Shot**: Provide examples for Claude to follow

**Success Criteria**: Used all four techniques and got improved
results.

- [ ] Completed

----------------------------------------------------------------------


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

  * Access the internet in real-time
  * Run arbitrary code execution without permission
  * Access files outside your working directory
  * Remember across completely new sessions (use `-r`)
  * Guarantee 100% accuracy (always verify critical code)

```
+----------------------------------------------------+
|  >>> ACHIEVEMENT UNLOCKED: Troubleshooter (+5 XP)  |
+----------------------------------------------------+
```

----------------------------------------------------------------------


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

----------------------------------------------------------------------


## Chapter 8: Working with Agents

### Understanding the Agent System

Claude Code includes a powerful **Agent system** that allows Claude
to delegate complex, multi-step tasks to specialized sub-agents.

```
+--------------------------------------------------------------+
|  AGENT SYSTEM: PARALLEL TASK EXECUTION                       |
|--------------------------------------------------------------|
|                                                              |
|   Main Claude  -->  Agent 1: Code Analysis                   |
|       |        -->  Agent 2: Documentation Search            |
|       |        -->  Agent 3: Test Generation                 |
|       v                                                      |
|   Continues working while agents run in background           |
|                                                              |
+--------------------------------------------------------------+
```


### What Agents Do

Agents handle tasks that would otherwise interrupt your workflow:

  * **Deep code exploration** - Search through large codebases
  * **Background research** - Fetch documentation while you work
  * **Parallel analysis** - Investigate multiple files simultaneously
  * **Specialized operations** - Code reviews, test generation, etc.


### When Agents Are Used

Agents activate automatically when Claude Code determines a task
would benefit from background processing:

```
Scenario                    Agent Usage
---------------------------------------
"Find all API endpoints"    YES - Explore agent
"Explain this function"     NO  - Direct response
"Audit security issues"     YES - Multiple agents
"Fix this typo"             NO  - Simple edit
```


### Agent Types

```
+-------------------+--------------------------------------------+
| Agent Type        | Purpose                                    |
+-------------------+--------------------------------------------+
| Explore           | Fast codebase exploration and search      |
| Plan              | Design implementation strategies          |
| General-Purpose   | Complex multi-step research tasks         |
| Specialized       | Domain-specific operations                |
+-------------------+--------------------------------------------+
```


### Working with Agents

#### How to Trigger Agents

You don't manually invoke agents - Claude Code decides when to use
them based on your request:

```bash
# This might trigger an explore agent:
claude
> Find all database query functions in this project

# This might trigger multiple agents:
> Analyze security vulnerabilities across the codebase
```


#### Monitoring Agent Progress

When agents run, you'll see status updates:

```
🤖 Spawning explore agent to search codebase...
⚡ Agent searching: src/**/*.py
✓ Agent complete: Found 47 query functions
```


#### Agent Limitations

Agents are powerful but have constraints:

  * **No file modifications** - Agents only read and analyze
  * **Background only** - They don't interact with you directly
  * **Resource limits** - Maximum concurrent agents
  * **Scope boundaries** - Each agent has specific capabilities


### Best Practices for Agent-Heavy Workflows

```
+----------------------------------------------------+
|  DO's                      |  DON'Ts               |
+----------------------------+---------------------- +
|  ✓ Let Claude decide       |  ✗ Try to force agents|
|  ✓ Provide clear scope     |  ✗ Expect instant     |
|  ✓ Be patient with large   |      results          |
|      codebases             |  ✗ Interrupt agents   |
|  ✓ Trust agent results     |      mid-execution    |
+----------------------------+-----------------------+
```


### Real-World Agent Scenarios

#### Scenario 1: Comprehensive Code Audit

```bash
claude
> Audit this codebase for:
> - Security vulnerabilities
> - Performance bottlenecks
> - Code quality issues
> - Missing tests

# Claude spawns multiple agents:
🤖 Agent 1: Security scan
🤖 Agent 2: Performance analysis
🤖 Agent 3: Quality metrics
🤖 Agent 4: Test coverage
```


#### Scenario 2: Large Codebase Navigation

```bash
> Where is authentication handled in this project?

# Explore agent searches efficiently:
⚡ Searching: src/**/*.{js,ts,py}
⚡ Found: 12 auth-related files
✓ Analysis complete
```


### Understanding Agent Output

Agents provide structured results:

```
AGENT REPORT: Code Exploration
-------------------------------
Files Scanned: 234
Matches Found: 47
Time Elapsed: 3.2s

Key Findings:
- src/auth/login.py: OAuth implementation
- src/middleware/auth.js: JWT validation
- config/security.yaml: Auth configuration
```


### Advanced: Agent Coordination

For complex tasks, multiple agents may coordinate:

```
Task: "Prepare production deployment checklist"

Main Claude:
  ├── Agent 1: Check test coverage
  ├── Agent 2: Review recent changes
  ├── Agent 3: Audit dependencies
  └── Agent 4: Verify configurations

Result: Comprehensive deployment report
```


### Agent System Benefits

```
+---------------------------------------------+
|  WITHOUT AGENTS      |  WITH AGENTS         |
+----------------------+----------------------+
|  Sequential search   |  Parallel search     |
|  Single file focus   |  Multi-file analysis |
|  Manual navigation   |  Automatic discovery |
|  Time: Minutes       |  Time: Seconds       |
+----------------------+----------------------+
```

```
+----------------------------------------------------+
|  >>> ACHIEVEMENT UNLOCKED: Agent Commander (+10 XP)|
+----------------------------------------------------+
```

----------------------------------------------------------------------


## Chapter 9: MCP (Model Context Protocol)

### What is MCP?

**Model Context Protocol** is a standardized way for Claude Code to
connect to external tools, databases, and services - extending its
capabilities far beyond built-in features.

```
 ______________________________________________________________________
|                                                                      |
|   Claude Code  <-->  MCP Protocol  <-->  External Tools             |
|                                                                      |
|   Built-in          Standard           - Databases                  |
|   Features          Interface          - APIs                       |
|                                        - File Systems               |
|                                        - Custom Tools               |
|______________________________________________________________________|
```


### Why MCP Matters

MCP transforms Claude Code from a standalone tool into an integration
platform:

  * **Database Access** - Query databases directly
  * **API Integration** - Connect to web services
  * **Custom Tools** - Build your own integrations
  * **Enterprise Systems** - Connect to internal platforms


### MCP Architecture

```
+-----------------------------------------------------------+
|  YOUR WORKFLOW                                             |
|-----------------------------------------------------------|
|                                                           |
|  You: "Query the production database for user stats"     |
|                                                           |
|  Claude Code:                                             |
|    1. Understands request                                 |
|    2. Calls MCP Database Server                           |
|    3. Formats results                                     |
|    4. Presents insights                                   |
|                                                           |
+-----------------------------------------------------------+
```


### Available MCP Servers

Common MCP integrations:

```
+--------------------+---------------------------------------+
| MCP Server         | Capabilities                          |
+--------------------+---------------------------------------+
| File System        | Extended file operations              |
| Database           | PostgreSQL, MySQL, MongoDB            |
| GitHub             | Repos, PRs, Issues, Actions           |
| Web Fetch          | HTTP requests, web scraping           |
| Slack              | Messages, channels, notifications     |
| Google Drive       | Docs, Sheets, Drive access            |
| Custom             | Your own integrations                 |
+--------------------+---------------------------------------+
```


### Configuring MCP

MCP servers are configured in your Claude Code settings:

#### Configuration Location

```bash
# Settings file location
~/.config/claude-code/mcp-servers.json
```


#### Example Configuration

```json
{
  "mcpServers": {
    "database": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres"],
      "env": {
        "POSTGRES_URL": "postgresql://localhost/mydb"
      }
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "your-token-here"
      }
    }
  }
}
```


### Using MCP Tools

Once configured, MCP tools are available transparently:

#### Example 1: Database Queries

```bash
claude
> Query the users table for accounts created this week

# Claude automatically uses MCP database server:
SELECT * FROM users
WHERE created_at >= NOW() - INTERVAL '7 days';

Results: 42 new users this week
```


#### Example 2: GitHub Integration

```bash
> Show me all open pull requests in this repo

# MCP GitHub server called automatically:
Found 7 open PRs:
1. #234: Add dark mode (3 days old)
2. #235: Fix auth bug (1 day old)
...
```


#### Example 3: Web Fetching

```bash
> Fetch the latest docs for React Hooks

# MCP Web Fetch server retrieves and analyzes:
📄 Retrieved: react.dev/reference/hooks
📊 Analyzing content...
✓ Here's a summary of React Hooks...
```


### Building Custom MCP Servers

Create your own integrations:

```python
# custom-mcp-server.py
from mcp import Server

server = Server("my-custom-tool")

@server.tool()
def analyze_metrics(date_range):
    """Fetch and analyze custom metrics"""
    # Your custom logic here
    return results

server.run()
```


### MCP Best Practices

```
+------------------------------------------------------------+
|  DO's                           |  DON'Ts                  |
+---------------------------------+--------------------------+
|  ✓ Secure credentials properly  |  ✗ Hardcode tokens       |
|  ✓ Test integrations thoroughly |  ✗ Expose sensitive data |
|  ✓ Handle errors gracefully     |  ✗ Skip error handling   |
|  ✓ Document custom servers      |  ✗ Assume always online  |
+---------------------------------+--------------------------+
```


### Common MCP Workflows

#### Workflow 1: Database-Driven Development

```
1. Query database with MCP
   > "Show recent error logs from production DB"

2. Analyze patterns
   > "What's the most common error?"

3. Write fix
   > "Generate migration to add missing index"
```


#### Workflow 2: Documentation Research

```
1. Fetch latest docs via MCP Web Fetch
2. Ask questions about API changes
3. Update code based on new documentation
```


#### Workflow 3: GitHub Automation

```
1. Check PR status via MCP GitHub
2. Analyze code changes
3. Generate review comments
4. Update PR with suggestions
```


### MCP Security Considerations

```
+-----------------------------------------------------+
|  SECURITY CHECKLIST                                  |
|-----------------------------------------------------|
|  [ ] Store credentials in environment variables     |
|  [ ] Use read-only access when possible             |
|  [ ] Audit MCP server permissions                   |
|  [ ] Review MCP server source code                  |
|  [ ] Enable logging for debugging                   |
|  [ ] Rotate tokens regularly                        |
+-----------------------------------------------------+
```


### Troubleshooting MCP

Common issues and solutions:

```
Problem: "MCP server not found"
Solution: Check configuration path and server installation

Problem: "Authentication failed"
Solution: Verify environment variables and token validity

Problem: "Connection timeout"
Solution: Check network connectivity and server status
```

```
+----------------------------------------------------+
|  >>> ACHIEVEMENT UNLOCKED: Protocol Master (+15 XP)|
+----------------------------------------------------+
```

----------------------------------------------------------------------


## Chapter 10: Extended Thinking Mode

### What is Extended Thinking?

Extended Thinking is Claude's deep reasoning capability - when faced
with complex problems, Claude can "think through" the solution
step-by-step before responding.

```
+--------------------------------------------------------------+
|  NORMAL MODE              |  EXTENDED THINKING MODE         |
+---------------------------+---------------------------------+
|  Quick response           |  Deep analysis                  |
|  Surface-level            |  Multi-step reasoning           |
|  Fast                     |  Thorough                       |
|  Simple questions         |  Complex problems               |
+---------------------------+---------------------------------+
```


### When Extended Thinking Activates

Claude Code automatically uses extended thinking for:

  * **Complex debugging** - Multi-layered issues
  * **Architecture decisions** - System design choices
  * **Security analysis** - Vulnerability assessment
  * **Performance optimization** - Bottleneck identification
  * **Strategic planning** - Project roadmaps


### How It Works

```
Your Request: "Why is this algorithm slow?"

Extended Thinking Process:
┌─────────────────────────────────────┐
│ 1. Analyze algorithm complexity     │
│ 2. Check data structure choices     │
│ 3. Examine loop nesting             │
│ 4. Consider memory allocation       │
│ 5. Review edge cases                │
│ 6. Synthesize findings              │
└─────────────────────────────────────┘
        ↓
Comprehensive Answer
```


### Recognizing Extended Thinking

You'll see indicators when Claude engages extended thinking:

```
🧠 Analyzing architectural implications...
🔍 Considering multiple solution paths...
⚙️ Reasoning through edge cases...
```


### Encouraging Deep Reasoning

Frame requests to trigger extended thinking:

```
Instead of:              Try:
------------------      ------------------------------------
"Fix this bug"          "Analyze why this bug occurs and
                         suggest the most robust fix"

"Optimize this"         "What are all the performance
                         bottlenecks and how should we
                         prioritize fixing them?"

"Review this PR"        "Conduct a thorough code review
                         considering security, performance,
                         and maintainability"
```


### Extended Thinking in Action

#### Example: Complex Debugging

```bash
claude
> This service is failing intermittently. The logs show timeout
> errors but only under high load. What's really happening?

🧠 Engaging extended thinking...

Analysis:
1. Symptom Pattern: Failures only under load suggest resource
   contention rather than logic error

2. Timeout Location: Reviewing code... database queries lack
   connection pooling

3. Load Behavior: High concurrency exhausts available connections

4. Root Cause: Connection pool size (10) insufficient for
   expected load (100+ concurrent requests)

5. Solution Path: Increase pool size AND implement connection
   retry logic for resilience

Recommendation: [detailed fix with code]
```


### When to Use Extended Thinking

```
+------------------------------------------------------------+
|  GOOD FOR                   |  OVERKILL FOR               |
+-----------------------------+-----------------------------+
|  Architecture decisions     |  Syntax questions           |
|  Root cause analysis        |  Quick lookups              |
|  Security audits            |  Simple refactoring         |
|  System design              |  Typo fixes                 |
|  Complex debugging          |  Basic explanations         |
+-----------------------------+-----------------------------+
```


### Token Implications

Extended thinking uses more tokens:

```
Simple Query:           ~500 tokens
Extended Thinking:      ~2000-5000 tokens

Cost Difference:        4-10x higher

Worth it when:
  ✓ Decision is critical
  ✓ Error cost is high
  ✓ Need comprehensive analysis
```


### Maximizing Extended Thinking Value

Tips for getting the best results:

  1. **Provide context** - Share relevant background
  2. **Ask open-ended questions** - Allow exploration
  3. **Request reasoning** - "Explain your thinking"
  4. **Challenge assumptions** - "What could go wrong?"


```
+--------------------------------------------------------+
|  >>> ACHIEVEMENT UNLOCKED: Deep Thinker (+10 XP)       |
+--------------------------------------------------------+
```

----------------------------------------------------------------------


## Chapter 11: Error Handling and Recovery

### Understanding Claude Code Errors

Errors happen. Here's how to handle them effectively:

```
+-----------------------------------------------------------+
|  ERROR CATEGORIES                                          |
|-----------------------------------------------------------|
|  1. API Errors        - Rate limits, connectivity         |
|  2. Input Errors      - Malformed requests                |
|  3. Tool Errors       - MCP, file access issues           |
|  4. Model Errors      - Context limits, timeouts          |
+-----------------------------------------------------------+
```


### Common Error Types

#### API Rate Limiting

```
Error: "Rate limit exceeded. Retry after 60 seconds"

Cause: Too many requests too quickly
Solution: Wait and retry, or implement backoff
```


#### Context Length Errors

```
Error: "Input exceeds maximum context length"

Cause: Too much text in conversation
Solution: Use /compact or start fresh session
```


#### Connection Failures

```
Error: "Failed to connect to API"

Cause: Network issues or API downtime
Solution: Check connection, wait and retry
```


### Error Recovery Strategies

#### 1. Automatic Retry with Backoff

```bash
# Build retry logic into scripts:
for i in {1..3}; do
  if claude -p "Your query" 2>/dev/null; then
    break
  else
    echo "Retry $i..."
    sleep $((i * 2))
  fi
done
```


#### 2. Graceful Degradation

```bash
# Try opus, fall back to sonnet if rate-limited:
claude --model opus -p "Complex task" || \
claude --model sonnet -p "Complex task"
```


#### 3. Context Management

```
When you see context errors:
1. Run /compact to summarize
2. Or start new session with /exit
3. Reference previous session if needed
```


### Debugging Error Messages

```
+------------------------------------------------------+
|  ERROR DEBUGGING CHECKLIST                            |
|------------------------------------------------------|
|  [ ] Read the full error message                     |
|  [ ] Check API key validity                          |
|  [ ] Verify network connectivity                     |
|  [ ] Review recent changes to config                 |
|  [ ] Check Claude Code version                       |
|  [ ] Look for error logs                             |
+------------------------------------------------------+
```


### Production-Ready Error Handling

For automated scripts:

```bash
#!/bin/bash
set -e  # Exit on error

# Trap errors
trap 'echo "Error on line $LINENO"' ERR

# Validate before running
if [ -z "$ANTHROPIC_API_KEY" ]; then
  echo "Error: API key not set"
  exit 1
fi

# Run with error checking
if ! output=$(claude -p "Query" 2>&1); then
  echo "Claude failed: $output"
  # Send alert, log error, etc.
  exit 1
fi
```


### Logging for Debugging

Enable detailed logging:

```bash
# Set debug mode
export CLAUDE_DEBUG=1

# Now Claude Code logs verbose output
claude -p "Test query"

# Review logs
cat ~/.config/claude-code/logs/latest.log
```


```
+----------------------------------------------------+
|  >>> ACHIEVEMENT UNLOCKED: Error Handler (+10 XP)  |
+----------------------------------------------------+
```

----------------------------------------------------------------------


## Chapter 12: Jupyter Notebook Integration

### Working with Notebooks

Claude Code can read and edit Jupyter notebooks (.ipynb files),
making it perfect for data science workflows.

```
+-----------------------------------------------------+
|  NOTEBOOK CAPABILITIES                               |
|-----------------------------------------------------|
|  ✓ Read notebook cells                              |
|  ✓ Edit code cells                                  |
|  ✓ Edit markdown cells                              |
|  ✓ Analyze outputs                                  |
|  ✓ Review visualizations                            |
|  ✓ Debug data pipelines                             |
+-----------------------------------------------------+
```


### Reading Notebooks

```bash
claude
> Read the notebook analysis.ipynb and summarize what it does

# Claude analyzes:
📓 Notebook: analysis.ipynb
Cells: 47 (32 code, 15 markdown)

Summary:
- Data loading from CSV
- Exploratory data analysis
- Feature engineering
- Model training (Random Forest)
- Results visualization
```


### Editing Notebook Cells

Claude can modify specific cells:

```bash
> Edit cell 5 in analysis.ipynb to use pandas instead of numpy

✓ Updated cell 5:
  Before: import numpy as np
  After:  import pandas as pd
```


### Notebook Analysis Workflows

#### Workflow 1: Debug a Failed Notebook

```
> This notebook fails at cell 23. Why?

🔍 Analyzing notebook...
📊 Examining cell 23 and dependencies...

Issue found: Cell 23 references 'df_clean' but cell 15
(where it's created) has a typo: 'df_clen'

Fix: Update cell 15 variable name
```


#### Workflow 2: Optimize Data Pipeline

```
> Review this notebook for performance issues

Analysis of all cells:
- Cell 8: Using .iterrows() - very slow
  → Recommend: Vectorized operations

- Cell 12: Loading full dataset each time
  → Recommend: Cache intermediate results

- Cell 19: Nested loops
  → Recommend: Use pandas .apply()
```


#### Workflow 3: Generate Documentation

```
> Add markdown documentation to this notebook

✓ Added documentation cells:
  - Overview before cell 1
  - Section headers before major steps
  - Explanation of key transformations
  - Results interpretation
```


### Best Practices for Notebook Work

```
+-----------------------------------------------------------+
|  DO's                          |  DON'Ts                  |
+--------------------------------+--------------------------+
|  ✓ Keep notebooks organized    |  ✗ Huge monolithic       |
|  ✓ Clear cell outputs before   |     notebooks            |
|     committing                 |  ✗ Hidden dependencies   |
|  ✓ Document complex cells      |  ✗ Out-of-order execution|
|  ✓ Use cell numbers in         |  ✗ Uncommitted changes   |
|     discussions                |                          |
+--------------------------------+--------------------------+
```


### Notebook + MCP Integration

Combine notebooks with MCP for powerful workflows:

```bash
> Query the production database and create a visualization
> notebook

# Claude:
1. Uses MCP to query database
2. Creates new notebook
3. Adds data loading cell
4. Adds visualization code
5. Runs analysis

✓ Created: production_stats.ipynb
```

```
+--------------------------------------------------------+
|  >>> ACHIEVEMENT UNLOCKED: Data Scientist (+10 XP)     |
+--------------------------------------------------------+
```

----------------------------------------------------------------------


## Chapter 13: Hooks - Customizing Claude Code Behavior

### What Are Hooks?

Hooks are **user-defined shell commands** that execute automatically
at specific points in Claude Code's lifecycle, giving you
deterministic control over its behavior.

```
 ______________________________________________________________________
|                                                                      |
|   HOOKS: AUTOMATE THE AUTOMATOR                                     |
|                                                                      |
|   Instead of hoping Claude remembers to run tests,                  |
|   hooks GUARANTEE it happens every time.                            |
|                                                                      |
|______________________________________________________________________|
```


### Why Hooks Matter

```
+--------------------------------------------------------------+
|  WITHOUT HOOKS              |  WITH HOOKS                    |
+-----------------------------+--------------------------------+
|  "Please run tests"         |  Tests run automatically       |
|  "Don't forget to format"   |  Auto-formatted on every edit  |
|  "Remember to check lint"   |  Linting happens always        |
|  Relies on LLM memory       |  Deterministic automation      |
+-----------------------------+--------------------------------+
```


### Hook Events

Claude Code provides several lifecycle events:

```
+------------------+-----------------------------------------------+
| Hook Event       | When It Fires                                 |
+------------------+-----------------------------------------------+
| PreToolUse       | Before Claude executes any tool               |
| PostToolUse      | After a tool execution completes              |
| SessionStart     | When Claude Code session begins               |
| SessionEnd       | When session ends                             |
| UserPromptSubmit | Before processing user input                  |
+------------------+-----------------------------------------------+
```


### Creating Your First Hook

Hooks live in `.claude/hooks/` directory:

```bash
# Create hooks directory
mkdir -p .claude/hooks

# Create a hook file
touch .claude/hooks/post-file-edit.sh
chmod +x .claude/hooks/post-file-edit.sh
```


### Example: Auto-Format After Edits

```bash
#!/bin/bash
# .claude/hooks/post-file-edit.sh

# Get the file that was edited
FILE="$1"

# Auto-format based on file type
case "$FILE" in
  *.ts|*.tsx|*.js|*.jsx)
    prettier --write "$FILE"
    echo "✓ Formatted: $FILE"
    ;;
  *.go)
    gofmt -w "$FILE"
    echo "✓ Formatted: $FILE"
    ;;
  *.py)
    black "$FILE"
    echo "✓ Formatted: $FILE"
    ;;
esac
```


### Example: Run Tests After Code Changes

```bash
#!/bin/bash
# .claude/hooks/post-tool-use.sh

TOOL_NAME="$1"
RESULT="$2"

# If a file was edited, run tests
if [ "$TOOL_NAME" = "edit_file" ]; then
  echo "Running tests..."
  npm test

  if [ $? -eq 0 ]; then
    echo "✅ Tests passed"
  else
    echo "❌ Tests failed - consider reverting"
    exit 1  # This will show Claude the failure
  fi
fi
```


### Example: Block Production Changes

```bash
#!/bin/bash
# .claude/hooks/pre-tool-use.sh

TOOL_NAME="$1"
FILE="$2"

# Block any edits to production config
if [[ "$TOOL_NAME" == "edit_file" ]] && [[ "$FILE" == *"production"* ]]; then
  echo "🚫 BLOCKED: Cannot modify production files!"
  echo "   File: $FILE"
  exit 1  # Exit code 1 blocks the action
fi

# Allow other actions
exit 0
```


### Hook Configuration

Configure hooks in `.claude/settings.json`:

```json
{
  "hooks": {
    "enabled": true,
    "preToolUse": ".claude/hooks/pre-tool-use.sh",
    "postToolUse": ".claude/hooks/post-tool-use.sh",
    "sessionStart": ".claude/hooks/session-start.sh",
    "sessionEnd": ".claude/hooks/session-end.sh"
  }
}
```


### Advanced: Conditional Hook Execution

```bash
#!/bin/bash
# .claude/hooks/smart-test.sh

TOOL_NAME="$1"
FILE="$2"

# Only run tests for source files, not tests themselves
if [[ "$FILE" == *"test"* ]]; then
  echo "Skipping tests for test file"
  exit 0
fi

# Only run affected tests
if [[ "$FILE" == "src/auth/"* ]]; then
  npm test -- auth
elif [[ "$FILE" == "src/api/"* ]]; then
  npm test -- api
else
  npm test
fi
```


### Hook Data Available

Each hook receives different data:

```
PreToolUse Hook:
  $1 = Tool name (e.g., "edit_file", "bash")
  $2 = Tool arguments
  Exit 0 = Allow
  Exit 1 = Block

PostToolUse Hook:
  $1 = Tool name
  $2 = Tool result
  $3 = Success/failure status

SessionStart Hook:
  $CLAUDE_PROJECT_DIR = Project directory
  $CLAUDE_MODEL = Model being used

SessionEnd Hook:
  $CLAUDE_SESSION_DURATION = Session length
  $CLAUDE_TOOLS_USED = Number of tools called
```


### Real-World Hook Workflows

#### Workflow 1: Compliance Logging

```bash
#!/bin/bash
# .claude/hooks/audit-log.sh

TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
TOOL="$1"
ACTION="$2"

# Log all actions for compliance
echo "$TIMESTAMP | $USER | $TOOL | $ACTION" >> ~/.claude-audit.log

# If sensitive operation, notify
if [[ "$TOOL" == "bash" ]] && [[ "$ACTION" == *"rm -rf"* ]]; then
  notify-send "⚠️ Claude Code" "Destructive command executed"
fi
```


#### Workflow 2: Code Quality Gates

```bash
#!/bin/bash
# .claude/hooks/quality-gate.sh

FILE="$1"

# Run linter
if ! eslint "$FILE"; then
  echo "❌ Linting failed - fix errors first"
  exit 1
fi

# Check for TODOs in production code
if [[ "$FILE" != *"test"* ]] && grep -q "TODO" "$FILE"; then
  echo "⚠️  Warning: TODO found in production code"
fi

# Check for console.log
if grep -q "console.log" "$FILE"; then
  echo "⚠️  Warning: console.log found - remove before commit"
fi

exit 0
```


#### Workflow 3: Automatic Git Integration

```bash
#!/bin/bash
# .claude/hooks/auto-stage.sh

TOOL="$1"
FILE="$2"

# Auto-stage files after edits
if [ "$TOOL" = "edit_file" ]; then
  git add "$FILE"
  echo "✓ Staged: $FILE"
fi
```


### Hook Best Practices

```
+-----------------------------------------------------------+
| DO's                            | DON'Ts                  |
+---------------------------------+-------------------------+
| ✓ Keep hooks fast (<1 second)  | ✗ Long-running processes|
| ✓ Provide clear output          | ✗ Silent failures       |
| ✓ Exit with proper codes        | ✗ Ignore exit codes     |
|   (0=success, 1=block)          |                         |
| ✓ Make hooks idempotent         | ✗ Assume clean state    |
| ✓ Log important actions         | ✗ Modify without logging|
| ✓ Version control hooks         | ✗ Keep hooks local only |
| ✓ Test hooks independently      | ✗ Only test via Claude  |
+---------------------------------+-------------------------+
```


### Debugging Hooks

Enable debug mode:

```bash
# Run Claude Code with hook debugging
CLAUDE_DEBUG_HOOKS=1 claude

# Output shows:
🔧 Hook: PreToolUse fired
   Tool: edit_file
   File: src/main.py
   Exit: 0 (allowed)
```


### Team Hooks vs Personal Hooks

```
Team Hooks (version controlled):
  .claude/hooks/           # Committed to git
  - Shared formatting
  - Linting standards
  - Test requirements

Personal Hooks (local):
  ~/.claude/hooks/         # Not in git
  - Personal notifications
  - Local tool integrations
  - Custom workflows
```


### Performance Optimization

```bash
#!/bin/bash
# .claude/hooks/optimized-test.sh

# Use file watching instead of running tests every time
if [ -f .tests-running ]; then
  echo "Tests already running, skipping..."
  exit 0
fi

touch .tests-running
npm test
rm .tests-running
```


### Hook Ecosystem

Common hook patterns shared by community:

```
Popular Hooks:
  - Auto-formatting (prettier, black, gofmt)
  - Linting enforcement (eslint, pylint, golangci-lint)
  - Test runners (jest, pytest, go test)
  - Security scanners (bandit, gosec, semgrep)
  - Documentation generators (jsdoc, sphinx)
  - Notification systems (Slack, email, desktop)
  - Metrics tracking (time, tokens, files changed)
```


### Advanced: Multi-Stage Hooks

```bash
#!/bin/bash
# .claude/hooks/multi-stage.sh

STAGE="${CLAUDE_HOOK_STAGE:-pre}"

case "$STAGE" in
  pre)
    # Pre-checks
    echo "Running pre-checks..."
    ;;
  post)
    # Post-actions
    echo "Running post-actions..."
    ;;
  validate)
    # Validation
    echo "Validating..."
    ;;
esac
```


### Disabling Hooks Temporarily

```bash
# Skip hooks for this session
claude --no-hooks

# Or disable specific hook type
export CLAUDE_SKIP_PRETOOLUSE=1
claude
```

```
+----------------------------------------------------+
|  >>> ACHIEVEMENT UNLOCKED: Hook Master (+15 XP)    |
+----------------------------------------------------+
```

----------------------------------------------------------------------


## Level 4 Challenge: The Automation Architect

```
+======================================================================+
|  CHALLENGE: THE AUTOMATION ARCHITECT                                 |
|----------------------------------------------------------------------|
|  Difficulty: Hard                                                    |
|  XP Reward: +35 XP                                                   |
+======================================================================+
```

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

----------------------------------------------------------------------


## Level 4 Boss Battle: The Production Gauntlet

```
+======================================================================+
|                                                                      |
|  *** BOSS BATTLE: THE PRODUCTION GAUNTLET ***                        |
|                                                                      |
|----------------------------------------------------------------------|
|  Difficulty: Very Hard                                               |
|  XP Reward: +75 XP                                                   |
+======================================================================+
```

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

----------------------------------------------------------------------


## Level 4 Summary

### New Skills Acquired

  1. **Model Selection**: Strategic use of Opus/Sonnet/Haiku
  2. **Context Management**: /compact, summarization, optimization
  3. **System Administration**: Logs, configs, infrastructure
  4. **Automation**: Shell scripts with Claude Code
  5. **Advanced Prompting**: Chain of thought, roles, constraints
  6. **Troubleshooting**: Edge cases and limitations


### Command Reference Update

```
+----------------------------------+----------------------------------+
|  Model Selection                 |  Context Management              |
+----------------------------------+----------------------------------+
|  claude --model opus             |  /compact  # Compress context    |
|  claude --model sonnet           |                                  |
|  claude --model haiku            |  Automation Pattern:             |
|                                  |  claude -p "prompt"              |
|  In-Session Switch:              |  (Non-interactive for scripts)   |
|  /model opus                     |                                  |
|  /model sonnet                   |                                  |
|  /model haiku                    |                                  |
+----------------------------------+----------------------------------+
```

----------------------------------------------------------------------


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

----------------------------------------------------------------------


## XP Calculation

```
+----------------------------------+---------+
| Item                             | XP      |
+----------------------------------+---------+
| Reading Chapters (12 x 5 XP)     | 60      |
| Exercises (5 total)              | 100     |
| Challenge                        | 35      |
| Boss Battle                      | 75      |
| Achievements (11 total)          | 90      |
+----------------------------------+---------+
| MAXIMUM AVAILABLE                | 360     |
| Required for Level 5             | 1000    |
+----------------------------------+---------+
```

----------------------------------------------------------------------


## Ready for Level 5?

If your total XP (Levels 1-4) is 1000 or more, you're ready for
Master level!

```
+============================================================+
|  Level 4 Complete!                                         |
|  Level 4 XP Earned: ___ / 360 possible                     |
|  New Total: ___ XP                                         |
|                                                            |
|  [==========] MASTERY AWAITS!                              |
+============================================================+
```

  --> Continue to Level 5: Master (05-LEVEL-MASTER.md)

----------------------------------------------------------------------


## Power-Up Tips

```
+============================================================+
|  EASTER EGG #5: Pipe complex inputs to Claude:             |
|                                                            |
|  git diff HEAD~5 | claude -p "Summarize all changes        |
|                              made in the last 5 commits"   |
+============================================================+

+============================================================+
|  EASTER EGG #6: Use environment variables for defaults:    |
|                                                            |
|  export ANTHROPIC_MODEL=opus                               |
|  # Now Claude Code will use opus by default                |
+============================================================+
```

======================================================================
  Level 4 Complete - You are now a Claude Code Expert!
======================================================================

  <-- Level 3: Journeyman (03-LEVEL-JOURNEYMAN.md)
  --> Level 5: Master (05-LEVEL-MASTER.md)
