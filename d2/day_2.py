from lib.lib_file import LibFile

DEPTH_INCREASE_UNITS = ["down"]
DEPTH_DECREASE_UNITS = ["up"]
HORIZONTAL_INCREASE_UNITS = ["forward"]

def get_unit_value(position: str):
        return int(position.split(" ")[-1])

def position_in_units(position, units):
    return any(x in position for x in units)



def get_position(positions):
    depth = 0
    horizontal = 0
    aim = 0
    for position in positions:
        unit_value = get_unit_value(position)
        if position_in_units(position, DEPTH_INCREASE_UNITS):
            aim += unit_value
        elif position_in_units(position, DEPTH_DECREASE_UNITS):
            aim -= unit_value
        elif position_in_units(position, HORIZONTAL_INCREASE_UNITS):
            horizontal += unit_value
            depth += aim * unit_value
        else:
            raise ValueError("unit not in known units")

    return depth, horizontal, depth * horizontal


def day_2():
    file_lines = LibFile.read_lines("d2/example.txt")
    return get_position(file_lines)
