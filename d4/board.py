from lib.lib_file import LibFile
from lib.lib_iterable import LibIterable


class Cell:
    def __init__(self, number: int):
        self.number = number
        self.marked = False

    def mark(self):
        self.marked = True


class Board:
    NB_ROWS = 5
    NB_COLS = 5

    def __init__(self):
        self.board = []
        self.flat_board = []

    def add_line(self, line: list[int]):
        if len(self.board) == self.NB_ROWS:
            raise Exception("Board is full")
        line_cells = [Cell(number) for number in line]
        self.board.append(line_cells)
        self.transposed_board = LibIterable.transpose(self.board)
        self.flat_board.extend(line_cells)

    def mark_number(self, number: int):
        cells = [cell for cell in self.flat_board if cell.number == number]
        [cell.mark() for cell in cells]

    def is_winning(self) -> bool:
        for line in self.board:
            if all(cell.marked for cell in line):
                return True
            
        for col in self.transposed_board:
            if all(cell.marked for cell in col):
                return True

        return False

    def get_score(self, last_drawn_number: int) -> int:
        return sum([cell.number for cell in self.flat_board if not cell.marked]) * last_drawn_number

    def __repr__(self) -> str:
        _str = ""
        for line in self.board:
            _str += "|" + \
                "|".join(
                    f"{cell.number} {'✅' if cell.marked else '⛔️'}" for cell in line) + "|\n"

        return _str
