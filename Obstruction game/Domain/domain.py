from texttable import Texttable

class Board:
    def __init__(self, lines, columns):
        self._lines = lines
        self._columns = columns
        self._board = [[0] * self._columns for i in range(self._lines)]

    @property
    def board(self):
        return self._board

    @property
    def lines(self):
        return self._lines

    @property
    def columns(self):
        return self._columns

    def get_element(self, i, j):
        return self._board[i][j]

    def set_element(self, i, j, new_el):
        self._board[i][j] = new_el

    def __str__(self):
        t = Texttable()
        header_row = ['/']
        for i in range(self._columns):
            header_row.append(i)
        t.header(header_row)

        for i in range(self._lines):
            row = self._board[i]
            display_row = [i]

            for j in range(self._columns):
                val = self._board[i][j]
                if val == 0:
                    if i == 0 and j == 0:
                        display_row.append('*')
                    else:
                        display_row.append(' ')
                else:
                    display_row.append(val)
            t.add_row(display_row)
        return t.draw()







