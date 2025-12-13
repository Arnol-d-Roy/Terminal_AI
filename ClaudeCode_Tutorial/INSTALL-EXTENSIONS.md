# VS Code Extensions for Interactive Checkboxes

## The Problem
VS Code's built-in markdown preview doesn't support clickable checkboxes.

## The Solution
Install one of these extensions:

### Option 1: Markdown All in One (Recommended)
1. Open VS Code
2. Press `Ctrl+Shift+X` (Extensions)
3. Search for "Markdown All in One"
4. Click Install
5. Reload VS Code

**Features:**
- Keyboard shortcuts to toggle checkboxes (`Alt+C`)
- Better markdown support overall
- Table formatting, auto-lists, etc.

**How to use:**
- Place cursor on a checkbox line
- Press `Alt+C` to toggle it

### Option 2: Markdown Checkbox
1. Press `Ctrl+Shift+X`
2. Search for "Markdown Checkbox"
3. Install it

**How to use:**
- Click checkboxes directly in preview
- Or use keyboard shortcuts

### Option 3: Manual Editing (No Extension Needed)
Just edit the markdown directly:
- Change `- [ ]` to `- [x]` (checked)
- Change `- [x]` to `- [ ]` (unchecked)

## Quick Test
After installing an extension, try this:
1. Open `PROGRESS-TRACKER.md`
2. Find any checkbox line: `- [ ] Chapter 1: What is Claude Code? (+5 XP)`
3. Press `Alt+C` on that line
4. It should change to: `- [x] Chapter 1: What is Claude Code? (+5 XP)`
5. Run `python3 xp-calculator.py` to see your XP!
