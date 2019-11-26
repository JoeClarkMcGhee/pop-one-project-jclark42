import textwrap


def initialise_test_road_map(index):
    road_map1 = [
        [
            ("Kentucky", "Frankfort", 38.197274, -84.86311),
            ("Delaware", "Dover", 39.161921, -75.526755),
            ("Minnesota", "Saint Paul", 44.95, -93.094),
        ],
        [
            ("Foo", "Bar", 38.197274, -84.86311),
            ("Bing", "Bong", 36.161921, -78.526755),
            ("Boo", "Baz", 42.95, -99.094),
        ],
        [
            ("Bill", "Ted", 38.197274, -84.86311),
            ("Freddy", "Krueger", 49.161921, -79.526755),
            ("Bilbo", "Baggins", 54.95, -33.094),
        ],
        [
            ("Bat", "Man", 38.197274, -84.86311),
            ("The", "Joker", 19.161921, -45.526755),
            ("Two", "Face", 74.95, -53.094),
        ],
        [
            ("Spider", "Man", 38.197274, -84.86311),
            ("Green", "Goblin", 31.161921, -85.526755),
            ("Ant", "Man", 44.95, -13.094),
            ("Flash", "Gordon", 49.95, -13.094),
            ("Super", "Man", 67.95, -13.094),
        ],
    ]
    return road_map1[index]


def swap_city_result(index):
    road_map1 = [
        (
            [
                ("Kentucky", "Frankfort", 38.197274, -84.86311),
                ("Delaware", "Dover", 39.161921, -75.526755),
                ("Minnesota", "Saint Paul", 44.95, -93.094),
            ],
            1.0,
        ),
        (
            [
                ("Kentucky", "Frankfort", 38.197274, -84.86311),
                ("Delaware", "Dover", 39.161921, -75.526755),
                ("Minnesota", "Saint Paul", 44.95, -93.094),
            ],
            1.0,
        ),
        (
            [
                ("Kentucky", "Frankfort", 38.197274, -84.86311),
                ("Delaware", "Dover", 39.161921, -75.526755),
                ("Minnesota", "Saint Paul", 44.95, -93.094),
            ],
            1.0,
        ),
        (
            [
                ("Kentucky", "Frankfort", 38.197274, -84.86311),
                ("Delaware", "Dover", 39.161921, -75.526755),
                ("Minnesota", "Saint Paul", 44.95, -93.094),
            ],
            1.0,
        ),
        (
            [
                ("Kentucky", "Frankfort", 38.197274, -84.86311),
                ("Delaware", "Dover", 39.161921, -75.526755),
                ("Minnesota", "Saint Paul", 44.95, -93.094),
            ],
            1.0,
        ),
    ]
    return road_map1[index]


def shift_city_result(index):
    road_map1 = [
        [
            ("Minnesota", "Saint Paul", 44.95, -93.094),
            ("Kentucky", "Frankfort", 38.197274, -84.86311),
            ("Delaware", "Dover", 39.161921, -75.526755),
        ],
        [
            ("Boo", "Baz", 42.95, -99.094),
            ("Foo", "Bar", 38.197274, -84.86311),
            ("Bing", "Bong", 36.161921, -78.526755),
        ],
        [
            ("Bilbo", "Baggins", 54.95, -33.094),
            ("Bill", "Ted", 38.197274, -84.86311),
            ("Freddy", "Krueger", 49.161921, -79.526755),
        ],
        [
            ("Two", "Face", 74.95, -53.094),
            ("Bat", "Man", 38.197274, -84.86311),
            ("The", "Joker", 19.161921, -45.526755),
        ],
        [
            ("Super", "Man", 67.95, -13.094),
            ("Spider", "Man", 38.197274, -84.86311),
            ("Green", "Goblin", 31.161921, -85.526755),
            ("Ant", "Man", 44.95, -13.094),
            ("Flash", "Gordon", 49.95, -13.094),
        ],
    ]
    return road_map1[index]


def format_string(input_string):
    """
    Return a string with normalized whitespace.
    This function is meant to be used where `input_string` is a triple-quoted
    string embedded in a test.
    """
    return textwrap.dedent(input_string).lstrip()


def cities_and_distance(index):
    """
    returns a tuple of (city_a_lat, city_a_long, city_b_lat, city_b_long, result)
    """
    return [
        (38.56, -85.67, 34.16, -75.52, 11.06),
        (37.16, -86.56, 35.16, -76.52, 10.23),
        (36.16, -87.75, 36.16, -77.52, 10.23),
        (35.86, -88.86, 37.16, -78.52, 10.42),
        (34.19, -89.86, 38.16, -79.52, 11.07),
    ][index]
