import pytest

from application import helpers as app_helpers


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
        app_helpers.parse_file_line(file_line=file_line)


def test_is_valid_file_line():
    file_line = "Alabama	Montgomery	32.361538	-86.279118"
    expected_file_line = ("Alabama", "Montgomery", 32.361538, -86.279118)
    assert app_helpers.parse_file_line(file_line=file_line) == expected_file_line


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
    test_file = "../fixtures/test_city_data.txt"
    assert app_helpers.is_valid_path_and_file_is_readable(file=test_file)
