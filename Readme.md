# Coffee Project: Agentic AI Development Guide

## Overview
This project is designed to be built and maintained using **Agentic AI** workflows. By leveraging advanced AI agents like **Claude** and **Gemini** directly in the terminal, we streamline coding, debugging, and documentation tasks.

This README serves as the central guide for setting up your environment and effectively collaborating with these AI agents.

## 🚀 Environment Setup

### 1. Windows Subsystem for Linux (WSL)
The development environment relies on WSL (Ubuntu) to ensure compatibility with linux-based AI tools and scripts.

*   **Launch Ubuntu**:
    Open your Windows command prompt or PowerShell and run:
    ```bash
    wsl -d ubuntu
    ```
    *This enters the Linux subsystem where the project lives.*

### 2. AI Tools Installation
Ensure you have the necessary CLI tools installed and authenticated.

*   **Claude Code**: typically installed via npm (`npm install -g @anthropic-ai/claude-code`) or a specific setup script.
*   **Gemini CLI**: verify your installation of the Google Gemini command-line interface.

---

## 🤖 Agentic AI Tools

### 1. Claude (`claude`)
**Role:** The "Engineer" Agent.
`claude` is an autonomous coding agent capable of editing files, running commands, and managing the git workflow.

**Basic Commands:**
*   **Interactive Session**:
    ```bash
    claude
    ```
    *Starts a conversational loop where Claude acts as a pair programmer.*

*   **Direct Instruction**:
    ```bash
    claude "Create a new file called coffee.py with a Coffee class"
    ```

*   **Review Changes**:
    Claude will often propose file edits. It will show a diff before applying.
    *   Type `y` to accept changes.
    *   Type `n` to reject.

**Agentic Capabilities:**
*   **Context Awareness**: Claude scans the current directory to understand the project structure.
*   **Task Execution**: You can give high-level goals like "Refactor the brewing logic to be thread-safe" and it will plan and execute the steps.
*   **Debugging**: Pipe error logs to Claude: `npm test 2>&1 | claude "Fix these failing tests"`

### 2. Gemini (`gemini`)
**Role:** The "Architect" / "Researcher" Agent.
`gemini` is ideal for high-level planning, explanation, and generating ideas.

**Basic Commands:**
*   **Start Session**:
    ```bash
    gemini
    ```

**Use Cases:**
*   **Brainstorming**: "Gemini, give me 3 ways to implement a coffee ordering queue."
*   **Documentation**: "Gemini, write a docstring for this complex function."

---

## 🧠 How to Use Agentic AI Effectively

To get the most out of the "Coffee Project", use the **Agentic Loop**:

### Step 1: Plan with Gemini
Before writing code, ask Gemini to outline the structure.
> *User*: "Gemini, I want to build a feature where users can customize their coffee (sugar, milk, type). Design the data structure."
> *Gemini*: [Outputs a JSON schema or Class diagram]

### Step 2: Build with Claude
Feed the plan to Claude to implement.
> *User (to Claude)*: "Read the plan above. Create the `Customization` class in `models.py` adhering to that structure."

### Step 3: Verify and Iterate
Use the agents to test their own work.
> *User (to Claude)*: "Run the tests. If the new customization feature fails, analyze the error and fix the code."

### Step 4: Context is King
When asking for help, always ensure the agent knows the context.
*   **Bad**: "Fix the bug."
*   **Good**: "I'm getting a `NullPointerException` in `brew()` when the water level is 0. Here is the `CoffeeMaker` class file. Fix it."

---

## 📂 Project Structure (Expected)
*   `src/` - Source code for the coffee application.
*   `tests/` - Unit tests (vital for Agentic verification).
*   `Readme.md` - This guide.

---
*Happy Coding with your AI Agents!*
