#!/usr/bin/env python3
"""
Claude Code Mastery Quest - All-in-One Tutorial System
Read tutorials, track progress, and view stats - all in one place!
"""

import re
import os
import sys
import subprocess
from pathlib import Path
from pydoc import pager

# ANSI color codes
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

def clear_screen():
    """Clear the terminal screen"""
    os.system('clear' if os.name != 'nt' else 'cls')

def format_markdown_for_terminal(content):
    """Basic markdown formatting for terminal display"""
    lines = content.split('\n')
    formatted = []

    for line in lines:
        # Headers
        if line.startswith('# '):
            formatted.append(f"\n{Colors.BOLD}{Colors.CYAN}{'='*70}{Colors.END}")
            formatted.append(f"{Colors.BOLD}{Colors.CYAN}{line[2:]}{Colors.END}")
            formatted.append(f"{Colors.BOLD}{Colors.CYAN}{'='*70}{Colors.END}\n")
        elif line.startswith('## '):
            formatted.append(f"\n{Colors.BOLD}{Colors.YELLOW}{line[3:]}{Colors.END}")
            formatted.append(f"{Colors.YELLOW}{'-'*50}{Colors.END}\n")
        elif line.startswith('### '):
            formatted.append(f"\n{Colors.BOLD}{Colors.GREEN}{line[4:]}{Colors.END}\n")
        # Code blocks
        elif line.startswith('```'):
            formatted.append(f"{Colors.CYAN}{line}{Colors.END}")
        # Lists
        elif line.startswith('- '):
            formatted.append(f"{Colors.GREEN}  •{Colors.END} {line[2:]}")
        elif re.match(r'^\d+\. ', line):
            formatted.append(f"{Colors.CYAN}{line}{Colors.END}")
        # Bold
        elif '**' in line:
            line = re.sub(r'\*\*(.+?)\*\*', f'{Colors.BOLD}\\1{Colors.END}', line)
            formatted.append(line)
        # Links
        elif '[' in line and '](' in line:
            line = re.sub(r'\[(.+?)\]\((.+?)\)', f'{Colors.BLUE}{Colors.UNDERLINE}\\1{Colors.END} ({Colors.CYAN}\\2{Colors.END})', line)
            formatted.append(line)
        else:
            formatted.append(line)

    return '\n'.join(formatted)

def view_markdown_file(filepath):
    """View a markdown file with formatting"""
    if not filepath.exists():
        print(f"{Colors.RED}Error: File not found!{Colors.END}")
        return False

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Try external viewers first
    external_viewers = ['glow', 'bat', 'mdcat']
    for viewer in external_viewers:
        try:
            # Check if viewer exists
            result = subprocess.run(['which', viewer], capture_output=True, text=True)
            if result.returncode == 0:
                if viewer == 'glow':
                    subprocess.run([viewer, str(filepath)])
                    return True
                elif viewer == 'bat':
                    subprocess.run([viewer, '--style=grid', '--paging=always', str(filepath)])
                    return True
                elif viewer == 'mdcat':
                    subprocess.run([viewer, str(filepath)])
                    return True
        except:
            continue

    # Fallback to Python pager with basic formatting
    formatted_content = format_markdown_for_terminal(content)

    print(f"\n{Colors.CYAN}{'='*70}{Colors.END}")
    print(f"{Colors.BOLD}📖 Reading: {filepath.name}{Colors.END}")
    print(f"{Colors.CYAN}{'='*70}{Colors.END}\n")
    print(f"{Colors.YELLOW}💡 Install 'glow' for better formatting: sudo snap install glow{Colors.END}\n")

    try:
        pager(formatted_content)
    except:
        # If pager fails, just print with pagination
        print(formatted_content)
        print(f"\n{Colors.CYAN}{'='*70}{Colors.END}")

    return True

def load_tracker():
    """Load the progress tracker file"""
    tracker_file = Path(__file__).parent / 'PROGRESS-TRACKER.md'
    if not tracker_file.exists():
        return None, None

    with open(tracker_file, 'r', encoding='utf-8') as f:
        content = f.read()

    return content, tracker_file

def save_tracker(content, tracker_file):
    """Save the updated progress tracker"""
    with open(tracker_file, 'w', encoding='utf-8') as f:
        f.write(content)

def extract_level_tasks(content, level_num):
    """Extract tasks from a specific level"""
    level_names = {
        1: "Level 1: Novice - Detailed Tracking",
        2: "Level 2: Apprentice - Detailed Tracking",
        3: "Level 3: Journeyman - Detailed Tracking",
        4: "Level 4: Expert - Detailed Tracking",
        5: "Level 5: Master - Detailed Tracking"
    }

    level_name = level_names.get(level_num)
    if not level_name:
        return []

    pattern = f"## {re.escape(level_name)}.*?(?=^## [^#]|\\Z)"
    section_match = re.search(pattern, content, re.DOTALL | re.MULTILINE)

    if not section_match:
        return []

    section = section_match.group(0)
    task_pattern = r'- \[([ x])\] (.+?) \(\+(\d+) XP\)'
    tasks = []

    for match in re.finditer(task_pattern, section):
        tasks.append({
            'checked': match.group(1) == 'x',
            'name': match.group(2),
            'xp': int(match.group(3)),
            'full_text': match.group(0)
        })

    return tasks

