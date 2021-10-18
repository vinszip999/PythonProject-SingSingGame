from baseball_game_engine import make_answer, check
# from custom_error import InvalidLengthError
answer = make_answer()
# print(answer)

# number = random.sample(range(0, 9), 3)
# print(str(number[0]) + str(number[1]) + str(number[2]))

count = 0
# 무한반복
while True:
    # 숫자 묻자
    guess = input("숫자를 입력하세요 : ")
    # 숫자인지 아닌지 확인하자
    try:
        guess_int = int(guess)
    except ValueError as e:
        print('*** 숫자를 입력하세요 ***')
        continue
    if len(guess) != len(answer):  # 3
        # raise InvalidLengthError('정답의 길이와 다른 것을 입력했습니다.')
        print(f'정답의 길이와 다른 것을 입력했습니다. {len(answer)} 문자')
        continue

    # print(guess_int)
    # strike, ball 판정하자
    strike, ball = check(guess, answer)
    count+=1
    # 출력하자
    print(f'{guess}\tstrike : {strike}, ball : {ball}\t{count}try')
    # 정답 == 숫자, 끝내기
    if answer == guess:
        print('정답입니다!!')
        break
