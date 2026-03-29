import csv
from datetime import date
from habits import get_streak

def export_to_csv(habits):
    if not habits:
        print("No habits yet. Add one first!\n")
        return
    
    filename = f"habits-export_{date.today()}.csv"
    try: 
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Habit", "Created", "Total Check-ins", "Current Streak", "Last Check-in"])
            
            for name, data in habits.items():
                total = len(data["checkins"])
                streak = get_streak(data["checkins"])
                last = data["checkins"][-1] if data["checkins"] else "Never"
                writer.writerow([name, data["created"], total, streak, last])
            
        print(f"Exported to '{filename}' succcessfully!\n")
    except OSError as e:
        print(f"Error exporting file: {e}\n")