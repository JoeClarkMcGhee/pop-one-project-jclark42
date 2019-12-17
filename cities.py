import argparse
import os

from application import cities_interface
from application import visualize_road_map


def main(*, file_name="city-data.txt"):
    """
    The programme reads in and prints out the provided city data from the file, then creates the
    best cycle and prints it out.

    Usage:
        - The program must be executed from the command line e.g. `python3 cities.py <file_name>`
        - Type `cities.py -h` for complete instructions.
        - The data file must be in the pop-one-project-jclark42 directory, not one of the nested
          subdirectories.
    """
    file = file_name
    this_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(this_dir, file)
    road_map = cities_interface.read_cities(file_name=file_path)
    if not road_map:
        print("Please fix the file errors")
        return
    print("---- Initial road map ----")
    cities_interface.print_cities(road_map=road_map)

    print("---- Optimised road map ----")
    best_road_map = cities_interface.find_best_cycle(road_map=road_map)
    cities_interface.print_map(road_map=best_road_map)
    visualize_road_map.visualise(
        road_map=best_road_map,
        distance=cities_interface.compute_total_distance(road_map=best_road_map),
    )


help_text = (
    "-------------------------------------------------------\n"
    "Provide a file name (with extension as .txt) consisting\n"
    "of city data and the best route between the cities will\n"
    "be calculated."
    "\n\nExample: `python3 cities.py your-city-data.txt`"
    "\n\nIf no file is provided and the optional `default_data`\n"
    "argument is passed to cities.py then the route will be\n"
    "calculated based on the data in  the `city-data.txt` file\n"
    "found in this directory."
    "\n\nNOTE: The file to process has to be in this directory."
    "\n-------------------------------------------------------"
)
parser = argparse.ArgumentParser(
    description=help_text, formatter_class=argparse.RawTextHelpFormatter
)
parser.add_argument("file_name", type=str, help="file of city data to process")
args = parser.parse_args()
if args.file_name == "default_data":
    main()
else:
    main(file_name=args.file_name)
