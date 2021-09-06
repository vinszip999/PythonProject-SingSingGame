# 1.
# 핸드폰 요금이 62421원이 나왔다. 100원 미만은 절사한다고 한다.
# 62400원 청구. 59827원일 경우, 실제 청구 금액은?
import math

bill = 62421
print(bill//100*100)
print(bill-bill%100)
print(math.floor(bill/100)*100)
print(int(bill/100)*100)

# 2.
# 평가계획은 100점 만점에 10점 단위로 점수를 줄 수 있다.
# 채점한 결과 93점이 나왔다. 90점 부여. 56점은 60점 부여.

score = 93
print(round(score/10)*10)  # round(score/10,1) ,1 생략가능
print(round(score, -1))

# 3.
# 로또 복권 자동 생성기를 만든다면?
# (로또복권: 1~45 사이의 번호 중 랜덤으로 6개 뽑기)
import random

print(random.sample(range(1, 45 + 1), 6))

# 4.
# 1~9 숫자로 중복되지 않은 숫자 세자리를 뽑는 방법은?(185:O, 212:X)

list_r = random.sample(range(1, 9 + 1), 3)
# print(list_r)
# print(str(list_r))  # 리스트 그대로 출력됨
# list_r에서 하나씩 꺼내서 n에 넣는데 str (문자열)로 바꿔서 넣으라는 뜻!
print("".join(str(n) for n in list_r))  # 문자열 합칠 때 join ** 굉장히 참신한 방법 ** str(n)
print("".join(map(str, list_r)))

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

# # 내 생일이 이미 지났을 때 쓰는 방법 *
# if my_b_day < now:  # 만약 now 가 my_b_day 보다 과거라면
#     my_b_day = my_b_day.replace(year=2022)
# print(my_b_day - today_2)

# 8.
# 랜덤하게 번호로 자리를 배치하는 방법은?
# 제적(전출, 자퇴) 인원이 있다면?

# 마지막 번호 묻기
last_number = input("마지막 번호는? ")
# 1부터 마지막 번호까지 숫자 리스트 만들기
list_class = list(range(1, int(last_number) + 1))
# print(list_class)
# 반복
while True:
#   뺄 번호 묻기
    exclude_number = input("뺄 번호는? (enter치면 그만 빼기) ")
#   다 뺐으면 반복 끝내기
    if exclude_number == '':
        break
#   빼기
    list_class.remove(int(exclude_number))
# 섞기
random.shuffle(list_class)
# 출력하기
print('<자리>\t<학생번호>')
for i, number in enumerate(list_class):
    print(f' {i+1}\t\t\t{number}')




