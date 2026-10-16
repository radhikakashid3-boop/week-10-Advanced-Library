
from contextlib import contextmanager
from pathlib import Path


class SafeFileHandler:
    """Read and write files safely using a context manager."""

    def __init__(self, filename, mode="r", encoding="utf-8"):
        self.filename = filename
        self.mode = mode
        self.encoding = encoding
        self.file = None

    def __enter__(self):
        self.file = open(
            self.filename,
            self.mode,
            encoding=self.encoding
        )
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file is not None:
            self.file.close()

        # Do not suppress exceptions
        return False


@contextmanager
def temporary_setting(obj, attribute, temporary_value):
    """Temporarily change an object's attribute."""

    original_value = getattr(obj, attribute)

    try:
        setattr(obj, attribute, temporary_value)
        yield obj
    finally:
        setattr(obj, attribute, original_value)


@contextmanager
def temporary_directory(path):
    """Create a directory and remove it when finished."""

    import tempfile
    import shutil

    directory = Path(
        tempfile.mkdtemp(dir=path)
    )

    try:
        yield directory
    finally:
        shutil.rmtree(directory, ignore_errors=True)
