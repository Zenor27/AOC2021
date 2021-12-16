from collections import Counter
from lib.lib_file import LibFile
from lib.lib_bench import LibBench


ONE_SEGMENT_LEN = 2
FOUR_SEGMENT_LEN = 4
SEVEN_SEGMENT_LEN = 3
EIGHT_SEGMENT_LEN = 7


NUMBER_TO_SEGMENT_LEN = {
    0: 6,
    1: ONE_SEGMENT_LEN,
    2: 5,
    3: 5,
    4: FOUR_SEGMENT_LEN,
    5: 5,
    6: 6,
    7: SEVEN_SEGMENT_LEN,
    8: EIGHT_SEGMENT_LEN,
    9: 6
}

SEGMENT_LEN_TO_NUMBER = {v: k for k, v in NUMBER_TO_SEGMENT_LEN.items()}

KNOWN_SEGMENT_LENGTHS = [ONE_SEGMENT_LEN,
                         FOUR_SEGMENT_LEN, SEVEN_SEGMENT_LEN, EIGHT_SEGMENT_LEN]


def get_signal_and_results(file_line: str) -> tuple[list[str], list[str]]:
    [signal, results] = file_line.split(" | ")
    signal, results = signal.split(" "), results.split(" ")
    return signal, results


def does_string_contains_characters(string: str, characters: str, thresold: int = 0) -> bool:
    common_letters = Counter(string) & Counter(characters)
    return (len(characters) - sum(common_letters.values())) == thresold


def filter_possible_signals(possible_signals: list[str], known_signal: str, thresold: int = 0) -> list[str]:
    return list(filter(lambda x: does_string_contains_characters(x, known_signal, thresold=thresold), possible_signals))


def filter_possible_signals_for_numbers(possible_signals: list[str], number: int) -> list[str]:
    return [x for x in possible_signals if len(x) == NUMBER_TO_SEGMENT_LEN[number]]


def get_known_signals(signal: list[str]) -> dict[int, str]:
    return {SEGMENT_LEN_TO_NUMBER[len(y)]: y for y in list(
            filter(lambda x: len(x) in KNOWN_SEGMENT_LENGTHS, signal))}


def remove_known_signals_from_possible_signals(known_signals, possible_signals):
    possible_signal_number_to_delete = []
    for possible_signal_number, possible_signal_strs in possible_signals.items():
        if len(possible_signal_strs) == 1:
            known_signals[possible_signal_number] = possible_signal_strs[0]
            possible_signal_number_to_delete.append(possible_signal_number)

    for possible_signal_number in possible_signal_number_to_delete:
        del possible_signals[possible_signal_number]

    for known_str in known_signals.values():
        for possible_signal_strs in possible_signals.values():
            if known_str in possible_signal_strs:
                possible_signal_strs.remove(known_str)


def deduce_signals(known_signals: dict[int, str], possible_signals: dict[int, list[str]]):
    possible_signals[0] = filter_possible_signals(
        possible_signals[0], known_signals[7])
    possible_signals[3] = filter_possible_signals(
        possible_signals[3], known_signals[7])
    possible_signals[9] = filter_possible_signals(
        possible_signals[9], known_signals[7])
    remove_known_signals_from_possible_signals(
        known_signals, possible_signals)

    possible_signals[9] = filter_possible_signals(
        possible_signals[9], known_signals[4])
    remove_known_signals_from_possible_signals(
        known_signals, possible_signals)

    possible_signals[0] = filter_possible_signals(
        possible_signals[0], known_signals[7])
    remove_known_signals_from_possible_signals(
        known_signals, possible_signals)

    possible_signals[2] = filter_possible_signals(
        possible_signals[2], known_signals[3], thresold=1)
    possible_signals[2] = filter_possible_signals(
        possible_signals[2], known_signals[4], thresold=2)
    remove_known_signals_from_possible_signals(known_signals, possible_signals)

    # We only got 5 left
    remove_known_signals_from_possible_signals(known_signals, possible_signals)


@LibBench.bench
def day_8():
    file_lines = LibFile.read_lines("d8/input.txt")
    res = 0
    for file_line in file_lines:
        signal, results = get_signal_and_results(file_line)
        known_signals = get_known_signals(signal)
        possible_signals = {k: filter_possible_signals_for_numbers(signal, k)
                            for k in range(10) if k not in [1, 4, 7, 8]}
        deduce_signals(known_signals, possible_signals)

        match = []
        for result in results:
            for known_signal_nb, known_signal_str in known_signals.items():
                if len(known_signal_str) == len(result) and does_string_contains_characters(result, known_signal_str):
                    match.append(str(known_signal_nb))
                    break

        res += int("".join(match))
    return res
