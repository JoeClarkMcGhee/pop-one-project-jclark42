import copy
import pathlib
from typing import List, Tuple

from . import helpers
from .best_cycle_data_container import BestCycleContainer as Container

RoadMap = List[Tuple[str, str, float, float]]


def read_cities(*, file_name) -> RoadMap or None:
    """
    Read in the cities from the given `file_name`, and return
    them as a list of four-tuples.

    :param file_name: file path of city data.
    :returns RoadMap -> [(state, city, latitude, longitude), ...]

    """
    # Test valid file.
    if not is_valid_file(file_name=file_name):
        return

    # Test valid file line and parse lines.
    road_map, err = build_file_lines(file_name=file_name)
    if err:
        return
    if len(road_map) < 2:
        print("A road map needs to have a length of at least 2")
        return

    return road_map


def build_file_lines(*, file_name) -> Tuple[RoadMap, bool]:
    """
    Builds a road map from the passed in file.

    :param file_name: file path of city data.
    :returns RoadMap -> [(state, city, latitude, longitude), ...]
    """
    road_map = list()
    path = pathlib.Path(file_name)
    lines = path.read_text().splitlines()
    err = False
    for idx, line in enumerate(lines):
        if line == "":
            continue
        parsed_file_line = helpers.parse_file_line(file_line=line, line_idx=idx)
        if not parsed_file_line:
            err = True
            break
        road_map.append(parsed_file_line)
    return road_map, err


def is_valid_file(*, file_name):
    """
    Check if the passed in file is valid. We check the following:
        - Does the file exist and we can open it
        - Is the file a valid extension for this application (.txt)
    :param file_name: File to be validated
    """
    is_valid_path_and_file = helpers.is_valid_path_and_file_is_readable(file=file_name)
    is_valid_file_type = helpers.is_valid_file_type(file=file_name)

    if is_valid_path_and_file and is_valid_file_type:
        return True


def print_cities(*, road_map: RoadMap):
    """
    Prints a list of cities, along with their locations.
    :param road_map: RoadMap -> [(state, city, latitude, longitude), ...]
    """
    road_map_to_print = ""
    for _, city, lat, long in road_map:
        road_map_to_print += f"city: {city} location: {round(lat, 2)}, {round(long, 2)}\n"
    print(road_map_to_print.rstrip())


def compute_total_distance(*, road_map: RoadMap) -> float:
    """
    Returns, as a floating point number, the sum of the distances of all the connections in the
    `road_map`. The distance is calculated as a full cycle i.e. the last city connects to the
    first.
    :param road_map: RoadMap -> [(state, city, latitude, longitude), ...]
    """
    total_distance = 0
    index_a = 0
    index_b = 1
    connections = len(road_map)
    while connections:
        _, _, city_a_lat, city_a_long = road_map[index_a]
        try:
            _, _, city_b_lat, city_b_long = road_map[index_b]
        except IndexError:
            _, _, city_b_lat, city_b_long = road_map[0]
        total_distance += helpers.compute_euclidean_distance(
            city_a_lat=city_a_lat,
            city_a_long=city_a_long,
            city_b_lat=city_b_lat,
            city_b_long=city_b_long,
        )
        index_a += 1
        index_b += 1
        connections -= 1

    return total_distance


def swap_cities(*, road_map: RoadMap, index_1: int, index_2: int) -> Tuple[RoadMap, float]:
    """
    Swap the city at index_1 with index_2.

    :param road_map: RoadMap -> [(state, city, latitude, longitude), ...]
    :param index_1: A int used to index the road_map
    :param index_2: A int used to index the road_map
    """
    if index_1 == index_2:
        return road_map, compute_total_distance(road_map=road_map)
    else:
        city_a = road_map[index_1]
        city_b = road_map[index_2]

        for idx, _ in enumerate(road_map):
            if idx == index_1:
                road_map[idx] = city_b
            if idx == index_2:
                road_map[idx] = city_a

        return road_map, compute_total_distance(road_map=road_map)


def shift_cities(*, road_map: RoadMap) -> RoadMap:
    """
    For every index i in the `road_map`, the city at the position i moves
    to the position i+1. The city at the last position moves to the position
    0.
    :param road_map: RoadMap -> [(state, city, latitude, longitude), ...]
    """
    last_city = road_map.pop()
    road_map.insert(0, last_city)
    return road_map


def find_best_cycle(*, road_map: RoadMap) -> RoadMap:
    """
    Using a combination of `swap_cities` and `shift_cities`, find the best cycle and return the
    corresponding road map.
    :param road_map: RoadMap -> [(state, city, latitude, longitude), ...]
    """
    best_cycle = Container()
    # Set best_cycle with values from the unoptimised road map.
    best_cycle.set_distance_and_road_map(
        road_map=road_map, distance=compute_total_distance(road_map=road_map)
    )
    for idx in range(10000):
        copied_map = copy.deepcopy(best_cycle.best_road_map)
        index_1 = helpers.generate_random_int(max_random_number=len(road_map))
        index_2 = helpers.generate_random_int(max_random_number=len(road_map))
        swapped_road_map, distance = swap_cities(
            road_map=copied_map, index_1=index_1, index_2=index_2
        )
        if best_cycle.should_update_best_distance(distance=distance):
            best_cycle.set_distance_and_road_map(distance=distance, road_map=swapped_road_map)
        # Shift the cities every 100 iterations.
        if idx % 100 == 0:
            shift_cities(road_map=best_cycle.best_road_map)

    return best_cycle.best_road_map


def print_map(*, road_map: RoadMap):
    """
    Prints the cities and their connections from a passed in road map, along with the distance
    for each connection and the total total distance.

    :param road_map: RoadMap -> [(state, city, latitude, longitude), ...]
    """
    total_distance = 0
    index_a = 0
    index_b = 1
    connections = len(road_map)
    string_to_print = ""
    while connections:
        _, city_a, city_a_lat, city_a_long = road_map[index_a]
        try:
            _, city_b, city_b_lat, city_b_long = road_map[index_b]
        except IndexError:
            _, city_b, city_b_lat, city_b_long = road_map[0]
        distance = helpers.compute_euclidean_distance(
            city_a_lat=city_a_lat,
            city_a_long=city_a_long,
            city_b_lat=city_b_lat,
            city_b_long=city_b_long,
        )
        total_distance += distance
        index_a += 1
        index_b += 1
        connections -= 1
        last_connection_string = (
            f"{index_a}. {city_a} -> {city_b}: Distance {round(distance, 2)}\n"
        )
        string_to_print += last_connection_string
    string_to_print += f"Total distance: {round(total_distance, 2)}"
    print(string_to_print)
