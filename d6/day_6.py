from collections import defaultdict
from typing import DefaultDict
from lib.lib_file import LibFile


def get_lanternfishes(file_content) -> DefaultDict[int, int]:
    days_until_new_fish = file_content.split(',')
    lanterfish_dict = defaultdict(int)
    for day_until_new_fish in [int(x) for x in days_until_new_fish]:
        lanterfish_dict[day_until_new_fish] += 1
    return lanterfish_dict


def get_lanternfishes_after_days(days: int, current_generation: DefaultDict[int, int]):
    for _ in range(days):
        new_generation = defaultdict(int)
        for key in sorted(current_generation.keys()):
            lanternfishes_to_add = current_generation[key]
            if key == 0:
                new_generation[8] = lanternfishes_to_add
                new_generation[6] = lanternfishes_to_add
            else:
                new_generation[key - 1] += lanternfishes_to_add
        
        current_generation = new_generation

    return sum(x for x in current_generation.values())


def day_6():
    file_content = LibFile.read_file("d6/example.txt")
    initial_lanternfishes: DefaultDict[int, int] = get_lanternfishes(file_content)
    return get_lanternfishes_after_days(256, initial_lanternfishes)
