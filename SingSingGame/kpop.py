import tkinter
import tkinter.font

import game
import main

import kpop1
import kpop2
import kpop3
import kpop4
import kpop5

class Kpop:
    def __init__(self, kpop):
        self.kpop = kpop

        # 화면
        self.Background = tkinter.PhotoImage(file="image/background.png")
        self.BackgroundL = tkinter.Label(image=self.Background)
        self.BackgroundL.place(x=-2, y=-2)

        # menu
        self.menuFont = tkinter.font.Font(size=25, weight="bold")
        self.menu = tkinter.Label(self.kpop, text=" << MENU >> ", foreground="#78a6c2", font=self.menuFont)
        self.menu.place(x=290, y=40)

        self.kpop1 = tkinter.Button(self.kpop, text="1", command=self.moveKpop1, foreground="#78a6c2", width=18, repeatdelay=20)
        self.kpop1.place(x=160, y=150)
        self.kpop2 = tkinter.Button(self.kpop, text="2", command=self.moveKpop2, foreground="#78a6c2", width=18, repeatdelay=20)
        self.kpop2.place(x=330, y=150)
        self.kpop3 = tkinter.Button(self.kpop, text="3", command=self.moveKpop3, foreground="#78a6c2", width=18, repeatdelay=20)
        self.kpop3.place(x=160, y=210)
        self.kpop4 = tkinter.Button(self.kpop, text="4", command=self.moveKpop4, foreground="#78a6c2", width=18, repeatdelay=20)
        self.kpop4.place(x=330, y=210)
        self.kpop5 = tkinter.Button(self.kpop, text="5", command=self.moveKpop5, foreground="#78a6c2", width=18, repeatdelay=20)
        self.kpop5.place(x=500, y=210)

      # home 버튼
        self.home = tkinter.PhotoImage(file="image/home.gif")
        self.homeButton = tkinter.Button(self.kpop, text="home", image=self.home, command=self.moveHomeBtn, repeatdelay=20)
        self.homeButton.place(x=50, y=400)

        # back 버튼
        self.back = tkinter.PhotoImage(file="image/back.gif")
        self.backButton = tkinter.Button(self.kpop, text="home", image=self.back, command=self.moveBackBtn, repeatdelay=20)
        self.backButton.place(x=710, y=400)

    # kpop1,2,3,4,5 페이지로 이동
    def moveKpop1(self):
        kpop1.Kpop1(self.kpop)

    def moveKpop2(self):
        kpop2.Kpop2(self.kpop)

    def moveKpop3(self):
        kpop3.Kpop3(self.kpop)

    def moveKpop4(self):
        kpop4.Kpop4(self.kpop)

    def moveKpop5(self):
        kpop5.Kpop5(self.kpop)

    # main=home 페이지로 가기
    def moveHomeBtn(self):
        game.Start(self.kpop)

    # back 페이지로 뒤로가기
    def moveBackBtn(self):
        main.Main(self.kpop)