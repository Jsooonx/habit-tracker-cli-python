import json
import os

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