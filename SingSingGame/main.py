import tkinter
import tkinter.font

import kpop
import ballade
import playGame


class Main:
    def __init__(self, main):
        self.main = main

        # main 화면 이미지
        self.mainBack = tkinter.PhotoImage(file="image/background.png")
        self.mainBackL = tkinter.Label(image=self.mainBack)
        self.mainBackL.place(x=-2, y=-2)

        # title
        self.titleFont = tkinter.font.Font(size=15, weight="bold")
        self.title = tkinter.Label(self.main, text=" ※ Sing     Sing    Game ※ ", foreground="#78a6c2", font=self.titleFont)
        self.title.place(x=270, y=40)

        # kpop 이미지
        self.kpop = tkinter.PhotoImage(file="image/kpop.gif")
        self.kpopL = tkinter.Label(image=self.kpop)
        self.kpopL.place(x=100, y=100)

        # 발라드 이미지
        self.ballade = tkinter.PhotoImage(file="image/ballade.gif")
        self.balladeL = tkinter.Label(image=self.ballade)
        self.balladeL.place(x=310, y=100)

        # 게임하기 이미지
        self.playgame = tkinter.PhotoImage(file="image/playGame.gif")
        self.playgameL = tkinter.Label(image=self.playgame)
        self.playgameL.place(x=520, y=100)

        # kpopMenuButton 버튼
        self.kpopMenuButton = tkinter.Button(self.main, text="대중가요", command=self.moveBtn1, foreground="#78a6c2", width=10, repeatdelay=20)
        self.kpopMenuButton.place(x=150, y=380)

        # balladeMenuButton 버튼
        self.balladeMenuButton = tkinter.Button(self.main, text="발라드", command=self.moveBtn2, foreground="#78a6c2", width=10, repeatdelay=20)
        self.balladeMenuButton.place(x=360, y=380)

        # PGMenuButton 버튼
        self.PGMenuButton = tkinter.Button(self.main, text="게임하기", command=self.moveBtn3, foreground="#78a6c2", width=10, repeatdelay=20)
        self.PGMenuButton.place(x=570, y=380)

    # kpop 페이지로 넘기기
    def moveBtn1(self):
        kpop.Kpop(self.main)

    # ballade 페이지로 넘기기
    def moveBtn2(self):
        ballade.Ballade(self.main)

    # playgame 페이지로 넘기기
    def moveBtn3(self):
        playGame.PlayGame(self.main)
