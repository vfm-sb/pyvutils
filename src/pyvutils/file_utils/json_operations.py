
# Built-in Modules
import json

# Local Imports
from pyvutils.file_utils.crud_operations import get_file_content, save_file_content


def get_json_file(filename: str, relative_path: str) -> dict:
    if not filename.endswith(".json"):
        raise ValueError("Invalid JSON Filename")
    file_content = get_file_content(filename, relative_path)
    return json.loads(file_content)


def save_json_file(filename: str, relative_path: str, data: dict) -> None:
    if not filename.endswith(".json"):
        raise ValueError("Invalid JSON Filename")
    json_string = json.dumps(data, indent=4)
    save_file_content(filename, relative_path, json_string)
