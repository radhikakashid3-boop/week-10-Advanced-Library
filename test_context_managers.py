
from pathlib import Path

from src.my_advanced_lib.core.context_managers import (
    SafeFileHandler,
    temporary_setting,
    temporary_directory,
)


def test_safe_file_handler(tmp_path):
    file_path = tmp_path / "sample.txt"

    with SafeFileHandler(file_path, "w") as file:
        file.write("Hello Python")

    with SafeFileHandler(file_path, "r") as file:
        assert file.read() == "Hello Python"

    assert file.closed


def test_temporary_setting():
    class Config:
        mode = "normal"

    config = Config()

    with temporary_setting(config, "mode", "temporary"):
        assert config.mode == "temporary"

    assert config.mode == "normal"


def test_temporary_setting_restores_after_exception():
    class Config:
        mode = "normal"

    config = Config()

    try:
        with temporary_setting(config, "mode", "temporary"):
            raise ValueError("Test error")
    except ValueError:
        pass

    assert config.mode == "normal"


def test_temporary_directory(tmp_path):
    with temporary_directory(tmp_path) as directory:
        assert directory.exists()
        assert directory.is_dir()

    assert not directory.exists()

