from d4.board import Board
from lib.lib_file import LibFile
from lib.lib_iterable import LibIterable

def get_drawn_numbers(file_lines):
    drawn_numbers_line = file_lines[0]
    return [int(x) for x in drawn_numbers_line.split(",")]

def get_boards(file_lines):
    file_lines = file_lines[1:]
    boards_grouped = LibIterable.grouper(file_lines, 5)
    boards = []
    for board_grouped in boards_grouped:
        board = Board()
        for board_line in board_grouped:
            board_line = [int(x) for x in board_line.split(" ") if x != ""]
            board.add_line(board_line)
        boards.append(board)
    return boards

def get_score(drawn_numbers: list[int], boards: list[Board]):
    for drawn_number in drawn_numbers:
        [board.mark_number(drawn_number) for board in boards]
        if len(boards) == 1:
            return boards[0].get_score(drawn_number)

        winning_boards = [board for board in boards if board.is_winning()]
        for winning_board in winning_boards:
            boards.remove(winning_board)

def day_4():
    file_lines = LibFile.read_lines("d4/input.txt")
    drawn_numbers = get_drawn_numbers(file_lines)
    boards = get_boards(file_lines)
    return get_score(drawn_numbers, boards)
