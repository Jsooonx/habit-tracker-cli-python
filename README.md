# Habit Tracker CLI

A command-line habit tracker built with Python. Track your daily habits, monitor streaks, and export your progress to CSV.

## Features

- Add and delete habits
- Daily check-in (case-insensitive input)
- Current streak and longest streak tracking
- Weekly summary with a visual progress bar
- Export habit data to CSV
- Color-coded output with Colorama
- Daily reminders for unchecked habits (with streak-at-risk warning)
- Corrupted data detection with automatic backup

## Requirements

- Python 3.7+
- Colorama

Install dependencies:
```bash
pip install -r requirements.txt
```

## Getting Started
```bash
git clone https://github.com/Jsooonx/habit-tracker-cli.git
cd habit-tracker-cli
pip install -r requirements.txt
python main.py
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

On startup, the app will remind you which habits haven't been checked in yet and warn you if an active streak is at risk.

## Project Structure
```
habit-tracker-cli/
├── main.py         # Entry point and menu loop
├── storage.py      # Load and save JSON data
├── habits.py       # Habit logic (add, delete, check-in, streaks)
├── display.py      # Output formatting and reminders
├── export.py       # CSV export
├── requirements.txt
├── .gitignore
└── data/
    └── habits.json
```

## Data Storage

Habits are saved locally in `data/habits.json`, created automatically on first run. If the file is corrupted, it will be backed up as `habits.json.corrupted` and the app will start fresh.

## Export

Use option 6 to export your data. A CSV file named `habits_export_YYYY-MM-DD.csv` will be created in the project root.

Example output:

| Habit | Created | Total Check-ins | Current Streak | Last Check-in |
|---|---|---|---|---|
| Working out | 2026-03-28 | 5 | 3 | 2026-03-29 |
| Study | 2026-03-28 | 4 | 2 | 2026-03-29 |