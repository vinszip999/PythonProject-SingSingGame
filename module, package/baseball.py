from baseball_game_engine import make_answer, check

answer = make_answer()
# print(answer)

# number = random.sample(range(0, 9), 3)
# print(str(number[0]) + str(number[1]) + str(number[2]))

# 무한반복
while True:
    # 숫자 묻자
    guess = input("숫자를 입력하세요 : ")
    # strike, ball 판정하자
    strike, ball = check(guess, answer)
    # 출력하자
    print(f'{guess}\tstrike : {strike}, ball : {ball}')
    # 정답 == 숫자, 끝내기
    if answer == guess:
        print('정답입니다!!')
        break
