import numpy as np


class Coordinate:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __eq__(self, coordinate) -> bool:
        return coordinate.x == self.x and coordinate.y == self.y

    def __repr__(self) -> str:
        return f'Coordinate({self.x}, {self.y})'

    def __hash__(self):
        return hash((self.x, self.y))



class Vector:
    def __init__(self, begin: Coordinate, end: Coordinate):
        self.begin = begin
        self.end = end

    def get_coordinates(self) -> list[Coordinate]:
        ends = np.array([[self.begin.x, self.begin.y],
                        [self.end.x, self.end.y]])

        diff = np.diff(ends, axis=0)[0]
        max_diff = np.argmax(np.abs(diff))
        abs_max_diff = np.abs(diff[max_diff])
        all_coordinates = ends[0] + \
            (np.outer(np.arange(abs_max_diff + 1), diff) + (abs_max_diff >> 1)) // abs_max_diff

        coordinates = []
        for x, y in all_coordinates:
            coordinates.append(Coordinate(x, y))

        return coordinates

    def __repr__(self) -> str:
        return f"{self.begin.x}, {self.begin.y} -> {self.end.x}, {self.end.y}"
