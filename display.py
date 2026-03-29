from datetime import date, timedelta
from habits import get_streak, get_longest_streak
from colorama import init, Fore, Style

init(autoreset=True)

def view_habits(habits):
    if not habits:
        print(Fore.YELLOW + "No habits yet. Add one first!\n")
        return
    print(Fore.CYAN + "\n=== Your Habits ===")
    for i, name in enumerate(habits, start=1):
        total = len(habits[name]["checkins"])
        print(f"{i}. {Style.BRIGHT}{name}{Style.RESET_ALL} — {total} check-in(s)")
    print()

def view_streaks(habits):
    if not habits:
        print(Fore.YELLOW + "No habits yet. Add one first!\n")
        return
    print(Fore.CYAN + "=== Streaks ===")
    for name, data in habits.items():
        streak = get_streak(data["checkins"])
        longest = get_longest_streak(data["checkins"])
        total = len(data["checkins"])
        fire = "🔥" * min(streak, 5)

        if streak >= 7:
            streak_color = Fore.GREEN
        elif streak >= 3:
            streak_color = Fore.YELLOW
        elif streak == 0:
            streak_color = Fore.RED
        else:
            streak_color = Fore.WHITE

        print(
            f"{Style.BRIGHT}{name}{Style.RESET_ALL}: "
            f"{streak_color}{streak} day(s) streak{Style.RESET_ALL} {fire} | "
            f"longest: {Fore.CYAN}{longest} day(s){Style.RESET_ALL} | "
            f"{total} total check-in(s)"
        )
    print()

def weekly_summary(habits):
    if not habits:
        print(Fore.YELLOW + "No habits yet. Add one first!\n")
        return
    today = date.today()
    week_dates = {str(today - timedelta(days=i)) for i in range(7)}
    print(Fore.CYAN + "=== Weekly Summary (Last 7 Days) ===")
    for name, data in habits.items():
        count = len([d for d in data["checkins"] if d in week_dates])
        bar = Fore.GREEN + "█" * count + Fore.RED + "░" * (7 - count) + Style.RESET_ALL
        print(f"{Style.BRIGHT}{name}{Style.RESET_ALL}: {bar} {count}/7")
    print()