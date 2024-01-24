class Cell(object):
    NO_COLOUR = "Blank"

    def __init__(self, name):
        """

        :param int name:
        :param int column:
        """
        self.name = name
        self.colour = self.NO_COLOUR

    def is_empty(self):
        return self.colour == self.NO_COLOUR

    def change_color(self, new_color):
        """

        :param str new_color:
        :rtype: bool
        """
        if self.is_empty():
            self.colour = new_color
            return True
        return False

    def same_colour(self, colour):
        """

        :param str colour:
        :rtype: bool
        """
        return self.colour == colour

    def __str__(self):
        return "name: {0}, colour: {1}".format(self.name, self.colour)


class Vector(object):

    def __init__(self, name):
        """

        :param int name:
        """
        self._name = name
        self.cells = []

    def add_cell(self, cell):
        """

        :param Cell cell:
        :return:
        """
        self.cells.append(cell)

    def get_cell_by_index(self, index):
        """

        :param int index:
        :rtype: Cell
        """
        try:
            return self.cells[index]
        except IndexError:
            return Cell(index)

    def is_there_a_winner(self, colour, win_cond=4):
        """

        :param str colour:
        :param int win_cond:
        :rtype: bool
        """
        if len(self.cells) < win_cond:
            return False
        for i in range(0, len(self.cells) + 1 - win_cond):
            if len(list(filter(lambda cell: cell.same_colour(colour), self.cells[i:i + win_cond]))) == win_cond:
                return True
        return False


class Board(object):
    MAX_ROW = 6
    MAX_COL = 7

    COLUMNS = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6}

    def __init__(self, ):
        self._board = [Vector(pos) for pos in range(self.MAX_COL)]

    def fill_board_with_colours(self, colours: list):
        pos_char, color = colours
        index = self._translate(pos_char)
        cell = Cell(index)
        cell.colour = color
        self._board[index].add_cell(cell)

    def _translate(self, pos_char: str) -> int:
        return self.COLUMNS[pos_char]

    def _search_by_column(self, color):
        for column in self._board:
            if column.is_there_a_winner(color):
                return True
        return False

    def _search_by_row(self, color):
        for index in range(self.MAX_ROW):
            vector = Vector(index)
            for column in self._board:
                vector.add_cell(column.get_cell_by_index(index))
            if vector.is_there_a_winner(color):
                return True
        return False

    def _search_by_diagonal(self, color):
        for _cols in range(3, self.MAX_COL):
            vector = Vector(0)
            _pos = 0
            for _column in range(_cols, -1, -1):
                vector.add_cell(self._board[_column].get_cell_by_index(_pos))
                _pos += 1
            if vector.is_there_a_winner(color):
                return True
        return False

    def _search_by_anti_diagonal(self, color):
        for _cols in range(0, 4):
            vector = Vector(0)
            _pos = 0
            for _column in range(_cols, self.MAX_COL):
                vector.add_cell(self._board[_column].get_cell_by_index(_pos))
                _pos += 1
            if vector.is_there_a_winner(color):
                return True
        return False

    def find_winner(self):
        for colour in ("Yellow", "Red"):
            if self._search_by_column(colour) or self._search_by_row(colour) or self._search_by_diagonal(
                    colour) or self._search_by_anti_diagonal(colour):
                return colour
        return "Draw"


def who_is_winner(pieces_position_list):
    """

    :param list of str pieces_position_list:
    :rtype: str
    """
    c4g = Board()
    for pieces_position in pieces_position_list:
        c4g.fill_board_with_colours(pieces_position.split("_"))
        res = c4g.find_winner()
        if res == "Draw":
            continue
        return res
    return "Draw"
