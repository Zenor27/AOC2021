import math
import numpy as np
from lib.lib_check import LibCheck
from lib.lib_file import LibFile

input_files_and_results = [("d9/example.txt", 1134), ("d9/input.txt", 902880)]


def get_height_map(file_lines: list[str]):
    height_map = []
    for file_line in file_lines:
        current_row = []
        for height in file_line:
            current_row.append(int(height))
        height_map.append(current_row)
    return height_map


def get_low_points(height_map: list[list[int]]) -> list[(int, int)]:
    low_points = []
    for row_idx, row in enumerate(height_map):
        for col_idx, col in enumerate(row):
            upper = height_map[row_idx -
                               1][col_idx] if row_idx > 0 else math.inf
            left = height_map[row_idx][col_idx -
                                       1] if col_idx > 0 else math.inf
            right = height_map[row_idx][col_idx +
                                        1] if col_idx < len(row) - 1 else math.inf
            bottom = height_map[row_idx +
                                1][col_idx] if row_idx < len(height_map) - 1 else math.inf
            if col < upper and col < left and col < right and col < bottom:
                low_points.append((row_idx, col_idx))
    return low_points


def flood_fill(matrix, x, y, initial_color, limit_color):
    matrix_width = len(matrix)
    matrix_height = len(matrix[0])

    is_out_of_bound = x < 0 or x >= matrix_width or y < 0 or y >= matrix_height
    if is_out_of_bound:
        return
    if matrix[x][y] == limit_color or matrix[x][y] != initial_color:
        return

    if matrix[x][y] == initial_color:
        matrix[x][y] = -1

    flood_fill(matrix, x - 1, y, initial_color, limit_color)
    flood_fill(matrix, x + 1, y, initial_color, limit_color)
    flood_fill(matrix, x, y - 1, initial_color, limit_color)
    flood_fill(matrix, x, y + 1, initial_color, limit_color)

def get_normalized_height_map(height_map: list[list[int]]) -> list[list[int]]:
    return [[0 if y != 9 else 9 for y in x] for x in height_map]



@LibCheck.check(input_files_and_results=input_files_and_results, input_parse_func=LibFile.read_lines)
def day_9(file_lines: list[str]):
    height_map = get_height_map(file_lines)
    low_points: list[(int, int)] = get_low_points(height_map)

    bassin_sz = []
    normalized_height_map = get_normalized_height_map(height_map)
    for low_point_x, low_point_y in low_points:
        normalized_height_map_copy = [x.copy() for x in normalized_height_map]
        flood_fill(normalized_height_map_copy, low_point_x, low_point_y, 0, 9)
        bassin_sz.append(sum(len(x) for x in [
            list(filter(lambda x: x == -1, row)) for row in normalized_height_map_copy]))

    return np.prod(sorted(bassin_sz, reverse=True)[:3])