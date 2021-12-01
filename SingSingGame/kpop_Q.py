import tkinter
import tkinter.font

import game
import KQ_menu
import kpop_Q2
import pygame
import time

class Kpop_Q:
    def __init__(self, Kpop_Q):
        self.Kpop_Q = Kpop_Q

        self.Background = tkinter.PhotoImage(file="image/background.png")
        self.BackgroundL = tkinter.Label(image=self.Background)
        self.BackgroundL.place(x=-2, y=-2)
        # self.BackgroundL.pack()

        self.menuFont = tkinter.font.Font(size=25, weight="bold")
        self.menu = tkinter.Label(self.Kpop_Q, text=" << 노래재생 >> ", foreground="#78a6c2", font=self.menuFont)
        self.menu.place(x=100, y=40)

        self.songButton = tkinter.Button(self.Kpop_Q, text="노래 틀기", command=self.sound, repeatdelay=20)
        self.songButton.place(x=380, y=50)

        self.Button1 = tkinter.Button(self.Kpop_Q, text="색안경",command=self.false, repeatdelay=20, width=10, height=3)
        self.Button1.place(x=300, y=210)

        self.Button2 = tkinter.Button(self.Kpop_Q, text="weekend",command=self.right, repeatdelay=20,width=10, height=3)
        self.Button2.place(x=500, y=210)

    def sound(self):
        pygame.init()  # 초기화

        weekend = pygame.mixer.Sound('music/weekend.mp3')
        weekend.play(-1)

        print("소리")

        while True:
            time.sleep(1.5)
            weekend.stop()
            break
        pygame.quit()

    def right(self):
        self.menuFont = tkinter.font.Font(size=25, weight="bold")
        self.menu = tkinter.Label(self.Kpop_Q, text=" 정답입니다. ", foreground="#78a6c2", font=self.menuFont)
        self.menu.place(x=100, y=40)
        self.nextbutton = tkinter.Button(self.Kpop_Q, text="다음문제로", command=self.nextQuiz, repeatdelay=20)
        self.nextbutton.place(x=570, y=430)
        self.stopbutton = tkinter.Button(self.Kpop_Q, text="그만하기", command=self.moveHomeBtn, repeatdelay=20)
        self.stopbutton.place(x=680, y=430)

    def false(self):
        self.menuFont = tkinter.font.Font(size=25, weight="bold")
        self.menu = tkinter.Label(self.Kpop_Q, text=" 틀렸습니다. ", foreground="#78a6c2", font=self.menuFont)
        self.menu.place(x=100, y=40)
        self.nextbutton = tkinter.Button(self.Kpop_Q, text="다음문제로", command=self.nextQuiz, repeatdelay=20)
        self.nextbutton.place(x=570, y=430)
        self.stopbutton = tkinter.Button(self.Kpop_Q, text="그만하기", command=self.moveHomeBtn, repeatdelay=20)
        self.stopbutton.place(x=680, y=430)

    def moveHomeBtn(self):
        game.Start(self.Kpop_Q)

    def nextQuiz(self):
        KQ_menu.KQ_menu(self.Kpop_Q)
        kpop_Q2.Kpop_Q2(self.Kpop_Q)
