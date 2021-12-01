import tkinter
import main

class Start:
    def __init__(self, start):
        self.start = start

        # start 화면 이미지
        self.startBack = tkinter.PhotoImage(file="image/first_page.png")
        self.startBackL = tkinter.Label(image=self.startBack)
        self.startBackL.place(x=-2, y=-2)

        # start 버튼
        self.startFont = tkinter.font.Font(size=11, weight="bold")
        self.startButton = tkinter.Button(self.start, text="START", command=self.move, foreground="#78a6c2", width=10, repeatdelay=20, font=self.startFont)
        self.startButton.place(x=350, y=310)

    def move(self):
        main.Main(self.start)

    def play(self):
        self.start.mainloop()

if __name__ == '__main__':
    # start 화면 만들기
    start = tkinter.Tk()
    start.title("SingSingGame")
    start.geometry("800x500+250+50")  # 너비 x 높이 + x좌표 + y좌표
    start.resizable(False, False)

    singsing = Start(start)
    singsing.play()
