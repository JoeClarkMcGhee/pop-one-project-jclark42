import pytest
import cities


def test_compute_total_distance():
    road_map1 = [
        ("Kentucky", "Frankfort", 38.197274, -84.86311),
        ("Delaware", "Dover", 39.161921, -75.526755),
        ("Minnesota", "Saint Paul", 44.95, -93.094),
    ]

    assert cities.compute_total_distance(road_map1) == pytest.approx(9.386 + 18.496 + 10.646, 0.01)

    """add your further tests"""


def test_swap_cities():
    assert True


def test_shift_cities():
    assert True
