import os

import pytest

from application import cities_interface
from tests import helpers as test_helpers

DIR = os.path.dirname(os.path.abspath(__file__))


def test_read_cities_passes():
    """
    Test read_cities reads in a text file and returns a road map.
    """
    test_file = os.path.join(DIR, "fixtures/test_city_data.txt")

    expected_road_map = [
        ("Alabama", "Montgomery", 32.361538, -86.279118),
        ("Alaska", "Juneau", 58.301935, -134.41974),
        ("Arizona", "Phoenix", 33.448457, -112.073844),
    ]
    assert cities_interface.read_cities(file_name=test_file) == expected_road_map


def test_read_cities_fails(capsys):
    """
    Test read_cities returns InvalidFileException when it reads in a bad file.
    """
    bad_file = os.path.join(DIR, "fixtures/test_bad_city_data.txt")
    cities_interface.read_cities(file_name=bad_file)
    expected_string = (
        "file line 2 must read state, city, latitude, longitude.\nError: not "
        "enough values to unpack (expected 4, got 3)\n"
    )
    captured_out = capsys.readouterr()
    assert captured_out.out == test_helpers.format_string(expected_string)


@pytest.mark.parametrize(
    "road_map, result",
    [
        pytest.param(test_helpers.initialise_test_road_map(0), 38.528),
        pytest.param(test_helpers.initialise_test_road_map(1), 43.316),
        pytest.param(test_helpers.initialise_test_road_map(2), 113.398),
        pytest.param(test_helpers.initialise_test_road_map(3), 148.578),
        pytest.param(test_helpers.initialise_test_road_map(4), 181.49),
    ],
)
def test_compute_total_distance(road_map, result):
    """
    Test that the correct distance between a passed in road map is computed correctly.

    :param road_map: A list of state, city, latitude, longitude tuples.
    :param result: A float of the sum distances of all the connections in the road_map i.e. the
    distance between the cities.
    """
    assert cities_interface.compute_total_distance(road_map=road_map) == pytest.approx(
        result, 0.01
    )


@pytest.mark.parametrize(
    "road_map, index_1, index_2, result",
    [
        pytest.param(
            test_helpers.initialise_test_road_map(0), 1, 1, test_helpers.swap_city_result(0)
        ),
        pytest.param(
            test_helpers.initialise_test_road_map(1), 1, 2, test_helpers.swap_city_result(1)
        ),
        pytest.param(
            test_helpers.initialise_test_road_map(2), 2, 0, test_helpers.swap_city_result(2)
        ),
        pytest.param(
            test_helpers.initialise_test_road_map(3), 2, 1, test_helpers.swap_city_result(3)
        ),
        pytest.param(
            test_helpers.initialise_test_road_map(4), 1, 3, test_helpers.swap_city_result(4)
        ),
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
    mock_road_map, mock_distance = result
    road_map, distance = cities_interface.swap_cities(
        road_map=road_map, index_1=index_1, index_2=index_2
    )
    assert pytest.approx(mock_distance, 0.01) == distance
    assert mock_road_map == road_map


@pytest.mark.parametrize(
    "road_map, shifted_road_map",
    [
        pytest.param(test_helpers.initialise_test_road_map(0), test_helpers.shift_city_result(0)),
        pytest.param(test_helpers.initialise_test_road_map(1), test_helpers.shift_city_result(1)),
        pytest.param(test_helpers.initialise_test_road_map(2), test_helpers.shift_city_result(2)),
        pytest.param(test_helpers.initialise_test_road_map(3), test_helpers.shift_city_result(3)),
        pytest.param(test_helpers.initialise_test_road_map(4), test_helpers.shift_city_result(4)),
    ],
)
def test_shift_cities(road_map, shifted_road_map):
    """
    For a given road map shift every city forward one position. The city at the end of the road
    map assumes the first position.

    :param road_map: A list of state, city, latitude, longitude tuples.
    :param shifted_road_map: A list of state, city, latitude, longitude tuples.
    """
    assert cities_interface.shift_cities(road_map=road_map) == shifted_road_map
