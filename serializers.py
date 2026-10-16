
import json
from pathlib import Path


def to_json(data, indent=2):
    """Convert Python data into a JSON string."""
    return json.dumps(data, indent=indent)


def from_json(json_string):
    """Convert a JSON string into Python data."""
    return json.loads(json_string)


def save_json(data, filename):
    """Save Python data to a JSON file."""
    path = Path(filename)

    with path.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)


def load_json(filename):
    """Load JSON data from a file."""
    path = Path(filename)

    with path.open("r", encoding="utf-8") as file:
        return json.load(file)
