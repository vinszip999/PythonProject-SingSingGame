class TictactoeGameEngine:
    def __init__(self):
        self.board = list('.' * 9)  # ['.','.','.','.','.','.','.','.','.']
        self.turn = 'X'

    def show_board(self):
        # print('  '.join(self.board[0:3]))   #'  '.join(['.', '.', '.']): '.  .  .'
        # print('  '.join(self.board[3:6]))
        # print('  '.join(self.board[6:9]))
        for i, v in enumerate(self.board):
            print(v + '  ', end='')
            if i % 3 == 2:
                print()

    def set(self, row, col):
        # self.board 에 위치에다가  = self.turn
        # input -> 처리 -> output: row, col -> 처리 -> index
        # row, col -> index
        index = (row - 1) * 3 + (col - 1)
        self.board[index] = self.turn

    def position_to_index(self, row, col):
        return (row - 1) * 3 + (col - 1)

    def set_winner(self):
        # - 3줄
        for row in range(1, 3 + 1):
            if self.board[self.position_to_index(row, 1)] \
                    == self.board[self.position_to_index(row, 2)] \
                    == self.board[self.position_to_index(row, 3)] \
                    == self.turn:
                return self.turn
        # |줄
        for col in range(1, 3 + 1):
            if self.board[self.position_to_index(1, col)] \
                    == self.board[self.position_to_index(2, col)] \
                    == self.board[self.position_to_index(3, col)] \
                    == self.turn:
                return self.turn
        # /줄
        if self.board[self.position_to_index(1, 3)] \
            == self.board[self.position_to_index(2, 2)] \
            == self.board[self.position_to_index(3, 1)] \
            == self.turn:
            return self.turn
        # \줄
        if self.board[self.position_to_index(1, 1)] \
            == self.board[self.position_to_index(2, 2)] \
            == self.board[self.position_to_index(3, 3)] \
            == self.turn:
            return self.turn

        if not '.' in self.board:
            return 'd'  # draw

    def change_turn(self):
        # if self.turn == 'X':
        #     self.turn = 'O'
        # else:
        #     self.turn = 'X'
        self.turn = 'O' if self.turn == 'X' else 'X'


if __name__ == '__main__':
    game_engine = TictactoeGameEngine()
    game_engine.show_board()  # ...\n...\n...
    game_engine.set(2, 2)
    game_engine.show_board()  # ['.', '.', '.', '.', 'X', '.', '.', '.', '.']
    game_engine.set(2, 1)
    game_engine.set(2, 3)
    game_engine.show_board()  # ['.', '.', '.', 'X', 'X', 'X', '.', '.', '.']
    game_engine.board = ['.', '.', '.', 'X', 'X', 'X', '.', '.', '.']
    game_engine.set_winner()  # '-'  -> 'X'
    game_engine.change_turn()
    print(game_engine.turn)  # 'O'
    game_engine.change_turn()
    print(game_engine.turn)  # 'X'
