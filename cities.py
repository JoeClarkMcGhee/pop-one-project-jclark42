import os

from application import cities_interface
from application import visualize_road_map


def main():
    """
    The programme reads in and prints out the provided city data from the file, then creates the
    best cycle and prints it out.

    Usage:
        - Provide the variable *file* with the file name of city data.
        - The file must be in the pop-one-project-jclark42 directory, not one of the nested
          subdirectories.
        - You do not need to provide the full path just the name of the file.
        - Once you have set the *file* variable you can run the program by calling `python3
          cities.py`.
        - You must run the program in the pop-one-project-jclark42 directory
    """
    file = "city-data.txt"
    this_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(this_dir, file)
    print("---- Initial road map ----")
    road_map = cities_interface.read_cities(file_name=file_path)
    cities_interface.print_cities(road_map=road_map)

    print("---- Optimised road map ----")
    best_road_map = cities_interface.find_best_cycle(road_map=road_map)
    cities_interface.print_map(road_map=best_road_map)
    visualize_road_map.visualise(
        road_map=best_road_map,
        distance=cities_interface.compute_total_distance(road_map=best_road_map),
    )


if __name__ == "__main__":
    main()
