
# Local Imports
from pyvutils.path_utils.project_helpers import get_project_relative_file_path


def get_file_content(filename: str, relative_path: str) -> str:
    filepath = get_project_relative_file_path(filename, relative_path)
    with open(filepath, "r", encoding="UTF-8") as file:
        return file.read()


def save_file_content(filename: str, relative_path: str, content: str) -> None:
    filepath = get_project_relative_file_path(filename, relative_path)
    with open(filepath, "w", encoding="UTF-8") as file:
        file.write(content)
