import json
import os

DATA_FILE = "data/habits.json"

def load_habits():
    if not os.path.exists(DATA_FILE):
        return {}
    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
            if not isinstance(data, dict):
                raise ValueError("Invalid data format.")
            return data
    except json.JSONDecodeError:
        print("Warning: habits.json is corrupted. Starting with empty data.")
        _backup_corrupted_file()
        return {}
    except ValueError as e:
        print(f"Warning: {e} Starting with empty data.")
        _backup_corrupted_file()
        return {}
    except OSError as e:
        print(f"Error reading data file: {e}")
        return {}
     
def save_habits(habits):
    try:
        os.makedirs("data", exist_ok=True)
        tmp_file = DATA_FILE + ".tmp"
        with open(DATA_FILE, "w") as f:
            json.dump(habits, f, indent=2)
        os.replace(tmp_file, DATA_FILE)
    except OSError as e:
        print(f"Error saving data: {e}")

def _backup_corrupted_file():
    try:
        backup = DATA_FILE + ".corrupted"
        os.replace(DATA_FILE, backup)
        print(f"Corrupted file backed up as '{backup}'.\n")
    except OSError:
        pass