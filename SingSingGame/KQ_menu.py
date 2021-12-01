import tkinter
import tkinter.font

import game
import playGame


class KQ_menu:
    def __init__(self, KQ_menu):
        self.KQ_menu = KQ_menu

        self.Background = tkinter.PhotoImage(file="image/background.png")
        self.BackgroundL = tkinter.Label(image=self.Background)
        self.BackgroundL.place(x=-2, y=-2)

        # home, back 버튼
        self.home = tkinter.PhotoImage(file="image/home.gif")
        self.homeButton = tkinter.Button(self.KQ_menu, text="home", image=self.home, command=self.moveHomeBtn, repeatdelay=20)
        self.homeButton.place(x=50, y=400)
        self.back = tkinter.PhotoImage(file="image/back.gif")
        self.backButton = tkinter.Button(self.KQ_menu, text="back", image=self.back, command=self.moveBackBtn, repeatdelay=20)
        self.backButton.place(x=710, y=400)

        # home 가기
    def moveHomeBtn(self):
        game.Start(self.KQ_menu)

        # 뒤로가기
    def moveBackBtn(self):
        playGame.PlayGame(self.KQ_menu)
