import math
import numpy as np
from lib.lib_check import LibCheck
from lib.lib_file import LibFile

input_files_and_results = [
    ("d11/example.txt", 195),
    ("d11/input.txt", 324)
]


def get_octopuses(file_lines: list[str]) -> list[list[int]]:
    rows = []
    for file_line in file_lines:
        rows.append([int(octopus) for octopus in file_line])
    return rows


def increment(octopuses: list[list[int]]) -> list[(int, int)]:
    need_to_flash_coords = []
    for row_idx, row in enumerate(octopuses):
        for col_idx, _ in enumerate(row):
            octopuses[row_idx][col_idx] += 1
            if octopuses[row_idx][col_idx] == 10:
                need_to_flash_coords.append((row_idx, col_idx))
    return need_to_flash_coords


def process_flashes(octopuses: list[list[int]], need_to_flash_coords: list[(int, int)]) -> bool:
    processed_flash = []

    while len(need_to_flash_coords) != 0:
        for row_idx, col_idx in need_to_flash_coords:
            need_to_flash_coords.remove((row_idx, col_idx))
            adjacent_coords_to_is_bound = {
                (row_idx - 1, col_idx): row_idx - 1 >= 0,
                (row_idx + 1, col_idx): row_idx + 1 < len(octopuses),
                (row_idx, col_idx - 1): col_idx - 1 >= 0,
                (row_idx, col_idx + 1): col_idx + 1 < len(octopuses[row_idx]),
                (row_idx - 1, col_idx - 1): row_idx - 1 >= 0 and col_idx - 1 >= 0,
                (row_idx - 1, col_idx + 1): row_idx - 1 >= 0 and col_idx + 1 < len(octopuses[row_idx]),
                (row_idx + 1, col_idx - 1): row_idx + 1 < len(octopuses) and col_idx - 1 >= 0,
                (row_idx + 1, col_idx + 1): row_idx + 1 < len(octopuses) and col_idx + 1 < len(octopuses[row_idx])
            }
            for (adj_row_idx, adj_col_idx), is_bound in adjacent_coords_to_is_bound.items():
                if not is_bound:
                    continue
                octopuses[adj_row_idx][adj_col_idx] += 1
                if octopuses[adj_row_idx][adj_col_idx] == 10:
                    need_to_flash_coords.append((adj_row_idx, adj_col_idx))
            
            processed_flash.append((row_idx, col_idx))

    has_simultaneaously_flashed = len(processed_flash) == (
        len(octopuses) * len(octopuses[0]))
    for row_idx, col_idx in processed_flash:
        octopuses[row_idx][col_idx] = 0
    return has_simultaneaously_flashed


def get_step(octopuses: list[list[int]]) -> int:
    step = 0
    while True:
        need_to_flash_coords = increment(octopuses)
        has_simultaneaously_flashed = process_flashes(
            octopuses, need_to_flash_coords)
        step += 1
        if has_simultaneaously_flashed:
            return step


@LibCheck.check(input_files_and_results=input_files_and_results, input_parse_func=LibFile.read_lines)
def day_11(file_lines: list[str]):
    octopuses: list[list[int]] = get_octopuses(file_lines)
    step: int = get_step(octopuses)
    return step
