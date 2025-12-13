#!/usr/bin/env python3
"""
Claude Code Mastery Quest - Interactive Progress Tracker
Mark tasks complete directly from the terminal!
"""

import re
import os
from pathlib import Path

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

def load_tracker():
    """Load the progress tracker file"""
    tracker_file = Path(__file__).parent / 'PROGRESS-TRACKER.md'
    if not tracker_file.exists():
        print(f"{Colors.RED}Error: PROGRESS-TRACKER.md not found!{Colors.END}")
        return None, None

    with open(tracker_file, 'r', encoding='utf-8') as f:
        content = f.read()

    return content, tracker_file

def extract_tasks(content, level_num=1):
    """Extract tasks from a specific level"""
    level_names = {
        1: "Level 1: Novice - Detailed Tracking",
        2: "Level 2: Apprentice - Detailed Tracking",
        3: "Level 3: Journeyman - Detailed Tracking",
        4: "Level 4: Expert - Detailed Tracking",
        5: "Level 5: Master - Detailed Tracking"
    }

    level_name = level_names.get(level_num, "Level 1: Novice - Detailed Tracking")

    # Find the level section (match until next ## that's not ###)
    pattern = f"## {re.escape(level_name)}.*?(?=^## [^#]|\\Z)"
    section_match = re.search(pattern, content, re.DOTALL | re.MULTILINE)

    if not section_match:
        return []

    section = section_match.group(0)

    # Extract all tasks with checkboxes
    task_pattern = r'- \[([ x])\] (.+?) \(\+(\d+) XP\)'
    tasks = []

    for match in re.finditer(task_pattern, section):
        is_checked = match.group(1) == 'x'
        task_name = match.group(2)
        xp_value = int(match.group(3))
        full_match = match.group(0)

        tasks.append({
            'checked': is_checked,
            'name': task_name,
            'xp': xp_value,
            'full_text': full_match
        })

    return tasks

def calculate_total_xp(content):
    """Calculate total XP from all checked tasks"""
    checked_pattern = r'- \[x\].*?\(\+(\d+) XP\)'
    checked_matches = re.findall(checked_pattern, content, re.IGNORECASE)
    return sum(int(xp) for xp in checked_matches)

def display_level_menu(tasks, level_num):
    """Display tasks for a level with numbers"""
    clear_screen()

    level_names = ["Novice", "Apprentice", "Journeyman", "Expert", "Master"]
    level_name = level_names[level_num - 1] if 1 <= level_num <= 5 else "Unknown"

    print("\n" + "="*70)
    print(f"{Colors.BOLD}{Colors.CYAN}🎮 LEVEL {level_num}: {level_name.upper()}{Colors.END}")
    print("="*70 + "\n")

    if not tasks:
        print(f"{Colors.YELLOW}No tasks found for this level.{Colors.END}\n")
        return

    # Calculate completed tasks
    completed = sum(1 for t in tasks if t['checked'])
    total_xp = sum(t['xp'] for t in tasks if t['checked'])
    max_xp = sum(t['xp'] for t in tasks)

    print(f"{Colors.BOLD}Progress: {completed}/{len(tasks)} tasks completed ({total_xp}/{max_xp} XP){Colors.END}\n")

    # Display tasks
    for i, task in enumerate(tasks, 1):
        status = f"{Colors.GREEN}[✓]" if task['checked'] else f"{Colors.RED}[ ]"
        print(f"{status}{Colors.END} {i:2d}. {task['name']} {Colors.CYAN}(+{task['xp']} XP){Colors.END}")

    print()

def toggle_task(content, task):
    """Toggle a task's checkbox in the content"""
    old_checkbox = "[x]" if task['checked'] else "[ ]"
    new_checkbox = "[ ]" if task['checked'] else "[x]"

    old_text = task['full_text']
    new_text = old_text.replace(f"[{old_checkbox[1]}]", new_checkbox, 1)

    # Replace in content
    new_content = content.replace(old_text, new_text, 1)
    return new_content

def save_tracker(content, tracker_file):
    """Save the updated progress tracker"""
    with open(tracker_file, 'w', encoding='utf-8') as f:
        f.write(content)

