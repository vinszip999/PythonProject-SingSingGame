import tkinter
import tkinter.font

import game
import ballade

class Ballade2:
    def __init__(self, Ballade2):
        self.Ballade2 = Ballade2

        # Ballade2 화면 이미지
        self.Background = tkinter.PhotoImage(file="image/background.png")
        self.BackgroundL = tkinter.Label(image=self.Background)
        self.BackgroundL.place(x=-2, y=-2)

        # 열애중
        self.titleFont = tkinter.font.Font(size=25, weight="bold")
        self.title = tkinter.Label(self.Ballade2, text=" ♡ 열애중 ♡ ", foreground="#d375ff", font=self.titleFont)
        self.title.place(x=315, y=40)

        # 불러오기
        self.info = open("ballade2.txt", "r", encoding="utf-8")
        addY = 150
        while True:
            self.infoData = self.info.readlines()
            if not self.infoData:
                break

            # 데이터 사용
            for self.line in self.infoData:
                self.title = tkinter.Label(self.Ballade2, text=self.line, foreground="#d375ff")
                self.title.place(x=150, y=addY)
                addY += 30

        self.info.close()

        # home, back 버튼
        self.home = tkinter.PhotoImage(file="image/home.gif")
        self.homeBtn = tkinter.Button(self.Ballade2, text="home", image=self.home, command=self.moveHomeBtn, repeatdelay=20)
        self.homeBtn.place(x=50, y=400)
        self.back = tkinter.PhotoImage(file="image/back.gif")
        self.backBtn = tkinter.Button(self.Ballade2, text="home", image=self.back, command=self.moveBackBtn, repeatdelay=20)
        self.backBtn.place(x=710, y=400)

    # home 가기
    def moveHomeBtn(self):
        game.Start(self.Ballade2)

    # 뒤로가기
    def moveBackBtn(self):
        ballade.Ballade(self.Ballade2)