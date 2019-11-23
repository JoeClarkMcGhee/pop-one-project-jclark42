import pytest

from application import cities
from application import helpers as app_helpers
from tests import helpers as test_helpers


def test_read_cities_passes():
    """
    Test read_cities reads in a text file and returns a road map.
    """
    test_file = "fixtures/test_city_data.txt"
    expected_road_map = [
        ("Alabama", "Montgomery", 32.361538, -86.279118),
        ("Alaska", "Juneau", 58.301935, -134.41974),
        ("Arizona", "Phoenix", 33.448457, -112.073844),
    ]
    assert cities.read_cities(file_name=test_file) == expected_road_map


def test_read_cities_fails():
    """
    Test read_cities returns InvalidFileException when it reads in a bad file.
    """
    bad_file = "fixtures/test_bad_city_data.txt"
    with pytest.raises(app_helpers.InvalidFileException):
        cities.read_cities(file_name=bad_file)


@pytest.mark.parametrize(
    "road_map, result",
    [
        pytest.param(test_helpers.initialise_test_case(0), 38.528),
        pytest.param(test_helpers.initialise_test_case(1), 38.528),
        pytest.param(test_helpers.initialise_test_case(2), 38.528),
        pytest.param(test_helpers.initialise_test_case(3), 38.528),
        pytest.param(test_helpers.initialise_test_case(4), 38.528),
    ],
)
def test_compute_total_distance(road_map, result):
    """
    Test that the correct distance between a passed in road map is computed correctly.

    :param road_map: A list of state, city, latitude, longitude tuples.
    :param result: A float of the sum distances of all the connections in the road_map i.e. the
    distance between the cities.
    """
    assert cities.compute_total_distance(road_map=road_map) == pytest.approx(result, 0.01)


@pytest.mark.parametrize(
    "road_map, index_1, index_2, result",
    [
        pytest.param(test_helpers.initialise_test_case(0), 0, 1, test_helpers.swap_city_result(0)),
        pytest.param(test_helpers.initialise_test_case(1), 1, 2, test_helpers.swap_city_result(1)),
        pytest.param(test_helpers.initialise_test_case(2), 2, 0, test_helpers.swap_city_result(2)),
        pytest.param(test_helpers.initialise_test_case(3), 0, 1, test_helpers.swap_city_result(3)),
        pytest.param(test_helpers.initialise_test_case(4), 0, 2, test_helpers.swap_city_result(4)),
    ],
)
def test_swap_cities(road_map, index_1, index_2, result):
    """
    Test that the cites at index_1 and index_2 are swapped in the returned road map and the
    distance for the new road_map is computed correctly.

    :param road_map: A list of state, city, latitude, longitude tuples.
    :param index_1: Integer to be used as an index on the road map.
    :param index_2: Integer to be used as an index on the road map.
    """
    assert cities.swap_cities(road_map=road_map, index_1=index_1, index_2=index_2) == result


@pytest.mark.parametrize(
    "road_map, shifted_road_map",
    [
        pytest.param(test_helpers.initialise_test_case(0), test_helpers.shift_city_result(0)),
        pytest.param(test_helpers.initialise_test_case(0), test_helpers.shift_city_result(1)),
        pytest.param(test_helpers.initialise_test_case(0), test_helpers.shift_city_result(2)),
        pytest.param(test_helpers.initialise_test_case(0), test_helpers.shift_city_result(3)),
        pytest.param(test_helpers.initialise_test_case(0), test_helpers.shift_city_result(4)),
    ],
)
def test_shift_cities(road_map, shifted_road_map):
    """
    For a given road map shift every city forward one position. The city at the end of the road
    map assumes the first position.

    :param road_map: A list of state, city, latitude, longitude tuples.
    :param shifted_road_map: A list of state, city, latitude, longitude tuples.
    """
    assert cities.shift_cities(road_map=road_map) == shifted_road_map
