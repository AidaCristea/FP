from random import shuffle

class Services:

    @staticmethod
    def parity(a):
        """
        Checks the parity of a number
        :param a:
        :return: True if number is odd, False otherwise
        """
        a = a % 2
        if a == 1:
            return True
        else:
            return False

    @staticmethod
    def check_symbol(s):
        """
        Checks if the symbol that the player entered is X
        :param s:
        :return: True if it is X, return False otherwise
        """
        if s != 'X':
            return False
        return True


    def is_full(self, board):
        """
        Checks if the board is full or not
        :param board:
        :return: True if board is full, False otherwise
        """
        for i in range(board._lines):
            for j in range(board._columns):
                value = board.get_element(i, j)
                if value == 0:
                    return False
        return True

    def move_computer_random_position(self, board):
        """
        The computer moves in a random, but valid position
        :param board:
        :return:
        """
        choices = []
        for row in range(board._lines):
            for col in range(board._columns):
                if board.get_element(row, col) == 0:
                    choices.append((row, col))
        shuffle(choices)
        return choices[0]

    def complete_computer_turn(self, board):
        """
        Completes the computers move
        :param board:
        :return: x and y (row and col)
        """
        x, y = self.move_computer_random_position(board)
        board.set_element(x, y, 'O')

        self.comlpete_neighburs(board, x, y)
        return x, y

    def first_comp_move(self, board, m_l, m_c):
        """
        Completes the middle square of the table
        :param board:
        :return:
        """
        board.set_element(m_l, m_c, "O")
        self.comlpete_neighburs(board, m_l, m_c)


    def computer_strategy(self, board, player_move, m_l, m_c):
        """
        Completes the image of the last move the player did
        :param board:
        :param player_move: list of all player moves
        :param m_l: middle row
        :param m_c: middle column
        :return: new line and new column
        """
        new_line = 0
        new_col = 0
        if len(player_move) == 0:
            self.first_comp_move(board, m_l, m_c)
        else:
            last_line, last_col = player_move[len(player_move)-1]
            if last_line > m_l:
                difl = last_line-m_l
            else:
                difl = m_l-last_line

            if last_col > m_c:
                difc = last_col - m_c
            else:
                difc = m_c - last_col

            if last_line > m_l:
                new_line = m_l - difl
            else:
                new_line = m_l+difl

            if last_col > m_c:
                new_col = m_c-difc
            else:
                new_col = m_c+difc

            board.set_element(new_line, new_col, "O")
            self.comlpete_neighburs(board, new_line, new_col)
        return new_line, new_col


    def move_player(self, board, x, y, symbol):
        """
        Make a move on the board
        :param board:
        :param x: line
        :param y: col
        :param symbol: X or O
        :return:
        """
        if not(0 <= x <= board._lines and 0 <= y <= board._columns):
            raise ValueError("Not a valid cell!")

        if board.get_element(x, y) != 0:
            raise ValueError("Cell already taken!")
        else:
            board.set_element(x, y, symbol)
            self.comlpete_neighburs(board, x, y)


    def comlpete_neighburs(self, board, x, y):
        """
        Completes the neighbours of the term form the (x, y) position
        :param x: row
        :param y: column
        :return:
        """
        li = 0
        ci = 0
        cf = 0
        lf = 0

        if x == 0:
            li = 0
            lf = x+1
        elif 0 < x < board._lines-1:
            li = x-1
            lf = x+1
        else:
            li = x-1
            lf = x

        if y == 0:
            ci = 0
            cf = y+1
        elif 0 < y < board._columns-1:
            ci = y-1
            cf = y+1
        else:
            ci = y - 1
            cf = y

        i = li
        while i <= lf:
            j = ci
            while j <= cf:
                if board.get_element(i, j) != 'X' and board.get_element(i, j) != 'O':
                    board.set_element(i, j, "/")
                j += 1
            i += 1



class RepositoryException(Exception):
    """
    Exception class for repository errors
    """
    def __init__(self, message):
        """
        Constructor for repository exception class
        :param message: A string representing the exception message
        """
        self._message = message

    def __str__(self):
        return self._message



