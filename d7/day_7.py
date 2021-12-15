import statistics
from lib.lib_file import LibFile
from lib.lib_bench import LibBench


def get_crab_ships(file_content: str) -> list[int]:
    return [int(fuel) for fuel in file_content.split(",")]

def get_fuel_cost(crab_ships, mean):
    fuel_cost = 0
    for crab_ship in crab_ships:
        fuel_cost += sum(range(1, abs(crab_ship - mean) + 1))
    return fuel_cost



@LibBench.bench
def day_7():
    file_content: str = LibFile.read_file("d7/input.txt")
    crab_ships: list[int] = get_crab_ships(file_content)
    mean = int(statistics.mean(crab_ships))
    return get_fuel_cost(crab_ships, mean)