def main_menu():
    """Display the main menu"""
    clear_screen()
    print("\n" + "="*70)
    print(f"{Colors.BOLD}{Colors.CYAN}🎮 CLAUDE CODE MASTERY QUEST - INTERACTIVE TRACKER{Colors.END}")
    print("="*70 + "\n")

    content, tracker_file = load_tracker()
    if content is None:
        return

    total_xp = calculate_total_xp(content)

    print(f"{Colors.BOLD}Current Total XP: {Colors.GREEN}{total_xp}{Colors.END}{Colors.BOLD} / 1125{Colors.END}\n")

    print(f"{Colors.BOLD}Select a Level:{Colors.END}")
    print(f"  {Colors.CYAN}1{Colors.END}. Level 1: Novice (0-99 XP)")
    print(f"  {Colors.CYAN}2{Colors.END}. Level 2: Apprentice (100-299 XP)")
    print(f"  {Colors.CYAN}3{Colors.END}. Level 3: Journeyman (300-599 XP)")
    print(f"  {Colors.CYAN}4{Colors.END}. Level 4: Expert (600-999 XP)")
    print(f"  {Colors.CYAN}5{Colors.END}. Level 5: Master (1000+ XP)")
    print(f"  {Colors.YELLOW}S{Colors.END}. Show Stats (run xp-calculator.py)")
    print(f"  {Colors.RED}Q{Colors.END}. Quit")

    print()
    choice = input(f"{Colors.BOLD}Enter your choice: {Colors.END}").strip().upper()

    if choice == 'Q':
        print(f"\n{Colors.GREEN}Keep up the great work! 🚀{Colors.END}\n")
        return False
    elif choice == 'S':
        clear_screen()
        os.system('python3 xp-calculator.py')
        input(f"\n{Colors.BOLD}Press Enter to continue...{Colors.END}")
        return True
    elif choice in ['1', '2', '3', '4', '5']:
        level_menu(int(choice), content, tracker_file)
        return True
    else:
        print(f"{Colors.RED}Invalid choice!{Colors.END}")
        input(f"{Colors.BOLD}Press Enter to continue...{Colors.END}")
        return True

def level_menu(level_num, content, tracker_file):
    """Handle level-specific menu"""
    while True:
        tasks = extract_tasks(content, level_num)
        display_level_menu(tasks, level_num)

        if not tasks:
            input(f"{Colors.BOLD}Press Enter to go back...{Colors.END}")
            return

        print(f"{Colors.BOLD}Actions:{Colors.END}")
        print(f"  {Colors.CYAN}[Number]{Colors.END} - Toggle task (e.g., '1' to toggle task 1)")
        print(f"  {Colors.YELLOW}A{Colors.END} - Mark all complete")
        print(f"  {Colors.YELLOW}N{Colors.END} - Mark all incomplete")
        print(f"  {Colors.GREEN}B{Colors.END} - Back to main menu")

        print()
        choice = input(f"{Colors.BOLD}Enter your choice: {Colors.END}").strip().upper()

        if choice == 'B':
            return
        elif choice == 'A':
            # Mark all as complete
            for task in tasks:
                if not task['checked']:
                    content = toggle_task(content, task)
            save_tracker(content, tracker_file)
            print(f"{Colors.GREEN}All tasks marked complete!{Colors.END}")
            input(f"{Colors.BOLD}Press Enter to continue...{Colors.END}")
        elif choice == 'N':
            # Mark all as incomplete
            for task in tasks:
                if task['checked']:
                    content = toggle_task(content, task)
            save_tracker(content, tracker_file)
            print(f"{Colors.YELLOW}All tasks marked incomplete!{Colors.END}")
            input(f"{Colors.BOLD}Press Enter to continue...{Colors.END}")
        elif choice.isdigit():
            task_num = int(choice)
            if 1 <= task_num <= len(tasks):
                task = tasks[task_num - 1]
                content = toggle_task(content, task)
                save_tracker(content, tracker_file)

                status = "completed" if not task['checked'] else "uncompleted"
                print(f"{Colors.GREEN}Task {task_num} marked {status}! (+{task['xp']} XP){Colors.END}")
                input(f"{Colors.BOLD}Press Enter to continue...{Colors.END}")
            else:
                print(f"{Colors.RED}Invalid task number!{Colors.END}")
                input(f"{Colors.BOLD}Press Enter to continue...{Colors.END}")
        else:
            print(f"{Colors.RED}Invalid choice!{Colors.END}")
            input(f"{Colors.BOLD}Press Enter to continue...{Colors.END}")

def main():
    """Main program loop"""
    try:
        while main_menu():
            pass
    except KeyboardInterrupt:
        print(f"\n\n{Colors.GREEN}Goodbye! Keep learning! 🎮{Colors.END}\n")
    except Exception as e:
        print(f"\n{Colors.RED}Error: {e}{Colors.END}\n")

if __name__ == "__main__":
    main()
