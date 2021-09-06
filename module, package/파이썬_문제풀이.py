# 1.
# 핸드폰 요금이 62421원이 나왔다. 100원 미만은 절사한다고 한다.
# 62400원 청구. 59827원일 경우, 실제 청구 금액은?

pay = int(input("요금을 입력하세요 : "))
sum = pay-(pay%10)
print("100원 미만의 금액이 절사된 요금은 : ", sum)


# 2.
# 평가계획은 100점 만점에 10점 단위로 점수를 줄 수 있다.
# 채점한 결과 93점이 나왔다. 90점 부여. 56점은 60점 부여.

score = int(input("점수를 입력하세요 : "))
result1 = round(score,-1)
print(result1)

# 3.
# 로또 복권 자동 생성기를 만든다면?
# (로또복권: 1~45 사이의 번호 중 랜덤으로 6개 뽑기)

import random
print("1~45 사이의 번호 중 랜덤으로 숫자 뽑기 : ", random.randint(1, 45))

# 4.
# 1~9 숫자로 중복되지 않은 숫자 세자리를 뽑는 방법은?(185:O, 212:X)

# number = set()
# while len(number) < 3:
#     number.add(random.randint(1, 9))  # 추가할 숫자가 중복이면 추가가 되지 않음.
#     # num = number[0] + number[1] + number[2]
# # result2 = ''
# # for i in number:
# #     result2+=i
# print(str(number[0]) + str(number[1]) + str(number[2]))
# # print("1~9까지 숫자 중 중복되지 않은 세자리 숫자 뽑기 : ", result2)

# <하람스 콜링>
number = random.sample(range(1, 9), 3)
# print('4번 문제 : ', number[0]*100 + number[1]*10 + number[2])
print('4번 문제 : ', str(number[0]) + str(number[1]) + str(number[2]))

# 5.
# 내가 태어난 날로부터 며칠이 지났는지?

import datetime
now = datetime.datetime.now()
birthday = datetime.datetime(2004, 11, 29)
print("내가 태어난 날로부터 몇일이 지났는가? ", now - birthday)

# 6.
# 올해 크리스마스까지 며칠이 남았는지?

today = datetime.date.today()
cm_day = datetime.date(2021, 12, 25)
print("올해 크리스마스까지 며칠이 남았는가? ", cm_day - today)

# 7.
# 내 생일이 며칠 남았는지?

today_2 = datetime.date.today()
my_b_day = datetime.date(2021, 11, 29)
print("내 생일이 며칠이 남았는가? ", my_b_day - today_2)

# 8.
# 랜덤하게 번호로 자리를 배치하는 방법은?
# 제적(전출, 자퇴) 인원이 있다면?


