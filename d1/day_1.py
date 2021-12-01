from lib.lib_file import LibFile
from lib.lib_iterable import LibIterable


def count_depth_increase(depths):
    previous_depth = None
    nb_depth_increase = 0
    for depth in depths:
        if previous_depth is not None and depth > previous_depth:
            nb_depth_increase += 1
        previous_depth = depth

    return nb_depth_increase


def count_sliding_depth_increase(depths):
    grouped_depths = LibIterable.sliding_grouper(depths, 3)
    previous_depth = None
    nb_depth_increase = 0
    for grouped_depth in grouped_depths:
        grouped_depth_sum = sum(grouped_depth)
        if previous_depth is not None and grouped_depth_sum > previous_depth:
            nb_depth_increase += 1
        previous_depth = grouped_depth_sum

    return nb_depth_increase


def day_1():
    file_lines = LibFile.read_lines("d1/input.txt")
    depths = [int(x) for x in file_lines]
    return count_depth_increase(depths), count_sliding_depth_increase(depths)
