import shutil
import os
from typing import Callable, Any
from pathlib import Path

def is_decorator(original_function: Callable[[], Any]) -> Callable[[], Any]:
    def wrapper(*args, **kwargs):
        return original_function(*args, **kwargs)
    return wrapper

@is_decorator
def file_operation(original_function) -> Callable[[], Any]:
    def wrapper(*args, **kwargs):
        return original_function(*args, **kwargs)
    return wrapper

@is_decorator
def folder_operation(original_function) -> Callable[[], Any]:
    def wrapper(*args, **kwargs):
        return original_function(*args, **kwargs)
    return wrapper


class FileOperation:
    @staticmethod
    @file_operation
    def file_exists(file_path: str) -> bool:
        return os.path.isfile(Path(file_path))

    @staticmethod
    @file_operation
    def write_file(file_path: str, content: str, mode="w") -> None:
        with open(Path(file_path), mode) as file:
            file.write(content)

    @staticmethod
    @file_operation
    def read_file(file_path: str, mode="r") -> str:
        with open(Path(file_path), mode) as file:
            return file.read()

    @staticmethod
    @file_operation
    def move_file(old_file_path: str, new_file_path: str) -> str:
        shutil.move(Path(old_file_path), Path(new_file_path))

    @staticmethod
    @file_operation
    def delete_file(file_path: str) -> None:
        return Path(file_path).unlink()

class FolderOperation:
    @staticmethod
    @folder_operation
    def folder_exists(folder_path: str) -> bool:
        return os.path.isdir(Path(folder_path))

    @staticmethod
    @folder_operation
    def create_folder(folder_path: str) -> None:
        os.mkdir(Path(folder_path))

    @staticmethod
    @folder_operation
    def rename_folder(old_folder_path: str, new_folder_path: str) -> None:
        os.rename(Path(old_folder_path), Path(new_folder_path))

    @staticmethod
    @folder_operation
    def move_folder(old_folder_path: str, new_folder_path: str) -> None:
        shutil.move(Path(old_folder_path), Path(new_folder_path))

    @staticmethod
    @folder_operation
    def delete_folder(folder_path: str) -> None:
        shutil.rmtree(Path(folder_path))
