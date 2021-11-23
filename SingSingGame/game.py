import random

class Game:

    def __init__(self):
        self.user_num = 0
        self.user_name = []
        self.user_hint = []

        self.kpop_singer = ["태연", "오마이걸", "에스파", "전소미", "스테이씨"]  # 가수
        self.kpop_name = ["weekend", "dundundance", "nextlevel", "xoxo", "색안경"]  # 곡 제목
        self.kpop_song = ["가장 가까운 바다. 혼자만의 영화관", "말리지 마 지금 내 기분은 feel so high", "위협에 맞서서 제껴라 제껴라 제껴라", "반쪽 같은 소리 하지 마. 내 반쪽 이제 내 거야", "패션은 과감한 게 좋아 Like it uh huh"]  # 하이라이트

        self.ballade_singer = ["임창정", "벤", "윤종신", "허각", "다비치"]  # 가수
        self.ballade_name = ["소주한잔", "열애중", "좋니", "hello", "너에게 못했던 마지막 말은"]  # 곡 제목
        self.ballade_song = ["여보세요 나야 거기 잘 지내니", "누구보다 뜨겁게 사랑해", "사랑을 시작할때 내가 얼마나 예쁜지 모르지", "그대는 내 사랑 그리운 내 사랑", "긴밤을 새우고 아직 너를 많이 사랑한다고"]  # 하이라이트

    # 1. 씽씽게임하기
    def set_user(self):
        # 인원 수 입력받기
        while True:
            self.user_num = int(input('1~6(최대) 게임을 진행할 인원수를 입력하세요 ex) 6 : '))
            if 0 < self.user_num and self.user_num <= 6:
                # 인원 수대로 사용자명 입력받기
                count = 0
                while True:
                    name = input("사용자명을 입력하세요 : ")
                    self.user_name.append(name)
                    count += 1
                    if self.user_num == count:
                        print('감사합니다~ 모든 사용자의 이름이 정상적으로 입력되었습니다~')
                        break

            else:  # user < 0 or user > 6 :
                print('** 1~6 이상의 인원수를 다시 골라주세요 **')
                continue

    # def turn_user(self):
    #     # 랜덤함수 돌려서 순서 정하기
    #     # rn = random.randint(1, self.user_num)
    #     # print(rn)
    #     pass

    def turn_user(self):
        # 랜덤함수 돌려서 순서 정하기
        while True:
            alist = []
            for i in range(1):
                rn = random.choice(self.user_name)
                while rn in alist:
                    rn = random.choice(self.user_name)
                alist.append(rn)
            print(rn)
            print(f'{rn}차례입니다.')
            break

    def genre_songs(self):
        # 노래 장르 선택하기 (발라드, 대중가요)
        while True:
            choice_song = input("대중가요 or 발라드 중 게임을 진행할 노래 장르를 선택하세요 : ")
            if choice_song == "대중가요":
                print("지금부터 SingSingGame - 대중가요(k-pop) 버전이 시작됩니다!")
                print('-' * 50)
                length = len(self.kpop_singer)
                while True:
                    for i in range(length):
                        print(f'<다음 노래 가사를 보고 가수와 곡 제목을 쓰세요>\n {self.kpop_song[i]}')
                        user_singer_answer = input("가수 : ")
                        user_song_name = input("곡 제목 : ")
                        if user_singer_answer == self.kpop_singer[i] and user_song_name == self.kpop_name[i]:
                            print("축하합니다!! 정답을 맞추셨습니다. ")
                        elif user_singer_answer == self.kpop_singer[i] or user_song_name == self.kpop_name[i]:
                            print("안타깝게 정답을 틀리셨습니다ㅠㅠ")
                        else:
                            print("정답을 틀리셨습니다.")

            elif choice_song == "발라드":
                print("지금부터 SingSingGame - 발라드 버전이 시작됩니다!")
                print('-' * 50)
                length = len(self.ballade_singer)
                while True:
                    for i in range(length):
                        print(f'<다음 노래 가사를 보고 가수와 곡 제목을 쓰세요>\n {self.ballade_song[i]}')
                        user_singer_answer = input("가수 : ")
                        user_song_name = input("곡 제목 : ")
                        if user_singer_answer == self.ballade_singer[i] and user_song_name == self.ballade_name[i]:
                            print("축하합니다!! 정답을 맞추셨습니다. ")
                        elif user_singer_answer == self.ballade_singer[i] or user_song_name == self.ballade_name[i]:
                            print("안타깝게 정답을 틀리셨습니다ㅠㅠ")
                        else:
                            print("정답을 틀리셨습니다.")

            else:
                print("** 발라드와 대중가요 중 선택하세요 **")
                continue

    def quiz(self):
        pass
        # 문제 랜덤으로 배열에서 뽑기
        #   문제를 못 맞춘다면:
        #     힌트주기(초성, 스펠링, 글자 수)
        #     또 못 맞춘다면:
        #       탈락하고 다음 사용자 턴으로 돌아가기
        #   문제를 맞춘다면:
        #     점수 주고 배열에 저장하기
        #     다음 사용자 턴으로 돌아가기

    def __str__(self):
        pass

game = Game()
# game.set_user()
game.genre_songs()
# game.turn_user()