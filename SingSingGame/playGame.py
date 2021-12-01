import tkinter
import tkinter.font

import game
import main
import KQ_menu
import BQ_menu
import kpop_Q
import ballade_Q


class PlayGame:
    def __init__(self, playgame):
        self.playgame = playgame

        # playgame 화면 이미지
        self.Background = tkinter.PhotoImage(file="image/background.png")
        self.BackgroundL = tkinter.Label(image=self.Background)
        self.BackgroundL.place(x=-2, y=-2)

        # menu
        self.menuFont = tkinter.font.Font(size=25, weight="bold")
        self.menu = tkinter.Label(self.playgame, text=" << 게임을 진행할 장르를 선택하세요 >> ", foreground="#78a6c2", font=self.menuFont)
        self.menu.place(x=100, y=40)

        # 대중가요
        self.kpop = tkinter.Button(self.playgame, text="대중가요", command=self.moveKpopQ, foreground="#78a6c2", width=18, repeatdelay=20)
        self.kpop.place(x=160, y=150)

        # 발라드
        self.ballade = tkinter.Button(self.playgame, text="발라드", command=self.moveBalladeQ, foreground="#78a6c2", width=18, repeatdelay=20)
        self.ballade.place(x=480, y=150)

        # home, back 버튼
        self.home = tkinter.PhotoImage(file="image/home.gif")
        self.homeButton = tkinter.Button(self.playgame, text="home", image=self.home, command=self.moveHomeBtn, repeatdelay=20)
        self.homeButton.place(x=50, y=400)
        self.back = tkinter.PhotoImage(file="image/back.gif")
        self.backButton = tkinter.Button(self.playgame, text="home", image=self.back, command=self.moveBackBtn, repeatdelay=20)
        self.backButton.place(x=710, y=400)

    # kpop_Q로 이동
    def moveKpopQ(self):
        KQ_menu.KQ_menu(self.playgame)
        kpop_Q.Kpop_Q(self.playgame)

    # Ballade_Q로 이동
    def moveBalladeQ(self):
        BQ_menu.BQ_menu(self.playgame)
        ballade_Q.Ballade_Q(self.playgame)

    # home 가기
    def moveHomeBtn(self):
        game.Start(self.playgame)

    # 뒤로가기
    def moveBackBtn(self):
        main.Main(self.playgame)