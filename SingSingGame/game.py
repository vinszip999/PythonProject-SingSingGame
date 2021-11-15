import random

class Game:

    def __init__(self):
        self.user_num = 0
        self.user_name = []
        self.user_hint = []

    # 1. 씽씽게임하기
    def set_user(self):
        # 인원 수 입력받기
        while(True):
            self.user_num = int(input('1~6(최대) 게임을 진행할 인원수를 입력하세요 ex) 6 : '))
            if 0 < self.user_num and self.user_num <= 6:
                # 인원 수대로 사용자명 입력받기
                count = 0
                while(True):
                    name = input("사용자명을 입력하세요 : ")
                    self.user_name.append(name)
                    count += 1
                    if(self.user_num == count):
                        print('감사합니다~ 모든 사용자의 이름이 정상적으로 입력되었습니다~')
                        break

            else:  # user < 0 or user > 6 :
                print('** 1~6 이상의 인원수를 다시 골라주세요 **')
                continue

    def turn_user(self):
        # 랜덤함수 돌려서 순서 정하기
        # rn = random.randint(1, self.user_num)
        # print(rn)
        pass

    def genre_songs(self):
        # 노래 장르 선택하기 (발라드, 대중가요)
        choice_song = input("발라드 or 대중가요 중 게임을 진행할 노래 장르를 선택하세요 : ")


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
game.set_user()
# game.turn_user()