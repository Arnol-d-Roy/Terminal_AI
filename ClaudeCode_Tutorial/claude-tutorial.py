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
    """Extract tasks from a specific level with category information"""
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

    # Track current section to categorize tasks
    current_category = "Chapter"

    for line in section.split('\n'):
        # Detect category from section headers
        if '### Chapter' in line:
            current_category = "Chapter"
        elif '### Exercise' in line:
            current_category = "Exercise"
        elif '### Challenge' in line:
            current_category = "Challenge"
        elif '### Boss Battle' in line:
            current_category = "Boss"
        elif '### Achievement' in line:
            current_category = "Achievement"

        # Match task pattern
        match = re.search(task_pattern, line)
        if match:
            tasks.append({
                'checked': match.group(1) == 'x',
                'name': match.group(2),
                'xp': int(match.group(3)),
                'full_text': match.group(0),
                'category': current_category
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

def auto_complete_achievements(content, tasks, level_num):
    """Automatically mark achievements based on completion criteria"""
    # Count completed tasks by category
    chapters_done = sum(1 for t in tasks if t['category'] == 'Chapter' and t['checked'])
    exercises_done = sum(1 for t in tasks if t['category'] == 'Exercise' and t['checked'])
    challenges_done = sum(1 for t in tasks if t['category'] == 'Challenge' and t['checked'])
    boss_done = sum(1 for t in tasks if t['category'] == 'Boss' and t['checked'])

    total_chapters = sum(1 for t in tasks if t['category'] == 'Chapter')
    total_exercises = sum(1 for t in tasks if t['category'] == 'Exercise')

    # Define achievement criteria
    achievement_criteria = {
        1: [  # Level 1: Novice
            (chapters_done >= 1, "Understanding the Mission"),
            (chapters_done >= 3, "First Contact"),
            (exercises_done >= 1, "Command Discovery"),
            (exercises_done >= 2, "Time Traveler"),
            (chapters_done == total_chapters and exercises_done == total_exercises and boss_done > 0, "Novice No More")
        ],
        2: [  # Level 2: Apprentice
            (chapters_done >= 2, "Flag Bearer"),
            (exercises_done >= 2, "File Whisperer"),
            (chapters_done >= 4, "Danger Zone Awareness"),
            (exercises_done >= 4, "Prompt Architect"),
            (chapters_done == total_chapters and exercises_done == total_exercises and boss_done > 0, "Apprentice Graduate")
        ],
        3: [  # Level 3: Journeyman
            (chapters_done >= 2, "Workflow Analyst"),
            (exercises_done >= 2, "Configuration Master"),
            (exercises_done >= 3, "Task Commander"),
            (chapters_done >= 5, "Efficiency Expert"),
            (chapters_done == total_chapters and exercises_done == total_exercises and boss_done > 0, "Journeyman Complete")
        ],
        4: [  # Level 4: Expert
            (chapters_done >= 2, "Model Strategist"),
            (exercises_done >= 2, "Context Commander"),
            (exercises_done >= 3, "Automation Architect"),
            (chapters_done >= 5, "Prompt Wizard"),
            (exercises_done >= 4, "Troubleshooter"),
            (chapters_done == total_chapters and exercises_done == total_exercises and boss_done > 0, "Expert Elite")
        ],
        5: [  # Level 5: Master
            (chapters_done >= 2, "Path of the Master"),
            (exercises_done >= 2, "Systems Architect"),
            (exercises_done >= 3, "Knowledge Sharer"),
            (chapters_done >= 4, "Boundary Pusher"),
            (chapters_done == total_chapters and exercises_done == total_exercises and boss_done > 0, "True Master")
        ]
    }

    # Auto-mark achievements
    criteria = achievement_criteria.get(level_num, [])
    for should_unlock, achievement_name in criteria:
        if should_unlock:
            # Find and mark the achievement
            for task in tasks:
                if task['category'] == 'Achievement' and achievement_name in task['name'] and not task['checked']:
                    content = toggle_task(content, task)

    return content

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

        # Group tasks by category
        categories = {
            'Chapter': {'tasks': [], 'color': Colors.BLUE, 'icon': '📘'},
            'Exercise': {'tasks': [], 'color': Colors.GREEN, 'icon': '📗'},
            'Challenge': {'tasks': [], 'color': Colors.CYAN, 'icon': '📙'},
            'Boss': {'tasks': [], 'color': Colors.RED, 'icon': '📕'},
            'Achievement': {'tasks': [], 'color': Colors.YELLOW, 'icon': '🏆'}
        }

        # Organize tasks into categories
        for i, task in enumerate(tasks, 1):
            task['number'] = i  # Add task number for reference
            category = task['category']
            if category in categories:
                categories[category]['tasks'].append(task)

        # Display tasks grouped by category
        print(f"{Colors.BOLD}Tasks:{Colors.END}\n")

        for category_name, category_info in categories.items():
            category_tasks = category_info['tasks']
            if not category_tasks:
                continue

            # Calculate category completion
            completed_in_category = sum(1 for t in category_tasks if t['checked'])
            total_in_category = len(category_tasks)
            category_xp = sum(t['xp'] for t in category_tasks if t['checked'])
            max_category_xp = sum(t['xp'] for t in category_tasks)

            # Category header
            completion_text = f"{completed_in_category}/{total_in_category}"
            xp_text = f"{category_xp}/{max_category_xp} XP"

            # Show completion status
            if completed_in_category == total_in_category:
                status_icon = f"{Colors.GREEN}✓{Colors.END}"
                status_text = f"{Colors.GREEN}Complete{Colors.END}"
            elif completed_in_category > 0:
                status_icon = f"{Colors.YELLOW}⚡{Colors.END}"
                status_text = f"{Colors.YELLOW}In Progress{Colors.END}"
            else:
                status_icon = f"{Colors.RED}○{Colors.END}"
                status_text = f"{Colors.RED}Not Started{Colors.END}"

            # Print category header
            category_display = category_name.upper() + "S" if category_name != "Boss" else "BOSS BATTLE"
            if category_name == "Achievement":
                category_display = "ACHIEVEMENTS"

            print(f"{category_info['icon']} {Colors.BOLD}{category_info['color']}{category_display}{Colors.END} "
                  f"{status_icon} ({completion_text} - {xp_text}) {status_text}")

            # Print tasks in this category
            for task in category_tasks:
                task_status = f"{Colors.GREEN}[✓]" if task['checked'] else f"{Colors.RED}[ ]"

                # Add hint for locked achievements
                hint = ""
                if category_name == 'Achievement' and not task['checked']:
                    hint = f" {Colors.YELLOW}🔒{Colors.END}"

                print(f"  {task_status}{Colors.END} {task['number']:2d}. {category_info['color']}{task['name']}{Colors.END} "
                      f"({task['xp']} XP){hint}")

            print()  # Blank line between categories

        print(f"\n{Colors.BOLD}Options:{Colors.END}\n")
        print(f"  {Colors.GREEN}R{Colors.END}. Read this level's tutorial")
        print(f"  {Colors.CYAN}T{Colors.END}. Toggle task completion")
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
                                if not task['checked'] and task['category'] != 'Achievement':
                                    content = toggle_task(content, task)
                                    # Auto-complete achievements
                                    tasks = extract_level_tasks(content, level_num)
                                    content = auto_complete_achievements(content, tasks, level_num)
                                    save_tracker(content, tracker_file)
                                    print(f"{Colors.GREEN}✓ Task {num} marked complete (+{task['xp']} XP){Colors.END}")

                input(f"\n{Colors.BOLD}Press Enter to continue...{Colors.END}")
            else:
                print(f"{Colors.RED}Tutorial file not found!{Colors.END}")
                input(f"{Colors.BOLD}Press Enter to continue...{Colors.END}")

        elif choice == 'T':
            # Toggle task completion
            print(f"\nEnter task number to toggle (or Enter to cancel): ", end='')
            task_input = input().strip()

            if task_input.isdigit():
                num = int(task_input)
                if 1 <= num <= len(tasks):
                    task = tasks[num - 1]
                    # Don't allow manual toggling of achievements
                    if task['category'] == 'Achievement':
                        print(f"{Colors.YELLOW}⚠ Achievements are earned automatically!{Colors.END}")
                        print(f"{Colors.YELLOW}Complete more tasks to unlock achievements.{Colors.END}")
                    else:
                        content = toggle_task(content, task)
                        # Auto-complete achievements after toggling
                        tasks = extract_level_tasks(content, level_num)
                        content = auto_complete_achievements(content, tasks, level_num)
                        save_tracker(content, tracker_file)
                        status = "completed" if not task['checked'] else "uncompleted"
                        print(f"{Colors.GREEN}✓ Task {num} marked {status}!{Colors.END}")

                        # Show newly unlocked achievements
                        new_tasks = extract_level_tasks(content, level_num)
                        newly_unlocked = [t for t in new_tasks if t['category'] == 'Achievement' and t['checked'] and not any(ot['name'] == t['name'] and ot['checked'] for ot in tasks if ot['category'] == 'Achievement')]
                        if newly_unlocked:
                            print(f"\n{Colors.YELLOW}🏆 Achievement Unlocked:{Colors.END}")
                            for ach in newly_unlocked:
                                print(f"  {Colors.YELLOW}★ {ach['name']} (+{ach['xp']} XP){Colors.END}")
                else:
                    print(f"{Colors.RED}Invalid task number!{Colors.END}")

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
