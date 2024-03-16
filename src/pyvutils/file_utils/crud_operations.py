
# Local Imports
from pyvutils.path_utils.project_helpers import get_project_relative_file_path


def get_file_content(filename: str, relative_path: str) -> str:
    file_path = get_project_relative_file_path(filename, relative_path)
    with open(file_path, "r", encoding="UTF-8") as file:
        return file.read()


def save_file_content(filename: str, relative_path: str, content: str) -> None:
    file_path = get_project_relative_file_path(filename, relative_path)
    with open(file_path, "w", encoding="UTF-8") as file:
        file.write(content)
