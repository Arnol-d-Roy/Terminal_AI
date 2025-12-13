
```
 ______________________________________________________________________
|                                                                      |
|     T R O U B L E S H O O T I N G   G U I D E                        |
|                                                                      |
|     Solutions for Common Issues                                      |
|                                                                      |
|______________________________________________________________________|
```

======================================================================
                     PYTHON COMMAND ISSUES
======================================================================

### Problem: "Python was not found" error

**Symptoms**:
  * Error message: "Python was not found; run without arguments..."
  * Scripts won't run


### Solutions

#### Solution 1: Try different Python commands

Your system might use a different Python command. Try in order:

```bash
# Try python3 (most common in WSL/Linux)
python3 claude-tutorial.py

# Try python (Windows/some systems)
python claude-tutorial.py

# Try with full path
/usr/bin/python3 claude-tutorial.py
```


#### Solution 2: Check if Python is installed

```bash
# Check Python 3
python3 --version

# Or
python --version

# Should show: Python 3.x.x
```

If not installed:

```bash
# Ubuntu/WSL
sudo apt update
sudo apt install python3

# Check installation
python3 --version
```


#### Solution 3: Use the universal launcher

The `start-tutorial.sh` script automatically detects Python:

```bash
./start-tutorial.sh
```

----------------------------------------------------------------------


## File Not Found Issues

### Problem: "No such file or directory"

**Cause**: Running from wrong directory.


### Solution

Make sure you're in the tutorial directory:

```bash
# Navigate to the correct directory
cd "/mnt/d/Github Repos/Terminal_AI/ClaudeCode_Tutorial"

# Verify files exist
ls *.py *.md

# Then run
python claude-tutorial.py
```

----------------------------------------------------------------------


## Progress Tracker Issues

### Problem: Checkboxes not updating

**Cause**: File permissions or file is open elsewhere.


### Solutions

  1. Close PROGRESS-TRACKER.md if open in any editor
  2. Check file permissions:
     ```bash
     ls -la PROGRESS-TRACKER.md
     ```
  3. Ensure you have write permissions


### Problem: XP not calculating correctly

**Cause**: Checkbox format is incorrect.


### Solution

Ensure checkboxes are formatted exactly as:

```
- [ ]  for unchecked (note the spaces)
- [x]  for checked (lowercase x)
(+XX XP)  for XP value (with parentheses and +)
```

----------------------------------------------------------------------


## Display Issues

### Problem: Colors not showing in terminal

**Cause**: Terminal doesn't support ANSI colors.


### Solution

Use a modern terminal:

  * **Windows**: Windows Terminal (recommended)
  * **Linux**: Most terminals support colors by default
  * **Mac**: iTerm2 or default Terminal.app


### Problem: Tables/boxes look broken

**Cause**: Font doesn't support box-drawing characters.


### Solution

Use a monospace font that supports Unicode:

  * Consolas
  * Cascadia Code
  * JetBrains Mono
  * Fira Code

----------------------------------------------------------------------


## XP Calculator Issues

### Problem: "No files found" or incorrect XP

**Cause**: Running from wrong directory.


### Solution

```bash
# Make sure you're in the tutorial directory
cd "/mnt/d/Github Repos/Terminal_AI/ClaudeCode_Tutorial"

# Then run
python xp-calculator.py
```


### Problem: Script shows encoding errors

**Cause**: File encoding issues.


### Solution

Ensure files are UTF-8 encoded:

```bash
file -i PROGRESS-TRACKER.md
# Should show: charset=utf-8
```

----------------------------------------------------------------------


## Quick Diagnostic Commands

Run these to verify your setup:

```bash
# 1. Check Python version
python3 --version

# 2. Test Python works
python3 -c "print('Python works!')"

# 3. Verify files exist
ls -lh *.py *.md

# 4. Check file permissions
ls -la PROGRESS-TRACKER.md

# 5. Test the main script
python3 claude-tutorial.py
```

----------------------------------------------------------------------


## Common Error Messages

```
+---------------------------------------------------------------------+
|  ERROR MESSAGE                |  LIKELY CAUSE & FIX                 |
+---------------------------------------------------------------------+
|  "command not found: python"  |  Use python3 instead                |
|  "No such file or directory"  |  cd to tutorial directory first     |
|  "Permission denied"          |  chmod +x script.sh                 |
|  "SyntaxError"                |  Using Python 2; need Python 3      |
|  "UnicodeDecodeError"         |  File encoding issue; save as UTF-8 |
+---------------------------------------------------------------------+
```

----------------------------------------------------------------------


## Working Commands Reference

These should work on most systems:

```bash
# Main tutorial (recommended)
python3 claude-tutorial.py

# View stats
python3 xp-calculator.py

# Universal launcher
./start-tutorial.sh

# Manual editing
nano PROGRESS-TRACKER.md
# or
code PROGRESS-TRACKER.md
```

If `python3` doesn't work, try replacing with `python`.

----------------------------------------------------------------------


## Still Stuck?

### Checklist

- [ ] Am I in the correct directory?
- [ ] Is Python 3 installed?
- [ ] Do all required files exist?
- [ ] Do I have write permissions?
- [ ] Is my terminal supporting colors and Unicode?


### Getting More Help

  1. **Check file integrity**:
     ```bash
     ls -lh *.py *.md
     # Verify all files exist
     ```

  2. **Re-download files** if something is corrupted

  3. **Check Python version**:
     ```bash
     python3 --version
     # Should be Python 3.6 or higher
     ```

  4. **Test with simple command**:
     ```bash
     python3 -c "print('Python works!')"
     # Should print: Python works!
     ```

======================================================================
  If problems persist, check the project repository for updates.
======================================================================
