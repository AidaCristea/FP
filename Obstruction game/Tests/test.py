from Services.service import Services
import unittest
from Domain.domain import Board


class ServiceTest(unittest.TestCase):
    def setUp(self):
        self._myboard = Services()
        self._domboard = Board(4, 4)

    def test_get_element(self):
        v = self._domboard.get_element(1, 1)
        self.assertEqual(v, 0)
        self._myboard.move_player(self._domboard, 1, 2, "X")
        v1 = self._domboard.get_element(1,2)
        self.assertEqual(v1, "X")

    def test_set_element(self):
        self._domboard.set_element(1,1,"X")
        self.assertEqual(self._domboard.board[1][1], "X")

    def test_parity(self):
        self.assertEqual(self._myboard.parity(5), True)
        self.assertEqual(self._myboard.parity(6), False)

    def test_check_symbol(self):
        self.assertEqual(self._myboard.check_symbol('X'), True)
        self.assertEqual(self._myboard.check_symbol("O"), False)

    def test_move_player(self):
        board = Board(4, 4)
        self._myboard.move_player(board, 1, 2, "X")
        self.assertEqual(board.board[1][2], "X")
        self.assertEqual(board.board[1][3], "/")

    def test_complete_neighburs(self):
        board = Board(4, 4)
        self._myboard.comlpete_neighburs(board, 1, 2)
        self.assertEqual(board.board[0][2], "/")
        self.assertEqual(board.board[2][3], "/")

    def test_computer_strategy(self):
        board = Board(7, 5)
        player_move = []
        self._myboard.computer_strategy(board, player_move, 3, 2)
        self.assertEqual(board.board[3][2], "O")
        self.assertEqual(board.board[3][3], "/")

    def test_first_comp_move(self):
        board = Board(5,7)
        self._myboard.first_comp_move(board, 2, 3)
        self.assertEqual(board.board[2][3], "O")
        self.assertEqual(board.board[2][4], "/")

    def test_move_computer_random_position(self):
        board = Board(4,4)
        self.assertNotEqual(self._myboard.move_computer_random_position(board), None)

    def test_complete_computer_turn(self):
        board = Board(4,4)
        self.assertNotEqual(self._myboard.complete_computer_turn(board), None)







