import unittest
from unittest.mock import patch
import json
import os
from io import StringIO
import sys


from checkers3635 import Piece, CheckerPiece, Board, CheckerBoard, Player, CheckerPlayer, PieceFactory, GameObserver, ScoreBoard, CheckersGame, CheckersGUI

class TestCheckers(unittest.TestCase):
    def setUp(self):
        self.checkers_game = CheckersGame()

    def tearDown(self):
        test_file = "test_checkers_game_data.json"
        if os.path.exists(test_file):
            os.remove(test_file)

    def test_export_game_data(self):
        captured_output = StringIO()
        sys.stdout = captured_output

        self.checkers_game.export_game_data()

        sys.stdout = sys.__stdout__

        self.assertIn("Game data exported successfully.", captured_output.getvalue())

        self.assertTrue(os.path.exists("test_checkers_game_data.json"))

    def test_import_game_data(self):
        test_data = {"current_player_index": 1, "board_state": [[" ", "B", " ", "B", " ", "B", " ", "B"], ["B", " ", "B", " ", "B", " ", "B", " "], [" ", "B", " ", "B", " ", "B", " ", "B"], [" ", " ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " ", " "], [" ", "W", " ", "W", " ", "W", " ", "W"], ["W", " ", "W", " ", "W", " ", "W", " "], [" ", "W", " ", "W", " ", "W", " ", "W"]]}
        with open("test_checkers_game_data.json", "w") as file:
            json.dump(test_data, file)

        self.checkers_game.import_game_data()

        self.assertEqual(self.checkers_game.current_player_index, 1)

        self.assertEqual(self.checkers_game.board.board, test_data["board_state"])

    def test_is_game_over(self):

        self.assertFalse(self.checkers_game.is_game_over())

        self.checkers_game.board.board = [[" "]*8 for _ in range(8)]
        self.assertTrue(self.checkers_game.is_game_over())

    @patch('builtins.input', side_effect=[(0, 0), (1, 1)])
    def test_handle_click(self, mock_input):

        captured_output = StringIO()
        sys.stdout = captured_output

        event = pygame.event.Event(pygame.MOUSEBUTTONDOWN, pos=(0, 0))
        pygame.event.get.return_value = [event]

        checkers_gui = CheckersGUI()
        checkers_gui.handle_click(0, 0)


        sys.stdout = sys.__stdout__

        self.assertIn("Piece selected at row: 0 col: 0", captured_output.getvalue())


        self.assertEqual(checkers_gui.selected_piece, (0, 0))


        checkers_gui.handle_click(1, 1)

        self.assertIn("Move from (0, 0) to (1, 1)", captured_output.getvalue())

        self.assertIsNone(checkers_gui.selected_piece)

if __name__ == "__main__":
    unittest.main()
