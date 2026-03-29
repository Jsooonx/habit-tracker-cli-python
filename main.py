from storage import load_habits
from habits import add_habit, check_in, delete_habit
from display import view_habits, view_streaks, weekly_summary
from export import export_to_csv
    
def main():
    habits = load_habits()
    
    while True:
        print("=== HABIT TRACKER ===")
        print("1. View all habits")
        print("2. Add new habit")
        print("3. Check in for today")
        print("4. View streaks")
        print("5. Weekly summary")
        print("6. Export to CSV")
        print("7. Delete a habit")
        print("0. Exit")
        
        choice = input("\nChoose an option: ").strip()
        print()
        
        if choice == "1":
            view_habits(habits)
        elif choice == "2":
            add_habit(habits)
        elif choice == "3":
            check_in(habits)
        elif choice == "4":
            view_streaks(habits)
        elif choice == "5":
            weekly_summary(habits)
        elif choice == "6":
            export_to_csv(habits)
        elif choice == "7":
            delete_habit(habits)
        elif choice == "0":
            print("See you later!")
            break
        else:
            print("Invalid option, please try again.\n")

if __name__ == "__main__":
    main()