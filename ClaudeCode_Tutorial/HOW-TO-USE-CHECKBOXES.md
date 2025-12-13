# 📋 How to Use Interactive Checkboxes

## Quick Guide to Tracking Your Progress

### Method 1: VS Code (Best Experience)

#### Step 1: Open the Progress Tracker
```bash
code PROGRESS-TRACKER.md
```

#### Step 2: Open Preview
- Press `Ctrl+Shift+V` (Windows/Linux) or `Cmd+Shift+V` (Mac)
- Or click the preview icon in the top right

#### Step 3: Click Checkboxes!
- In the preview pane, **click any checkbox** to toggle it
- `[ ]` becomes `[x]` automatically
- The markdown source file updates instantly

#### Step 4: Calculate Your XP
```bash
python3 xp-calculator.py
```

### Method 2: GitHub

1. Push your progress tracker to GitHub
2. View the file on GitHub.com
3. Click checkboxes directly in the rendered view
4. GitHub auto-commits the changes!

### Method 3: Manual Editing

1. Open `PROGRESS-TRACKER.md` in any text editor
2. Change `- [ ]` to `- [x]` for completed items
3. Change `- [x]` back to `- [ ]` to uncheck

## Visual Example

### Before (Unchecked):
```markdown
- [ ] Chapter 1: What is Claude Code? (+5 XP)
- [ ] Exercise 1.1: Installation Check (+10 XP)
- [ ] The Newcomer's Trial (+20 XP)
```

### After (Checked):
```markdown
- [x] Chapter 1: What is Claude Code? (+5 XP)
- [x] Exercise 1.1: Installation Check (+10 XP)
- [ ] The Newcomer's Trial (+20 XP)
```

### XP Calculator Output:
```bash
$ python3 xp-calculator.py

============================================================
🎮 CLAUDE CODE MASTERY QUEST - XP CALCULATOR
============================================================

Current Status:
  Level: 1 - Novice
  Total XP: 15 / 1125
  Completion: 1.3%

  Progress: [█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░]

XP Breakdown by Level:
  Level 1:  15/170 XP (  8.8%) ⚡ In Progress
  Level 2:   0/200 XP (  0.0%) ○ Not Started
  ...
```

## Tips

### 💡 Pro Tips:
1. **Check boxes as you complete tasks** - Don't wait! It's more motivating to see progress immediately
2. **Run the calculator frequently** - It's satisfying to see your XP grow
3. **Use VS Code's preview** - It's the smoothest experience
4. **Sync to GitHub** - Track your progress across devices

### 🎯 Recommended Workflow:
```bash
# 1. Complete a chapter or exercise
# 2. Open PROGRESS-TRACKER.md in VS Code
# 3. Check the completed item
# 4. Run the calculator
python3 xp-calculator.py

# 5. Feel accomplished! 🎉
```

## Troubleshooting

### Checkboxes not clicking in VS Code?
- Make sure you're in **Preview mode** (not the editor)
- Try the keyboard shortcut: `Ctrl+Shift+V` / `Cmd+Shift+V`

### Calculator not finding checkboxes?
- Ensure the format is exactly: `- [x] Task (+XX XP)`
- The XP value must be in parentheses with `+` and `XP`

### Python not installed?
```bash
# Check if Python is installed
python3 --version

# If not, install it:
# Ubuntu/WSL:
sudo apt install python3

# Mac:
brew install python3
```

## Example Session

Here's what a typical learning session looks like:

```bash
# Start by reading a chapter
# Then mark it complete in PROGRESS-TRACKER.md:
# - [x] Chapter 1: What is Claude Code? (+5 XP)

# Do the exercise
# Mark it complete:
# - [x] Exercise 1.1: Installation Check (+10 XP)

# Check your progress
$ python3 xp-calculator.py

# Output shows you earned 15 XP!
# Current Level: 1 - Novice
# Total XP: 15 / 1125
# Only 85 more XP to complete Level 1!

# Keep going! 🚀
```

---

**Remember**: The goal isn't just to check boxes—it's to actually learn and practice! The XP system is here to make learning fun and track your real progress. 🎮

[Back to Start](./00-START-HERE.md) | [Progress Tracker](./PROGRESS-TRACKER.md)
