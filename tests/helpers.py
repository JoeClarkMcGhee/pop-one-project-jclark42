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
            ("Bing", "Bong", 39.161921, -75.526755),
            ("Boo", "Baz", 44.95, -93.094),
        ],
        [
            ("Bill", "Ted", 38.197274, -84.86311),
            ("Freddy", "Krueger", 39.161921, -75.526755),
            ("Bilbo", "Baggins", 44.95, -93.094),
        ],
        [
            ("Bat", "Man", 38.197274, -84.86311),
            ("The", "Joker", 39.161921, -75.526755),
            ("Two", "Face", 44.95, -93.094),
        ],
        [
            ("Spider", "Man", 38.197274, -84.86311),
            ("Green", "Goblin", 39.161921, -75.526755),
            ("Ant", "Man", 44.95, -93.094),
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
            ("Boo", "Baz", 44.95, -93.094),
            ("Foo", "Bar", 38.197274, -84.86311),
            ("Bing", "Bong", 39.161921, -75.526755),
        ],
        [
            ("Bilbo", "Baggins", 44.95, -93.094),
            ("Bill", "Ted", 38.197274, -84.86311),
            ("Freddy", "Krueger", 39.161921, -75.526755),
        ],
        [
            ("Two", "Face", 44.95, -93.094),
            ("Bat", "Man", 38.197274, -84.86311),
            ("The", "Joker", 39.161921, -75.526755),
        ],
        [
            ("Ant", "Man", 44.95, -93.094),
            ("Spider", "Man", 38.197274, -84.86311),
            ("Green", "Goblin", 39.161921, -75.526755),
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
