class BestCycleContainer:
    shortest_distance = None
    best_road_map = None

    @classmethod
    def set_distance_and_road_map(cls, *, distance, road_map):
        cls.best_road_map = road_map
        cls.shortest_distance = distance

    @classmethod
    def should_update_best_distance(cls, *, distance):
        return distance < cls.shortest_distance
