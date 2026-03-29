from datetime import date, timedelta
from habits import get_streak, get_longest_streak

def view_habits(habits):
    if not habits:
        print("No habits yet. Add one first!")
        return
    print("\n=== Your Habits ===")
    for i, name in enumerate(habits, start=1):
        total = len(habits[name]["checkins"])
        print(f"{i}. {name} - {total} check-in(s)")
        
def view_streaks(habits):
    if not habits:
        print("No habits yet. Add one first!\n")
        return

    print("=== Streaks ===")
    for name, data in habits.items():
        streak = get_streak(data["checkins"])
        longest = get_longest_streak(data["checkins"])
        total = len(data["checkins"])
        fire = "🔥" * min(streak, 5)
        print(f"{name}: {streak} day(s) streak {fire} | longest: {longest} day(s) | {total} total check-in(s)")
    print()
    
def weekly_summary(habits):
    if not habits:
        print("No habits yet. Add one first!\n")
        return
    
    today = date.today()
    week_dates = {str(today - timedelta(days=i)) for i in range(7)}
    
    print("=== Weekly Summary (Last 7 Days) ===")
    for name, data in habits.items():
        checkins_this_week = [d for d in data["checkins"] if d in week_dates]
        count = len(checkins_this_week)
        bar = "█" * count + "░" * (7 - count)
        print(f"{name}: {bar} {count}/7")
    print()