def toggle_task(content, task):
    """Toggle a task's checkbox"""
    old_checkbox = "[x]" if task['checked'] else "[ ]"
    new_checkbox = "[ ]" if task['checked'] else "[x]"

    old_text = task['full_text']
    new_text = old_text.replace(f"[{old_checkbox[1]}]", new_checkbox, 1)

    return content.replace(old_text, new_text, 1)

def calculate_total_xp(content):
    """Calculate total XP"""
    checked_pattern = r'- \[x\].*?\(\+(\d+) XP\)'
    checked_matches = re.findall(checked_pattern, content, re.IGNORECASE)
    return sum(int(xp) for xp in checked_matches)

def show_stats():
    """Display XP statistics"""
    content, _ = load_tracker()
    if not content:
        print(f"{Colors.RED}Error: PROGRESS-TRACKER.md not found!{Colors.END}")
        return

    calculator_path = Path(__file__).parent / 'xp-calculator.py'
    try:
        subprocess.run([sys.executable, str(calculator_path)])
    except Exception as e:
        # Fallback to basic stats
        total_xp = calculate_total_xp(content)
        print(f"\n{Colors.BOLD}{Colors.CYAN}Total XP: {total_xp} / 1125{Colors.END}\n")

def level_menu(level_num):
    """Show menu for a specific level with read and track options"""
    content, tracker_file = load_tracker()
    if not content:
        print(f"{Colors.RED}Error: PROGRESS-TRACKER.md not found!{Colors.END}")
        return

    level_files = {
        1: "01-LEVEL-NOVICE.md",
        2: "02-LEVEL-APPRENTICE.md",
        3: "03-LEVEL-JOURNEYMAN.md",
        4: "04-LEVEL-EXPERT.md",
        5: "05-LEVEL-MASTER.md"
    }

    level_names = ["Novice", "Apprentice", "Journeyman", "Expert", "Master"]
    level_name = level_names[level_num - 1]

    while True:
        clear_screen()
        tasks = extract_level_tasks(content, level_num)

        print("\n" + "="*70)
        print(f"{Colors.BOLD}{Colors.CYAN}📚 LEVEL {level_num}: {level_name.upper()}{Colors.END}")
        print("="*70 + "\n")

        total_xp = calculate_total_xp(content)
        completed = sum(1 for t in tasks if t['checked'])
        level_xp = sum(t['xp'] for t in tasks if t['checked'])
        max_level_xp = sum(t['xp'] for t in tasks)

        print(f"{Colors.BOLD}Overall Progress:{Colors.END} {total_xp} / 1125 XP")
        print(f"{Colors.BOLD}Level Progress:{Colors.END} {completed}/{len(tasks)} tasks ({level_xp}/{max_level_xp} XP)\n")

        print(f"{Colors.BOLD}Options:{Colors.END}\n")
        print(f"  {Colors.GREEN}R{Colors.END}. Read this level's tutorial")
        print(f"  {Colors.CYAN}T{Colors.END}. Toggle task completion")
        print(f"  {Colors.YELLOW}L{Colors.END}. List all tasks")
        print(f"  {Colors.BLUE}S{Colors.END}. Show detailed stats")
        print(f"  {Colors.RED}B{Colors.END}. Back to main menu")

        print()
        choice = input(f"{Colors.BOLD}Enter your choice: {Colors.END}").strip().upper()

        if choice == 'B':
            return
        elif choice == 'R':
            # Read the tutorial
            filepath = Path(__file__).parent / level_files[level_num]
            if filepath.exists():
                view_markdown_file(filepath)
                print(f"\n{Colors.GREEN}✓ Tutorial read!{Colors.END}")

                # Offer to mark chapter tasks as complete
                print(f"\n{Colors.BOLD}Mark related tasks as complete?{Colors.END}")
                print(f"Enter task numbers separated by spaces (or Enter to skip): ", end='')
                task_input = input().strip()

                if task_input:
                    for num_str in task_input.split():
                        if num_str.isdigit():
                            num = int(num_str)
                            if 1 <= num <= len(tasks):
                                task = tasks[num - 1]
                                if not task['checked']:
                                    content = toggle_task(content, task)
                                    save_tracker(content, tracker_file)
                                    print(f"{Colors.GREEN}✓ Task {num} marked complete (+{task['xp']} XP){Colors.END}")

                input(f"\n{Colors.BOLD}Press Enter to continue...{Colors.END}")
            else:
                print(f"{Colors.RED}Tutorial file not found!{Colors.END}")
                input(f"{Colors.BOLD}Press Enter to continue...{Colors.END}")

        elif choice == 'T':
            # Toggle task completion
            print(f"\n{Colors.BOLD}Tasks:{Colors.END}\n")
            for i, task in enumerate(tasks, 1):
                status = f"{Colors.GREEN}[✓]" if task['checked'] else f"{Colors.RED}[ ]"
                print(f"{status}{Colors.END} {i:2d}. {task['name']} {Colors.CYAN}(+{task['xp']} XP){Colors.END}")

            print(f"\nEnter task number to toggle (or Enter to cancel): ", end='')
            task_input = input().strip()

            if task_input.isdigit():
                num = int(task_input)
                if 1 <= num <= len(tasks):
                    task = tasks[num - 1]
                    content = toggle_task(content, task)
                    save_tracker(content, tracker_file)
                    status = "completed" if not task['checked'] else "uncompleted"
                    print(f"{Colors.GREEN}✓ Task {num} marked {status}!{Colors.END}")
                else:
                    print(f"{Colors.RED}Invalid task number!{Colors.END}")

            input(f"\n{Colors.BOLD}Press Enter to continue...{Colors.END}")

        elif choice == 'L':
            # List all tasks
            print(f"\n{Colors.BOLD}All Tasks:{Colors.END}\n")
            for i, task in enumerate(tasks, 1):
                status = f"{Colors.GREEN}[✓]" if task['checked'] else f"{Colors.RED}[ ]"
                print(f"{status}{Colors.END} {i:2d}. {task['name']} {Colors.CYAN}(+{task['xp']} XP){Colors.END}")

            input(f"\n{Colors.BOLD}Press Enter to continue...{Colors.END}")

        elif choice == 'S':
            # Show stats
            clear_screen()
            show_stats()
            input(f"\n{Colors.BOLD}Press Enter to continue...{Colors.END}")

