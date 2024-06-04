
import json
from .pathworks import get_project_relative_filepath


def read_project_file(filename: str, relative_path: str) -> str:
    file_path = get_project_relative_filepath(filename, relative_path)
    if file_path is None:
        raise FileNotFoundError
    with open(file_path, "r", encoding="UTF-8") as file:
        return file.read()


def write_project_file(filename: str, relative_path: str, content: str) -> None:
    file_path = get_project_relative_filepath(filename, relative_path)
    if file_path is None:
        raise FileNotFoundError
    with open(file_path, "w", encoding="UTF-8") as file:
        file.write(content)


def get_json(filename: str, relative_path: str) -> dict:
    if not filename.endswith(".json"):
        raise ValueError("Invalid JSON Filename")
    file_content = read_project_file(filename, relative_path)
    return json.loads(file_content)


def save_json(filename: str, relative_path: str, data: dict) -> None:
    if not filename.endswith(".json"):
        raise ValueError("Invalid JSON Filename")
    json_string = json.dumps(data, indent=4)
    write_project_file(filename, relative_path, json_string)
