from d5.vector import Coordinate, Vector
from lib.lib_file import LibFile


def get_coordinate(coordinates_string) -> Coordinate:
    x, y = coordinates_string.split(",")
    return Coordinate(int(x), int(y))


def get_vectors(file_lines):
    vectors = []
    for file_line in file_lines:
        coordinates = file_line.split(" -> ")
        lhs, rhs = coordinates[0], coordinates[1]
        begin = get_coordinate(lhs)
        end = get_coordinate(rhs)
        vectors.append(Vector(begin, end))
    return vectors


def get_overlapping(vectors: list[Vector]):
    processed_coordinates = {}
    overlapping_coordinates = set()
    for vector in vectors:
        coordinates = vector.get_coordinates()
        for coordinate in coordinates:
            if processed_coordinates.get(coordinate, None):
                overlapping_coordinates.add(coordinate)
            else:
                processed_coordinates[coordinate] = True
    return len(overlapping_coordinates)

def get_horizontal_vertical(vectors: list[Vector]):
    _vectors = []
    for vector in vectors:
        if vector.begin.x == vector.end.x or vector.begin.y == vector.end.y:
            _vectors.append(vector)
    return _vectors


def day_5():
    file_lines = LibFile.read_lines("d5/input.txt")
    vectors = get_vectors(file_lines)
    # vectors = get_horizontal_vertical(vectors)
    return get_overlapping(vectors)
