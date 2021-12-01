import tkinter
import tkinter.font

import game
import main

import ballade1
import ballade2
import ballade3
import ballade4
import ballade5


class Ballade:
    def __init__(self, ballade):
        self.ballade = ballade

        # 화면
        self.Background = tkinter.PhotoImage(file="image/background.png")
        self.BackgroundL = tkinter.Label(image=self.Background)
        self.BackgroundL.place(x=-2, y=-2)

        # menu
        self.menuFont = tkinter.font.Font(size=25, weight="bold")
        self.menu = tkinter.Label(self.ballade, text=" << MENU >> ", foreground="#78a6c2", font=self.menuFont)
        self.menu.place(x=290, y=40)

        self.ballade1 = tkinter.Button(self.ballade, text="1", command=self.moveBallade1, foreground="#78a6c2", width=18, repeatdelay=20)
        self.ballade1.place(x=160, y=150)
        self.ballade2 = tkinter.Button(self.ballade, text="2", command=self.moveBallade2, foreground="#78a6c2", width=18, repeatdelay=20)
        self.ballade2.place(x=330, y=150)
        self.ballade3 = tkinter.Button(self.ballade, text="3", command=self.moveBallade3, foreground="#78a6c2", width=18, repeatdelay=20)
        self.ballade3.place(x=160, y=210)
        self.ballade4 = tkinter.Button(self.ballade, text="4", command=self.moveBallade4, foreground="#78a6c2", width=18, repeatdelay=20)
        self.ballade4.place(x=330, y=210)
        self.ballade5 = tkinter.Button(self.ballade, text="5", command=self.moveBallade5, foreground="#78a6c2", width=18, repeatdelay=20)
        self.ballade5.place(x=500, y=210)

      # home 버튼
        self.home = tkinter.PhotoImage(file="image/home.gif")
        self.homeBtn = tkinter.Button(self.ballade, text="home", image=self.home, command=self.moveHomeBtn, repeatdelay=20)
        self.homeBtn.place(x=50, y=400)

        # back 버튼
        self.back = tkinter.PhotoImage(file="image/back.gif")
        self.backBtn = tkinter.Button(self.ballade, text="home", image=self.back, command=self.moveBackBtn, repeatdelay=20)
        self.backBtn.place(x=710, y=400)

    # Ballade1,2,3,4,5페이지로 이동
    def moveBallade1(self):
        ballade1.Ballade1(self.ballade)

    def moveBallade2(self):
        ballade2.Ballade2(self.ballade)

    def moveBallade3(self):
        ballade3.Ballade3(self.ballade)

    def moveBallade4(self):
        ballade4.Ballade4(self.ballade)

    def moveBallade5(self):
        ballade5.Ballade5(self.ballade)

    # home 가기
    def moveHomeBtn(self):
        game.Start(self.ballade)

    # 뒤로가기
    def moveBackBtn(self):
        main.Main(self.ballade)