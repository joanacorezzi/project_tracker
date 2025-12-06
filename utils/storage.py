import json
from pathlib import Path

# Base directory of the project 
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"


def load_json(filename):
    #Load JSON data from a file inside the data folder

    file_path = DATA_DIR / filename

    if not file_path.exists():
        #return empty list
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError:
        # return empty list
        data = []

    return data


def save_json(filename, data):
   # Save data as JSON 

    file_path = DATA_DIR / filename

    # Check if the data directory exists
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)