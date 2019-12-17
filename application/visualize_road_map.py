from typing import Any, List, Tuple

import matplotlib.pyplot as plt

RoadMap = List[Tuple[str, str, float, float]]


def visualise(*, road_map: RoadMap, distance: float):
    plot, x_axis, y_axis = plot_cities(road_map=road_map)
    draw_arrow(plot=plot, x_axis=x_axis, y_axis=y_axis)
    add_graph_text(distance=distance, road_map=road_map, plot=plot, x_axis=x_axis, y_axis=y_axis)
    plt.show()


def plot_cities(*, road_map: RoadMap) -> Tuple[Any, list, list]:
    """
    :param road_map: [(state, city, latitude, longitude), ...]
    """
    x_axis = list()
    y_axis = list()
    for idx, city in enumerate(road_map):
        _, _, lat, long = city
        x_axis.append(lat)
        y_axis.append(long)
    plt.plot(x_axis, y_axis, "^k", linewidth=1, markersize=4)
    return plt, x_axis, y_axis


def draw_arrow(*, plot: Any, x_axis: list, y_axis: list) -> None:
    a_scale = float(max(x_axis)) / float(100)
    for i in range(0, len(x_axis) - 1):
        plot.arrow(
            x_axis[i],
            y_axis[i],
            (x_axis[i + 1] - x_axis[i]),
            (y_axis[i + 1] - y_axis[i]),
            head_width=a_scale,
            color="g",
            length_includes_head=True,
        )
    # Plot arrow back to the start.
    base_x = len(x_axis) - 1
    base_y = len(y_axis) - 1
    plot.arrow(
        x_axis[base_x],
        y_axis[base_y],
        (x_axis[0] - x_axis[base_x]),
        (y_axis[0] - y_axis[base_y]),
        head_width=a_scale,
        color="g",
        length_includes_head=True,
    )


def add_graph_text(
    *, distance: float, road_map: RoadMap, plot: Any, x_axis: list, y_axis: list
) -> None:
    text = f"  Road map\n\n"
    for i, city in enumerate(road_map):
        _, city, _, _ = city
        xy = (x_axis[i], y_axis[i])
        plot.annotate(i + 1, xy)
        text += f"{i+1}. {city}\n"
    text += f"\nTotal Distance: {round(distance,2)}"
    plot.text(0.02, 0.1, text, fontsize=8, transform=plt.gcf().transFigure)
    plot.subplots_adjust(left=0.3)
    plot.xlabel("Latitude")
    plot.ylabel("Longitude")
    plot.title("TSP Best Route")
