class InvalidFileException(Exception):
    """
    Raised when the application tries process a file that it can't handle.
    """


def is_valid_file_line(*, file_line: str) -> bool:
    return True


def is_valid_file_type(*, file) -> bool:
    return True


def is_valid_path_and_file_is_readable(*, file) -> bool:
    return True
