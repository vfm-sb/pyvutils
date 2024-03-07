
# Built-in Modules
from pathlib import Path


def get_project_root_path() -> Path | None:
    marker_filename = "pyproject.toml"
    current_directory = Path.cwd()
    home_directory = Path.home()
    while current_directory != home_directory:
        marker_file = current_directory / marker_filename
        if marker_file.is_file():
            return current_directory
        current_directory = current_directory.parent
    return None


def get_project_relative_folder_path(relative_path: str) -> Path | None:
    project_root = get_project_root_path()
    if project_root is None:
        return None
    return project_root / relative_path


def get_project_relative_file_path(filename: str, relative_path: str) -> Path | None:
    folder_path = get_project_relative_folder_path(relative_path)
    if folder_path is None:
        return None
    return folder_path / filename
