# Habit Tracker CLI

A command-line habit tracker built with Python. Track your daily habits, monitor streaks, and export your progress to CSV.

## Features

- Add and delete habits
- Daily check-in (case-insensitive input)
- Current streak and longest streak tracking
- Weekly summary with a visual progress bar
- Export habit data to CSV

## Getting Started

No external libraries required — only Python 3 standard library.
```bash
git clone https://github.com/yourusername/habit-tracker-cli.git
cd habit-tracker-cli
python habit_tracker.py
```

## Usage
```
=== HABIT TRACKER ===
1. View all habits
2. Add new habit
3. Check in for today
4. View streaks
5. Weekly summary
6. Export to CSV
7. Delete a habit
0. Exit
```

## Data Storage

Habits are saved locally in `data/habits.json`. This file is created automatically on first run.

## Export

Use option 6 to export your data. A CSV file named `habits_export_YYYY-MM-DD.csv` will be created in the project root.

Example output:
| Habit | Created | Total Check-ins | Current Streak | Last Check-in |
|---|---|---|---|---|
| Working out | 2026-03-28 | 2 | 2 | 2026-03-29 |
| Study | 2026-03-28 | 1 | 1 | 2026-03-28 |

---

Project structure:
```
habit-tracker-cli/
├── habit_tracker.py
├── .gitignore
├── README.md
└── data/
    └── habits.json
```