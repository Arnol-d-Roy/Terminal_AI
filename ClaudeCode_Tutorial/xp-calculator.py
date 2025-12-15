#!/usr/bin/env python3
"""
Claude Code Mastery Quest - XP Calculator
Automatically calculates your XP from checked boxes in PROGRESS-TRACKER.md
"""

import re
import os
from pathlib import Path

# ANSI color codes for terminal output
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

def calculate_xp():
    """Calculate total XP from checked boxes in PROGRESS-TRACKER.md"""

    tracker_file = Path(__file__).parent / 'PROGRESS-TRACKER.md'

    if not tracker_file.exists():
        print(f"{Colors.RED}Error: PROGRESS-TRACKER.md not found!{Colors.END}")
        return

    with open(tracker_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all checked boxes with XP values: - [x] Something (+XX XP)
    checked_pattern = r'- \[x\].*?\(\+(\d+) XP\)'
    checked_matches = re.findall(checked_pattern, content, re.IGNORECASE)

    # Calculate total XP
    total_xp = sum(int(xp) for xp in checked_matches)

    # Level thresholds
    levels = [
        (0, "Novice", 170),
        (100, "Apprentice", 210),
        (300, "Journeyman", 270),
        (600, "Expert", 380),
        (1000, "Master", 360)
    ]

    # Determine current level
    current_level = "Novice"
    current_level_num = 1
    next_level_xp = 100
    xp_in_current_level = total_xp

    for i, (threshold, level_name, level_max_xp) in enumerate(levels):
        if total_xp >= threshold:
            current_level = level_name
            current_level_num = i + 1
            xp_in_current_level = total_xp - threshold
            if i < len(levels) - 1:
                next_level_xp = levels[i + 1][0]
        else:
            break

    # Calculate progress percentage
    max_xp = 1390
    progress_percent = (total_xp / max_xp) * 100

    # Display results
    print("\n" + "="*60)
    print(f"{Colors.BOLD}{Colors.CYAN}🎮 CLAUDE CODE MASTERY QUEST - XP CALCULATOR{Colors.END}")
    print("="*60 + "\n")

    # Current Status
    print(f"{Colors.BOLD}Current Status:{Colors.END}")
    print(f"  Level: {Colors.YELLOW}{current_level_num} - {current_level}{Colors.END}")
    print(f"  Total XP: {Colors.GREEN}{total_xp}{Colors.END} / {max_xp}")
    print(f"  Completion: {Colors.CYAN}{progress_percent:.1f}%{Colors.END}\n")

    # Progress bar
    bar_length = 40
    filled_length = int(bar_length * total_xp / max_xp)
    bar = '█' * filled_length + '░' * (bar_length - filled_length)
    print(f"  Progress: [{Colors.GREEN}{bar}{Colors.END}]\n")

    # Level breakdown
    print(f"{Colors.BOLD}XP Breakdown by Level:{Colors.END}")

    level_xp = {
        "Level 1": 0,
        "Level 2": 0,
        "Level 3": 0,
        "Level 4": 0,
        "Level 5": 0
    }

    # Parse each level's XP (with correct section headers)
    level_sections = [
        ("Level 1: Novice - Detailed Tracking", "Level 1"),
        ("Level 2: Apprentice - Detailed Tracking", "Level 2"),
        ("Level 3: Journeyman - Detailed Tracking", "Level 3"),
        ("Level 4: Expert - Detailed Tracking", "Level 4"),
        ("Level 5: Master - Detailed Tracking", "Level 5")
    ]

    for section_title, level_key in level_sections:
        # Find section in content (match until next ## that's not ###)
        pattern = f"## {re.escape(section_title)}.*?(?=^## [^#]|\\Z)"
        section_match = re.search(pattern, content, re.DOTALL | re.MULTILINE)

        if section_match:
            section = section_match.group(0)
            # Find checked boxes in this section
            section_xp = sum(int(xp) for xp in re.findall(checked_pattern, section, re.IGNORECASE))
            level_xp[level_key] = section_xp

    max_xp_per_level = [170, 210, 270, 380, 360]
    for i, (level_key, xp) in enumerate(level_xp.items()):
        max_xp_level = max_xp_per_level[i]
        level_percent = (xp / max_xp_level) * 100 if max_xp_level > 0 else 0

        # Color code based on completion
        if level_percent == 100:
            color = Colors.GREEN
            status = "✓ Complete"
        elif level_percent > 0:
            color = Colors.YELLOW
            status = "⚡ In Progress"
        else:
            color = Colors.RED
            status = "○ Not Started"

        print(f"  {color}{level_key}: {xp:3d}/{max_xp_level} XP ({level_percent:5.1f}%) {status}{Colors.END}")

    # Next milestone
    print(f"\n{Colors.BOLD}Next Milestone:{Colors.END}")
    if total_xp < 1000:
        xp_needed = next_level_xp - total_xp
        print(f"  {xp_needed} XP needed to reach {Colors.YELLOW}{levels[current_level_num][1] if current_level_num < len(levels) else 'Master'}{Colors.END}")
    else:
        print(f"  {Colors.GREEN}🏆 You've reached MASTER level! Congratulations!{Colors.END}")

    # Achievements
    achievement_pattern = r'- \[x\].*?Achievement'
    achievements_earned = len(re.findall(achievement_pattern, content, re.IGNORECASE))
    print(f"\n{Colors.BOLD}Achievements Unlocked:{Colors.END} {Colors.CYAN}{achievements_earned}{Colors.END} / 30\n")

    # Boss Battles
    boss_pattern = r'- \[x\].*?Boss Battle|The (Configuration Quest|Multi-Modal Master|Integration Gauntlet|Production Gauntlet|Transformation Quest).*?\[x\]'
    boss_battles = len(re.findall(boss_pattern, content, re.IGNORECASE))
    print(f"{Colors.BOLD}Boss Battles Completed:{Colors.END} {Colors.RED}{boss_battles}{Colors.END} / 5\n")

    # Easter Eggs
    easter_egg_pattern = r'- \[x\].*?Easter Egg'
    easter_eggs = len(re.findall(easter_egg_pattern, content, re.IGNORECASE))
    print(f"{Colors.BOLD}Easter Eggs Found:{Colors.END} {Colors.YELLOW}{easter_eggs}{Colors.END} / 6\n")

    # Motivational message
    print("="*60)
    if total_xp == 0:
        print(f"{Colors.CYAN}🎯 Start your journey! Check out 00-START-HERE.md{Colors.END}")
    elif total_xp < 100:
        print(f"{Colors.CYAN}🌟 Great start! Keep going!{Colors.END}")
    elif total_xp < 300:
        print(f"{Colors.GREEN}💪 You're making solid progress!{Colors.END}")
    elif total_xp < 600:
        print(f"{Colors.GREEN}🚀 You're really mastering this!{Colors.END}")
    elif total_xp < 1000:
        print(f"{Colors.YELLOW}🔥 Almost at Master level!{Colors.END}")
    else:
        print(f"{Colors.BOLD}{Colors.GREEN}🏆 MASTER LEVEL ACHIEVED! You're a Claude Code expert!{Colors.END}")
    print("="*60 + "\n")

if __name__ == "__main__":
    calculate_xp()
