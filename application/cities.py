from typing import List, Tuple


RoadMap = List[Tuple[str, str, float, float]]


def read_cities(*, file_name) -> RoadMap:
    """
    Read in the cities from the given `file_name`, and return
    them as a list of four-tuples:

      [(state, city, latitude, longitude), ...]

    Use this as your initial `road_map`, that is, the cycle

      Alabama -> Alaska -> Arizona -> ... -> Wyoming -> Alabama.
    """
    pass


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