def main_menu():
    """Main menu"""
    clear_screen()

    print("\n" + "="*70)
    print(f"{Colors.BOLD}{Colors.CYAN}🎮 CLAUDE CODE MASTERY QUEST - ALL-IN-ONE{Colors.END}")
    print("="*70 + "\n")

    content, _ = load_tracker()
    if content:
        total_xp = calculate_total_xp(content)
        print(f"{Colors.BOLD}Current XP: {Colors.GREEN}{total_xp}{Colors.END}{Colors.BOLD} / 1125{Colors.END}\n")

    print(f"{Colors.BOLD}Main Menu:{Colors.END}\n")

    # Levels
    print(f"{Colors.CYAN}LEVELS:{Colors.END}")
    print(f"  1. Level 1: Novice - The Basics")
    print(f"  2. Level 2: Apprentice - Essential Commands")
    print(f"  3. Level 3: Journeyman - Workflow Optimization")
    print(f"  4. Level 4: Expert - Advanced Techniques")
    print(f"  5. Level 5: Master - Complete Mastery")

    # Other options
    print(f"\n{Colors.CYAN}RESOURCES:{Colors.END}")
    print(f"  S. Start Here - Tutorial Overview")
    print(f"  Q. Quick Reference - Command Cheat Sheet")
    print(f"  P. Progress Tracker - View Your XP Log")

    # Utilities
    print(f"\n{Colors.CYAN}UTILITIES:{Colors.END}")
    print(f"  X. Show Detailed Stats")
    print(f"  H. Help & Troubleshooting")
    print(f"  E. Exit")

    print()
    choice = input(f"{Colors.BOLD}Enter your choice: {Colors.END}").strip().upper()

    if choice == 'E':
        print(f"\n{Colors.GREEN}Keep learning! 🚀{Colors.END}\n")
        return False
    elif choice in ['1', '2', '3', '4', '5']:
        level_menu(int(choice))
        return True
    elif choice == 'S':
        filepath = Path(__file__).parent / '00-START-HERE.md'
        if filepath.exists():
            view_markdown_file(filepath)
        input(f"\n{Colors.BOLD}Press Enter to continue...{Colors.END}")
        return True
    elif choice == 'Q':
        filepath = Path(__file__).parent / 'QUICK-REFERENCE.md'
        if filepath.exists():
            view_markdown_file(filepath)
        input(f"\n{Colors.BOLD}Press Enter to continue...{Colors.END}")
        return True
    elif choice == 'P':
        filepath = Path(__file__).parent / 'PROGRESS-TRACKER.md'
        if filepath.exists():
            view_markdown_file(filepath)
        input(f"\n{Colors.BOLD}Press Enter to continue...{Colors.END}")
        return True
    elif choice == 'X':
        clear_screen()
        show_stats()
        input(f"\n{Colors.BOLD}Press Enter to continue...{Colors.END}")
        return True
    elif choice == 'H':
        filepath = Path(__file__).parent / 'TROUBLESHOOTING.md'
        if filepath.exists():
            view_markdown_file(filepath)
        input(f"\n{Colors.BOLD}Press Enter to continue...{Colors.END}")
        return True
    else:
        print(f"{Colors.RED}Invalid choice!{Colors.END}")
        input(f"{Colors.BOLD}Press Enter to continue...{Colors.END}")
        return True

def main():
    """Main program loop"""
    try:
        while main_menu():
            pass
    except KeyboardInterrupt:
        print(f"\n\n{Colors.GREEN}Keep learning! 🚀{Colors.END}\n")
    except Exception as e:
        print(f"\n{Colors.RED}Error: {e}{Colors.END}\n")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
