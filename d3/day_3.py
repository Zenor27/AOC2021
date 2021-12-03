from lib.lib_file import LibFile


def transpose_binaries(binaries):
    transposed = []
    for x in list(zip(*binaries))[:-1]:
        transposed.append([y for y in x])

    return transposed


def get_power_consumption(binaries):
    transposed_binaries = transpose_binaries(binaries)
    gamma_rate = ''
    espsilon_rate = ''
    for transposed_binary in transposed_binaries:
        zeros_count = transposed_binary.count("0")
        ones_count = transposed_binary.count("1")
        if zeros_count > ones_count:
            gamma_rate += "1"
            espsilon_rate += "0"
        else:
            gamma_rate += "0"
            espsilon_rate += "1"
    return int(gamma_rate, 2) * int(espsilon_rate, 2)


def get_oxygen_and_scrubber_generator_rating(binaries):
    def _get_oxygen_or_scrubber_generator_rating(matching_binaries, bit_index, bit_comparator_func):
        if len(matching_binaries) == 1:
            return matching_binaries

        transposed_binaries = transpose_binaries(matching_binaries)
        transposed_binary = transposed_binaries[bit_index]

        zeros_count = transposed_binary.count("0")
        ones_count = transposed_binary.count("1")

        matching_binaries = list(filter(lambda x: x[bit_index] == bit_comparator_func(
            zeros_count, ones_count), matching_binaries))
        return _get_oxygen_or_scrubber_generator_rating(matching_binaries, bit_index + 1, bit_comparator_func)

    matching_binaries = binaries.copy()
    oxygen_rating = _get_oxygen_or_scrubber_generator_rating(
        matching_binaries, 0, lambda zeros_count, ones_count: '0' if zeros_count > ones_count else '1')[0]
    scrubber_rating = _get_oxygen_or_scrubber_generator_rating(
        matching_binaries, 0, lambda zeros_count, ones_count: '0' if zeros_count <= ones_count else '1')[0]

    return int(oxygen_rating, 2) * int(scrubber_rating, 2)


def day_3():
    file_lines = LibFile.read_lines("d3/input.txt")
    return get_oxygen_and_scrubber_generator_rating(file_lines)
