from Domain.domain import Board
from Services.service import Services


class UI:
    def __init__(self):
        n = int(input("Enter numbers of lines : "))
        m = int(input("Enter number of columns: "))
        self._board = Board(n, m)
        self._services = Services()
        self._m = m
        self._n = n
        print(str(self._board))

    def start(self):
        option = input("Do you want to start? (1-Yes, 0-No) ")
        if option == '1':
            player_turn = True
        elif option == '0':
            player_turn = False
        else:
            raise Exception("Not valid option")

        if self._services.parity(self._n) is True and self._services.parity(self._m) is True:
            moves = []
            middle_row = int(self._n/2)
            middle_column = int(self._m/2)
            while not(self._services.is_full(self._board)):
                try:
                    if player_turn:
                        r = int(input("Enter row: "))
                        c = int(input("Enter col: "))
                        s = input("Enter symbol(X): ")
                        if self._services.check_symbol(s) is True:

                            r = r-1
                            c = c-1

                            moves.append((r, c))
                            self._services.move_player(self._board, r, c, s)
                        else:
                            raise ValueError("Not the good symbol!")
                    else:
                        # computers turn
                        x, y = self._services.computer_strategy(self._board, moves, middle_row, middle_column)
                        print("Computer move was at row " + str(x+1) + " and column " + str(y+1))

                    print(str(self._board))
                    player_turn = not player_turn
                except Exception as ve:
                    print(ve)

        else:
            while not (self._services.is_full(self._board)):
                try:

                    if player_turn:
                        r = int(input("Enter row: "))
                        c = int(input("Enter col: "))
                        s = input("Enter symbol(X): ")
                        if self._services.check_symbol(s) is True:
                            r = r - 1
                            c = c - 1
                            self._services.move_player(self._board, r, c, s)
                        else:
                            raise ValueError("Not the good symbol!")
                    else:
                        # computers turn
                        x, y = self._services.complete_computer_turn(self._board)
                        print("Computer move was at row " + str(x + 1) + " and column " + str(y + 1))

                    print(str(self._board))
                    player_turn = not player_turn
                except Exception as ve:
                    print(ve)

        if player_turn:
            print("You lost!")
        else:
            print("You win!")









