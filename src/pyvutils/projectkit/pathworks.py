
# Built-in Modules
from pathlib import Path


def get_project_path(marker: str = "pyproject.toml") -> Path | None:
    current = Path(__file__).parent
    home = Path.home()
    while current != home:
        marker_file = current / marker
        if marker_file.is_file():
            return current
        current = current.parent
    return None


def get_project_relative_path(relative_path: str) -> Path | None:
    project_root = get_project_path()
    if project_root is None:
        return None
    return project_root / relative_path


def get_project_relative_filepath(filename: str, relative_path: str) -> Path | None:
    folder_path = get_project_relative_path(relative_path)
    if folder_path is None:
        return None
    return folder_path / filename
