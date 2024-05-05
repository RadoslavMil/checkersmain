import json
import random
import os  
import pygame
from pygame.locals import *

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = HEIGHT // ROWS

class Piece:
    def __init__(self, color):
        self.color = color

    def can_move(self):
        pass

class CheckerPiece(Piece):
    def __init__(self, color, row, col):
        super().__init__(color)
        self.row = row
        self.col = col

    def can_move(self):
        return True

class Board:
    def setup(self):
        pass

class CheckerBoard:
    def __init__(self):
        self.board = [[' ' for _ in range(8)] for _ in range(8)]
        self.player = 'W'  
        self.setup_board()

    def setup_board(self):
        for row in range(8):
            for col in range(8):
                if (row + col) % 2 == 1:
                    if row < 3:
                        self.board[row][col] = 'W'
                    elif row > 4:
                        self.board[row][col] = 'B'

    def draw(self, screen):
        for row in range(ROWS):
            for col in range(COLS):
                if (row + col) % 2 == 0:
                    pygame.draw.rect(screen, (255, 255, 255), (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                else:
                    pygame.draw.rect(screen, (0, 0, 0), (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

                piece = self.board[row][col]
                if piece != ' ':
                    if piece == 'W':
                        self.drawPiece(screen, (255, 0, 0), col, row)
                    else:
                        self.drawPiece(screen, (0, 0, 255), col, row)

    def drawPiece(self, screen, colour, col, row):
        radius = SQUARE_SIZE // 2 - 15
        x = SQUARE_SIZE * col + SQUARE_SIZE // 2
        y = SQUARE_SIZE * row + SQUARE_SIZE // 2
        pygame.draw.circle(screen, colour, (x, y), radius)

    def move_piece(self, start_row, start_col, end_row, end_col):
        piece = self.board[start_row][start_col]
        if self.is_valid_move(piece, start_row, start_col, end_row, end_col):
            self.board[end_row][end_col] = piece
            self.board[start_row][start_col] = ' '
            
    
            if abs(start_row - end_row) == 2:
                captured_row = (start_row + end_row) // 2
                captured_col = (start_col + end_col) // 2
                self.board[captured_row][captured_col] = ' '
        else:
            print("Invalid move")

    def is_valid_move(self, piece, start_row, start_col, end_row, end_col):
        if piece == ' ':
            return False
        
        if self.board[end_row][end_col] != ' ':
            return False

        if abs(start_row - end_row) != abs(start_col - end_col):
            return False

        if abs(start_row - end_row) == 1:
            return True

        if abs(start_row - end_row) == 2:
            captured_row = (start_row + end_row) // 2
            captured_col = (start_col + end_col) // 2
            if self.board[captured_row][captured_col] != ' ' and self.board[captured_row][captured_col] != piece:
                return True

        return False

class Player:
    def make_move(self):
        pass

class CheckerPlayer(Player):
    def __init__(self, color):
        self.color = color

    def make_move(self):
        
        return random.choice([((1, 2), (3, 4)), ((5, 6), (7, 8))])  

class PieceFactory:
    def create_piece(self, piece_type, color):
        if piece_type == "checker":
            return CheckerPiece(color)

class GameObserver:
    def __init__(self):
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self, event):
        for observer in self.observers:
            observer.update(event)

class ScoreBoard(GameObserver):
    def __init__(self):
        super().__init__()
        self.score = 0

    def update(self, event):
        pass

class CheckersGame:
    def __init__(self):
        self.board = CheckerBoard()
        self.players = [CheckerPlayer("red"), CheckerPlayer("black")]
        self.piece_factory = PieceFactory()
        self.observer = GameObserver()
        self.observer.add_observer(ScoreBoard())
        self.current_player_index = 0
        self.file_name = os.path.join(os.path.dirname(__file__), "checkers_game_data.json")

    def export_game_data(self):
        game_data = {
            "current_player_index": self.current_player_index,
            "board_state": [[str(piece) for piece in row] for row in self.board.board] # Convert pieces to strings
        }
        try:
            with open(self.file_name, "w") as file:
                json.dump(game_data, file)
                print("Game data exported successfully.")
        except Exception as e:
            print("Error exporting game data:", e)

    def import_game_data(self):
        try:
            with open(self.file_name, "r") as file:
                game_data = json.load(file)
                self.current_player_index = game_data["current_player_index"]
                self.board.board = [[piece for piece in row] for row in game_data["board_state"]] # Convert strings back to pieces
                print("Game data imported successfully.")
        except FileNotFoundError:
            print("No saved game data found.")
        except Exception as e:
            print("Error importing game data:", e)

    def is_game_over(self):
        red_pieces = 0
        black_pieces = 0
        for row in self.board.board:
            for piece in row:
                if piece == 'W':
                    red_pieces += 1
                elif piece == 'B':
                    black_pieces += 1
        
        if red_pieces == 0:
            print("Game Over! Black player wins!")
            return True
        elif black_pieces == 0:
            print("Game Over! Red player wins!")
            return True

        return False

    def start(self):
        self.import_game_data()

        self.board.setup()
        while not self.is_game_over():
            current_player = self.get_current_player()
            move = current_player.make_move()
            print(f"{current_player.color} player's move: {move}")
            self.current_player_index = (self.current_player_index + 1) % len(self.players)
            self.export_game_data()

        print("Game Over!")

    def get_current_player(self):
        return self.players[self.current_player_index % len(self.players)]


class CheckersGUI:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Checkers")
        self.clock = pygame.time.Clock()
        self.running = True
        self.game = CheckersGame()
        self.selected_piece = None

    def run(self):
        while self.running:
            self.events()
            self.draw()
            self.clock.tick(60)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                row, col = y // SQUARE_SIZE, x // SQUARE_SIZE
                self.handle_click(row, col)

    def draw(self):
        self.screen.fill((255, 255, 255))
        self.game.board.draw(self.screen)
        pygame.display.flip()

    def handle_click(self, row, col):
        if self.selected_piece is None:
            piece = self.game.board.board[row][col]
            if piece != ' ':
                print("Piece selected at row:", row, "col:", col)
                self.selected_piece = (row, col)
        else:
            print("Move from", self.selected_piece, "to", (row, col))
            self.game.board.move_piece(*self.selected_piece, row, col)
            self.selected_piece = None

def main():
    gui = CheckersGUI()
    gui.run()
    pygame.quit()

if __name__ == "__main__":
    main()

