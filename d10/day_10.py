import math
import numpy as np
from lib.lib_check import LibCheck
from lib.lib_file import LibFile

input_files_and_results = [
    ("d10/example.txt", 288957), ("d10/input.txt", 3103006161)]


CHARACTER_TO_POINTS = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}


OPENING_TO_CLOSING = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}


@LibCheck.check(input_files_and_results=input_files_and_results, input_parse_func=LibFile.read_lines)
def day_10(file_lines: list[str]):
    total_scores = []
    for file_line in file_lines:
        token_stack = []
        for token in file_line:
            if token in OPENING_TO_CLOSING:
                token_stack.append(token)
            elif OPENING_TO_CLOSING[token_stack[-1]] == token:
                token_stack.pop()
            else:
                token_stack = []
                break

        token_stack.reverse()
        closing_token_stack = [OPENING_TO_CLOSING[x] for x in token_stack]

        current_score = 0
        for closing_token in closing_token_stack:
            current_score *= 5
            current_score += CHARACTER_TO_POINTS[closing_token]
        if current_score != 0:
            total_scores.append(current_score)

    return sorted(total_scores)[len(total_scores) // 2]
