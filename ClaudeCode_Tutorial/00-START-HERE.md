# Claude Code Mastery Quest
## Your Journey from Terminal Novice to AI Coding Master

```
    _____ _                 _        _____          _
   / ____| |               | |      / ____|        | |
  | |    | | __ _ _   _  __| | ___ | |     ___   __| | ___
  | |    | |/ _` | | | |/ _` |/ _ \| |    / _ \ / _` |/ _ \
  | |____| | (_| | |_| | (_| |  __/| |___| (_) | (_| |  __/
   \_____|_|\__,_|\__,_|\__,_|\___| \_____\___/ \__,_|\___|

              M A S T E R Y   Q U E S T
```

---

## Welcome, Adventurer!

You are about to embark on an epic journey to master **Claude Code** - a powerful AI assistant that lives in your terminal. Whether you're writing code, debugging complex issues, or automating workflows, Claude Code will become your most trusted companion.

This tutorial system is designed like a video game progression. You'll start as a **Novice**, earn experience through hands-on practice, unlock achievements, and eventually reach **Master** status.

---

## How This Tutorial Works

### The Level System

| Level | Title | XP Required | Description |
|-------|-------|-------------|-------------|
| 1 | Novice | 0 XP | Just starting out - learning the basics |
| 2 | Apprentice | 100 XP | Building foundation - essential commands |
| 3 | Journeyman | 300 XP | Gaining confidence - workflow optimization |
| 4 | Expert | 600 XP | Power user - advanced techniques |
| 5 | Master | 1000 XP | Teaching others - complete mastery |

### Earning XP

- Reading and understanding a section: **+5 XP**
- Completing a practice exercise: **+10 XP**
- Completing a challenge: **+15-25 XP** (based on difficulty)
- Defeating a "Boss Battle" scenario: **+50 XP**
- Discovering an Easter Egg tip: **+5 XP**

### Achievement Badges

Throughout your journey, you'll unlock achievement badges. Track them in your [Progress Tracker](./PROGRESS-TRACKER.md)!

### 🎮 Interactive Progress Tracking

**This tutorial features interactive checkboxes!** Here's how it works:

#### In VS Code (Recommended):
1. Open `PROGRESS-TRACKER.md` in VS Code
2. Enable preview mode (Ctrl+Shift+V or Cmd+Shift+V)
3. **Click any checkbox** to mark tasks complete - they toggle automatically!
4. Your progress is saved to the file immediately

#### Automatic XP Calculation:
After checking boxes, run this command to see your stats:
```bash
python3 xp-calculator.py
```

The script shows:
- Your current level and total XP
- Visual progress bar
- XP breakdown by level
- Achievements, boss battles, and Easter eggs found
- Motivational messages based on your progress

**Example Output:**
```
🎮 CLAUDE CODE MASTERY QUEST - XP CALCULATOR
============================================================
Current Status:
  Level: 2 - Apprentice
  Total XP: 145 / 1125
  Completion: 12.9%

  Progress: [████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░]
```

#### GitHub/Other Viewers:
The checkboxes work in GitHub too! Just view the file and click to toggle.

---

## Quick Navigation

### For Complete Beginners
> "I've never used Claude Code before"

Start here: **[Level 1: Novice](./01-LEVEL-NOVICE.md)**

### For Those With Some Experience
> "I know basic commands but want to learn more"

Jump to: **[Level 2: Apprentice](./02-LEVEL-APPRENTICE.md)**

### For Intermediate Users
> "I use Claude Code regularly but want to be faster"

Continue at: **[Level 3: Journeyman](./03-LEVEL-JOURNEYMAN.md)**

### For Advanced Users
> "I'm comfortable but want to master advanced features"

Level up at: **[Level 4: Expert](./04-LEVEL-EXPERT.md)**

### For Power Users
> "I want to know everything and help others"

Achieve mastery: **[Level 5: Master](./05-LEVEL-MASTER.md)**

---

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
|-- xp-calculator.py          <-- Auto-calculate XP from checkboxes
```

---

## Your Starting Stats

```
+------------------------------------------+
|           ADVENTURER PROFILE              |
+------------------------------------------+
| Name: ____________________               |
| Date Started: ____________               |
|                                          |
| Current Level: 1 (Novice)                |
| Total XP: 0 / 1000                       |
|                                          |
| [__________] 0%                          |
|                                          |
| Achievements Unlocked: 0 / 25            |
| Challenges Completed: 0 / 15             |
| Boss Battles Won: 0 / 5                  |
+------------------------------------------+
```

---

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

---

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

[Start Level 1: Novice -->](./01-LEVEL-NOVICE.md)

---

## Quick Start (For the Impatient)

If you just want to start using Claude Code right now, here are the essential commands:

```bash
# Start a new conversation
claude

# Resume your last conversation
claude -r

# Get help
claude --help
```

But trust us - taking the time to complete this tutorial will make you **10x more productive**. The investment pays off!

---

## Resources

- **Reference Video**: [Claude Code Tutorial](https://www.youtube.com/watch?v=MsQACpcuTkU&t=147s)
- **Official Documentation**: [Anthropic Docs](https://docs.anthropic.com)
- **Quick Reference**: [QUICK-REFERENCE.md](./QUICK-REFERENCE.md)

---

## A Note on Learning

> "The expert in anything was once a beginner."

Don't rush. Take your time with each level. Practice the exercises. The goal isn't to finish quickly - it's to build genuine mastery that will serve you for years to come.

Every command you learn, every shortcut you master, is XP in your real-world developer skills.

**Your adventure awaits!**

---

*Tutorial Version: 1.0*
*Last Updated: December 2024*
*Created for: Claude Code CLI Users*
