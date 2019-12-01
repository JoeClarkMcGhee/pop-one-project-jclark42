class BestCycleContainer:
    def __init__(self):
        self.shortest_distance = 0
        self.best_road_map = None

    def set_distance_and_road_map(self, *, distance, road_map):
        self.best_road_map = road_map
        self.shortest_distance = distance

    def should_update_best_distance(self, *, distance):
        return distance < self.shortest_distance
