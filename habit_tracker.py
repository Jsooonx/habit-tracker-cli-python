import json
import os
from datetime import date

DATA_FILE = "data/habits.json"

def load_habits():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as f:
        return json.load(f)
    
def save_habits(habits):
    os.makedirs("data", exist_ok=True)
    with open(DATA_FILE, "w") as f:
        json.dump(habits, f, indent=2)
        
def add_habits(habits):
    name = input("New habit name: ").strip()
    if not name:
        print("Habit name cannot be empty.")
        return
    if name in habits:
        print(f"Habit '{name}' already exists.")
    habits[name] = {
        "created": str(date.today()),
        "checkins": []
    }
    save_habits(habits)
    print(f"Habit '{name}' added successfully!")
    
def view_habits(habits):
    if not habits:
        print("No habits yet. Add one first!")
        return
    print("\n=== Your Habits ===")
    for i, name in enumerate(habits, start=1):
        total = len(habits[name]["checkins"])
        print(f"{i}. {name} - {total} check-in(s)")
        
def find_habit(habits, name):
    return next((k for k in habits if k.lower() == name.lower()), None)

def check_in(habits):
    if not habits:
        print("No habits yet. Add one first!\n")
        return
    
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
    
def get_streak(checkins):
    if not checkins:
        return 0
    
    sorted_dates = sorted(date.fromisoformat(d) for d in checkins)
    today = date.today()
    
    # Streak valid if only check-in today or yesterday
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

def view_streaks(habits):
    if not habits:
        print("No habits yet. Add one first!\n")
        return
    
    print("=== Streaks ===")
    for name, data in habits.items():
        streak = get_streak(data["checkins"])
        total = len(data["checkins"])
        fire = "🔥" * min(streak, 5)
        print(f"{name}: {streak} day(s) streak {fire} | {total} total check-in(s)")
    print()
        
def main():
    habits = load_habits()
    
    while True:
        print("=== HABIT TRACKER ===")
        print("1. View all habits")
        print("2. Add new habit")
        print("3. Check in for today")
        print("4. View streaks")
        print("5. Export to CSV")
        print("6. Delete a habit")
        print("0. Exit")
        
        choice = input("\nChoose an option: ").strip()
        print()
        
        if choice == '1':
            view_habits(habits)
        elif choice == '2':
            add_habits(habits)
        elif choice == '3':
            check_in(habits)
        elif choice == '4':
            view_streaks(habits)
        elif choice in ("5", "6"):
            print("This feature is coming soon!\n")
        elif choice == '0':
            print("See you later!")
            break
        else:
            print("Invalid option, please try again.\n")

if __name__ == "__main__":
    main()