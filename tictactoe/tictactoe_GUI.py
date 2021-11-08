import tkinter
from tkinter import messagebox

from tictactoe_game_engine import TictactoeGameEngine

class TictactoeGUI:

    def __init__(self):
        self.game_engine = TictactoeGameEngine()
        self.init_GUI()

    def init_GUI(self):
        self.CANVAS_SIZE = 300
        self.root = tkinter.Tk()
        self.root.title('틱택토')
        self.root.geometry(f'{self.CANVAS_SIZE}x{self.CANVAS_SIZE}')
        self.root.resizable(width=False, height=False)  # 사이즈를 바꿀 수 있냐 : 없다

        self.canvas = tkinter.Canvas(self.root, bg='white', width=self.CANVAS_SIZE, height=self.CANVAS_SIZE)
        self.canvas.pack()

        self.images = {}  # { 'X': PhotoImage 객체, 'O': PhotoImage 객체 }
        self.images['X'] = tkinter.PhotoImage(file='X.gif')
        self.images['O'] = tkinter.PhotoImage(file='O.gif')

        self.canvas.bind('<Button-1>', self.click_handler)  # 바인드에서 뒤에 함수명 옆에 괄호 치면 안됨!! 괄호치면 그 때 바로 실행되서 안됨!
        #  self.click_handler 옆에 괄호 쓰면 안됨!!! *** 시험에 나옴 ***
        self.root.mainloop()

    def click_handler(self, event):
        # print(f'{event.x}, {event.y}')

        row, col = self.coordinate_to_position(event.x, event.y)
        # set row, col
        self.game_engine.set(row, col)
        # show board
        self.game_engine.show_board()
        # set winner
        winner = self.game_engine.set_winner()
        # 승지가 있거나 무승부이면, 게임오버, 결과 표시하기
        if winner == 'O' or winner == 'X':
            messagebox.showinfo('Game Over', f'{winner} 이김!!')
            self.root.quit()
        elif winner == 'd':
            messagebox.showinfo('Game Over', '무승부!!')
            self.root.quit()
        # change_turn
        self.game_engine.change_turn()

    def draw_board(self):
        pass

    def coordinate_to_position(self, x, y):
        # 주연이 방법
        # x = x // 100 + 1
        # y = y // 100 + 1
        # return x, y

        # <첫 번째 방법>
        # if 0 <= y < 100 and 0 <= x < 100:
        #     return 1, 1

        # <두 번째 방법>
        # # row
        # if 0 <= y < 100:
        #     row = 1
        # elif 100 <= y < 300:
        #     row = 2
        # elif 200 <= y < 300:
        #     row = 3
        #
        # # col
        # if 0 <= x < 100:
        #     col = 1
        # elif 100 <= x < 200:
        #     col = 2
        # elif 200 <= x < 300:
        #     col = 3
        #
        # return row, col

        # <세 번째 방법> *선생님 추천*
        row = y // (self.CANVAS_SIZE // self.game_engine.SIZE) + 1  # int(y / 100) + 1
        col = x // (self.CANVAS_SIZE // self.game_engine.SIZE) + 1  # int(x / 100) + 1

        return row, col

if __name__ == '__main__':
    ttt_GUI = TictactoeGUI()

