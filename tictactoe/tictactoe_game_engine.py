class TictactoeGameEngine:

    def __init__(self):
        self.board = list('.' * 9)  # {'.','.','.','.','.','.','.','.','.'}
        self.turn = 'x'

    def show_board(self):
        print(self.board)

    def set(self, row, col):
        pass

    def set_winner(self):
        # - 3줄
        # | 3줄
        pass

    def change_turn(self):
        pass

if __name__ == '__main__':
    game_engine = TictactoeGameEngine()
    game_engine.show_board()  # .../n.../n...
    game_engine.set(2, 2)
    game_engine.show_board()
    game_engine.set(2, 1)
    game_engine.set(2, 3)
    game_engine.show_board()
    game_engine.board = ['.', '.', '.', 'X', 'X', 'X', '.', '.', '.']
    game_engine.set_winner()
    game_engine.change_turn()
    print(game_engine.turn)  # '0'
    game_engine.change_turn()
    print(game_engine.turn)  # 'X'
