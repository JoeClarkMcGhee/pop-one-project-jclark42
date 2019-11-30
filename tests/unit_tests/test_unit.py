import pytest
import os

from application import cities_interface
from application import helpers as app_helpers
from .. import helpers


@pytest.mark.parametrize(
    "file_line",
    [
        pytest.param("1, 2, 3, 4"),
        pytest.param("Alabama	Montgomery	32.361538	"),
        pytest.param("Alabama	32.361538	Montgomery	-86.27"),
        pytest.param("32.361538 Alabama	Montgomery	32.361538"),
    ],
)
def test_is_not_valid_file_line(file_line):
    """
    Tests that a file input line is a valid sting i.e. one that the application is able to parse.
    """
    with pytest.raises(app_helpers.InvalidFileException):
        app_helpers.parse_file_line(file_line=file_line, line_idx=1)


def test_is_valid_file_line():
    file_line = "Alabama	Montgomery	32.361538	-86.279118"
    expected_file_line = ("Alabama", "Montgomery", 32.361538, -86.279118)
    assert app_helpers.parse_file_line(file_line=file_line, line_idx=1) == expected_file_line


def test_not_valid_file_type_fails():
    """
    Test that the application raises an InvalidFileException when it tires to process a file
    with an extension other than '.csv'
    """
    test_file = "fixtures/test_bad_extension_city_data.tsv"
    with pytest.raises(app_helpers.InvalidFileException):
        app_helpers.is_valid_file_type(file=test_file)


def test_valid_file_type_passes():
    test_file = "fixtures/test_city_data.txt"
    assert app_helpers.is_valid_file_type(file=test_file)


def test_is_not_valid_path_and_file_is_not_readable():
    bad_file_path = "nowhere/this_is_not_a_file.txt"
    with pytest.raises(Exception):
        app_helpers.is_valid_path_and_file_is_readable(file=bad_file_path)


def test_is_valid_path_and_file_is_readable():
    this_dir = os.path.dirname(os.path.abspath(__file__))
    test_file = os.path.join(this_dir, os.pardir, "fixtures/test_city_data.txt")
    assert app_helpers.is_valid_path_and_file_is_readable(file=test_file)


def test_print_cities(capsys):
    road_map = [
        ("Alabama", "Montgomery", 32.361538, -86.279118),
        ("Alaska", "Juneau", 58.301935, -134.41974),
        ("Arizona", "Phoenix", 33.448457, -112.073844),
    ]
    expected_string = f"""
    city: Montgomery location: {round(32.361538, 2)}, {round(-86.279118, 2)}
    city: Juneau location: {round(58.301935, 2)}, {round(-134.41974, 2)}
    city: Phoenix location: {round(33.448457, 2)}, {round(-112.073844, 2)}
    """
    cities_interface.print_cities(road_map=road_map)
    captured = capsys.readouterr()
    assert captured.out == helpers.format_string(expected_string)


@pytest.mark.parametrize(
    "city_locations_and_distance",
    [
        pytest.param(helpers.cities_and_distance(0)),
        pytest.param(helpers.cities_and_distance(1)),
        pytest.param(helpers.cities_and_distance(2)),
        pytest.param(helpers.cities_and_distance(3)),
        pytest.param(helpers.cities_and_distance(4)),
    ],
)
def test_compute_distance_between_two_cities(city_locations_and_distance):
    city_a_lat, city_a_long, city_b_lat, city_b_long, result = city_locations_and_distance
    assert app_helpers.compute_euclidean_distance(
        city_a_lat=city_a_lat,
        city_a_long=city_a_long,
        city_b_lat=city_b_lat,
        city_b_long=city_b_long,
    ) == pytest.approx(result, 0.01)
