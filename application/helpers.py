import math
import pathlib
import re
from random import randrange
from typing import Tuple


class InvalidFileException(Exception):
    """
    Raised when the application tries process a file that it can't handle.
    """


Location = Tuple[str, str, float, float]


def parse_file_line(*, file_line: str, line_idx: int) -> Location:
    try:

        state, city, latitude, longitude = re.split(r"\t+", file_line)
    except ValueError as e:
        raise InvalidFileException(
            f"file line {line_idx} must read state, city, latitude, longitude: {e}"
        )

    file_line = [state, city]
    try:
        latitude = float(latitude)
        longitude = float(longitude)
    except ValueError:
        raise InvalidFileException(
            f"Error at file line {line_idx}. latitude/longitude can't be parsed to a float"
        )
    else:
        file_line.append(latitude)
        file_line.append(longitude)
        return tuple(file_line)


def is_valid_file_type(*, file) -> bool:
    path = pathlib.Path(file)
    file_extension = path.suffix
    if not file_extension == ".txt":
        raise InvalidFileException(f"{file} is not a .txt file")
    return True


def is_valid_path_and_file_is_readable(*, file) -> bool:
    path = pathlib.Path(file)
    if not path.exists():
        raise InvalidFileException(f"{file} does not exist")
    if not path.is_file():
        raise InvalidFileException(f"{file} is not a file")
    try:
        with path.open():
            # We call a method from the Path class to assess if we are able to read from the file
            _ = path.read_text()
    except Exception as e:
        raise InvalidFileException(f"file is not readable: {e}")

    # If we have not raised an exception by this stage we can be confident that the file exists
    # and we can read from it.
    return True


def compute_euclidean_distance(
    *, city_a_lat: float, city_a_long: float, city_b_lat: float, city_b_long: float
) -> float:
    return math.sqrt((city_a_lat - city_b_lat) ** 2 + (city_a_long - city_b_long) ** 2)


def generate_random_int(*, max_random_number):
    return randrange(0, max_random_number)
