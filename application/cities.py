import pathlib
from typing import List, Tuple

from . import helpers

RoadMap = List[Tuple[str, str, float, float]]


def read_cities(*, file_name) -> RoadMap:
    """
    Read in the cities from the given `file_name`, and return
    them as a list of four-tuples.

    :param file_name: file path of city data.
    :returns RoadMap -> [(state, city, latitude, longitude), ...]

    """
    # Test valid file.
    try:
        is_valid_file(file_name=file_name)
    except Exception as e:
        raise Exception(f"The program received bad file input: {e}")

    # Test valid file line and parse lines.
    road_map = build_file_lines(file_name=file_name)

    # A road map needs to have a length of at least 2.
    if len(road_map) < 2:
        raise helpers.InvalidFileException()

    return road_map


def build_file_lines(*, file_name) -> RoadMap:
    """
    Builds a road map from the passed in file.

    :param file_name: file path of city data.
    :returns RoadMap -> [(state, city, latitude, longitude), ...]
    """
    road_map = list()
    line_idx = None
    try:
        path = pathlib.Path(file_name)
        lines = path.read_text().splitlines()
        for idx, line in enumerate(lines):
            line_idx = idx
            road_map.append(helpers.parse_file_line(file_line=line))
    except (Exception, helpers.InvalidFileException) as e:
        raise helpers.InvalidFileException(f"Not able to parse file line {line_idx}: {e}")
    return road_map


def is_valid_file(*, file_name):
    """
    Check if the passed in file is valid. We check the following:
        - Does the file exist and we can open it
        - Is the file a valid extension for this application (.txt)
    :param file_name: File to be validated
    """
    helpers.is_valid_path_and_file_is_readable(file=file_name)
    helpers.is_valid_file_type(file=file_name)


def print_cities(*, road_map: RoadMap):
    """
    Prints a list of cities, along with their locations.
    Print only one or two digits after the decimal point.
    """
    pass


def compute_total_distance(*, road_map: RoadMap) -> float:
    """
    Returns, as a floating point number, the sum of the distances of all
    the connections in the `road_map`. Remember that it's a cycle, so that
    (for example) in the initial `road_map`, Wyoming connects to Alabama...
    """
    return 1.0


def swap_cities(*, road_map: RoadMap, index_1: int, index_2: int) -> Tuple[RoadMap, float]:
    """
    Take the city at location `index` in the `road_map`, and the
    city at location `index2`, swap their positions in the `road_map`,
    compute the new total distance, and return the tuple

        (new_road_map, new_total_distance)

    Allow for the possibility that `index1=index2`,
    and handle this case correctly.
    """
    new_road_map = [("foo", "bar", 1, 2), ("bing", "bong", 3, 4)]
    new_total_distance = 10
    return new_road_map, new_total_distance


def shift_cities(*, road_map: RoadMap) -> RoadMap:
    """
    For every index i in the `road_map`, the city at the position i moves
    to the position i+1. The city at the last position moves to the position
    0. Return the new road map.
    """
    new_road_map = [("foo", "bar", 1, 2), ("bing", "bong", 3, 4)]
    return new_road_map


def find_best_cycle(*, road_map: RoadMap) -> RoadMap:
    """
    Using a combination of `swap_cities` and `shift_cities`,
    try `10000` swaps/shifts, and each time keep the best cycle found so far.
    After `10000` swaps/shifts, return the best cycle found so far.
    Use randomly generated indices for swapping.
    """
    pass


def print_map(*, road_map: RoadMap):
    """
    Prints, in an easily understandable format, the cities and
    their connections, along with the cost for each connection
    and the total cost.
    """
    pass


def main():
    """
    Reads in, and prints out, the city data, then creates the "best"
    cycle and prints it out.
    """
    pass


if __name__ == "__main__":  # keep this in
    main()
