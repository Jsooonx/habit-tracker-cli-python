from datetime import date, timedelta
from storage import load_habits, save_habits

def find_habit(habits, name):
    return next((k for k in habits if k.lower() == name.lower()), None)

def add_habit(habits):
    name = input("New habit name: ").strip()
    if not name:
        print("Habit name cannot be empty.\n")
        return
    if find_habit(habits, name):
        print(f"Habit '{name}' already exists.\n")
        return
    habits[name] = {
        "created": str(date.today()),
        "checkins": []
    }
    save_habits(habits)
    print(f"Habit '{name}' added successfully!\n")

def check_in(habits):
    if not habits:
        print("No habits yet. Add one first!\n")
        return
    from display import view_habits
    view_habits(habits)
    name = input("Enter habit name to check in: ").strip()
    match = find_habit(habits, name)
    if match is None:
        print(f"Habit '{name}' not found.\n")
        return
    today = str(date.today())
    if today in habits[match]["checkins"]:
        print(f"You already checked in '{match}' today!\n")
        return
    habits[match]["checkins"].append(today)
    save_habits(habits)
    print(f"✓ Checked in '{match}' for {today}!\n")

def delete_habit(habits):
    if not habits:
        print("No habits yet. Add one first!\n")
        return
    from display import view_habits
    view_habits(habits)
    name = input("Enter habit name to delete: ").strip()
    match = find_habit(habits, name)
    if match is None:
        print(f"Habit '{name}' not found.\n")
        return
    confirm = input(f"Are you sure you want to delete '{match}'? (y/n): ").strip().lower()
    if confirm != "y":
        print("Cancelled.\n")
        return
    del habits[match]
    save_habits(habits)
    print(f"Habit '{match}' deleted.\n")

def get_streak(checkins):
    if not checkins:
        return 0
    sorted_dates = sorted(date.fromisoformat(d) for d in checkins)
    today = date.today()
    if (today - sorted_dates[-1]).days > 1:
        return 0
    streak = 1
    for i in range(len(sorted_dates) - 1, 0, -1):
        diff = (sorted_dates[i] - sorted_dates[i - 1]).days
        if diff == 1:
            streak += 1
        else:
            break
    return streak

def get_longest_streak(checkins):
    if not checkins:
        return 0
    sorted_dates = sorted(date.fromisoformat(d) for d in checkins)
    longest = 1
    current = 1
    for i in range(1, len(sorted_dates)):
        diff = (sorted_dates[i] - sorted_dates[i - 1]).days
        if diff == 1:
            current += 1
            longest = max(longest, current)
        else:
            current = 1
    return longest