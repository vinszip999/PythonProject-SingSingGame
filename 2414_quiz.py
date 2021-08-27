'''
Quiz1) 변수를 이용하여 다음 문장을 출력하시오
변수명
 : station
변수값
 : "사당", "신도림", "인천공항" 순서대로 입력
출력 문장
 : XX 행 열차가 들어오고 있습니다.
'''
# station = "사당" # 한번에 보기 위해서 3번 출력함
# print(station + "행 열차가 들어오고 있습니다.")
# station = "신도림"
# print(station + "행 열차가 들어오고 있습니다")
# station = "인천공항"
# print(station + "행 열차가 들어오고 있습니다.")
#
# '''Quiz2) 당신은 최근에 코딩 스터디 모임을 새로 만들었습니다.
# 월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인으로 하기로 했습니다.
# 아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오.
#
# 조건1 : 랜덤으로 날짜를 뽑아야 함
# 조건2 : 월별 날짜는 다름을 감안하여 최소 일수인 28 이내로 정함
# 조건3 : 매월 1~3일은 스터디 준비를 해야 하므로 제외
#
# (출력문 예제)
# 오프라인 스터디 모임 날짜는 매월 x 일로 선정되었습니다.'''
# # day = int(random()*28) + 1
# # print("오프라인 스터디 모임 날짜는 매월 " + str(day) + "일로 선정되었습니다.")
#
# from random import *
# date = randint(4,28)
# print("오프라인 스터디 모임 날짜는 매월 " + str(date) + "일로 선정되었습니다.") # 숫자는 string 변환 해야함!!
#
# '''Quiz3) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오
# 예) http://naver.com
# 규칙1 : http:// 부분은 제외 => naver.com
# 규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"로 구성
#                 (nav)               (5)             (1)         (!)
# 예) 생성된 비밀번호 : nav51!
# '''
# # www.daum.net
#
# url = "http://daum.met"
# my_str = url.replace("http://", "") #규칙1
# # print(my_str)
# my_str = my_str[:my_str.index(".")] # my_str[0:5] -> 0 ~ 5 직전까지. (0, 1, 2, 3, 4)
# print(my_str)
# password = my_str[:3] + str(len(my_str)) + str(my_str.count("e"))  + "!"# 정수이기 때문에 str로 감싸줌
# print("{0} 의 비밀번호는 {1} 입니다.".format(url, password))

# Quiz4) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
# 참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
# 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
# 추첨 프로그램을 작성하시오.
#
# 조건 1: 편의상 댓글은 20명이 작성하였고 아이디는 1~20명 이라고 가정
# 조건 2: 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
# 조건 3: random 모듈의 shuffle과 sample을 활용

# (활용 예제)
# from random import *
# lst = [1,2,3,4,5]
# # print(lst)
# # shuffle(lst)
# # print(lst)
# print(sample(lst, 1))


# from random import *
# users = range(1,21) # 1~20까지 숫자를 생성
# # print(type(users))
# users = list(users)
# # print(type(users))
#
# print(users)
# shuffle(users)
# print(users)
#
# winners = sample(users, 4) # 4명 중에서 1명은 치킨, 3명은 커피를 줌
#
# print(" -- 당첨자 발표 -- ")
# print("치킨 당첨자 : {0}".format(winners[0]))
# print("커피 당첨자 : {0}".format(winners[1:]))
# print(" -- 축하합니다 -- ")
#
# '''
# 3-1.주민등록번호 앞 6자리를 변수 id_number에 넣고,
# 출생년도 끝 두자리\n출생 월일\n그 두개의 곱 출력
# 예시
# id_number = 020316 일 때
#
# 출력 예시
# 02
# 0316
# 632
# '''
#
# id_number = "041129"
# a = int(id_number[:2])
# b = int(id_number[-4:])
# print(id_number[0:2])
# print(id_number[-6:-4]) # 똑같다!
# print(id_number[-4:])
# print(id_number[2:6]) # 2: 이렇게 해도됨!
# print(a*b)
#
# '''
# 3-2. 집 전화번호를 phone_number에 넣고,
# 지역번호\n맨 끝 네 자리 출력하기(지역번호의 자리수와 상관없이 동작하도록 하자)
# 예시
# phone_number = 02-1234-5678 또는 032-9876-4321
#
# 출력 예시
# 02 또는 032
# 5678 또는 4321
# '''
# phone_number = "02-1234-5678"
# print(phone_number[:phone_number.index('-')])
# print(phone_number[8:])

# Quiz 5)
# from random import *
# cnt = 0 # 총 탑승 승객 수
# for i in range(1, 51): # 1 ~ 50 이라는 수 (승객)
#     time = randrange(5,51) # 5분 ~ 50분 소요 시간
#     if 5 <= time <= 15: # 5분 ~ 15분 이내의 손님 (매칭 성공), 탑승 승객 수 증가 처리
#         print("[0] {0}번째 손님 (소요시간 : {1}분)".format(i,time))
#         cnt += 1
#     else: # 매칭에 실패한 경우
#         print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
# print("총 탑승 승객 : {0} 분".format(cnt))


# QuiZ 6)
# def std_weight(height, gender): # 키 m 단워 (실수), 성별 "남자" / "여자"
#     if gender == "남자":
#         return height * height * 22
#     else:
#         return height * height * 21
#
# height = 175 # cm 단위
# gender = "남자"
# weight = round(std_weight(height / 100, gender), 2)
# print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))


# Quiz2-1. 학번을 student_number 변수에 넣고, 학급을 출력하고, 학과를 출력하기
# 반이 0 미만이거나 7 이상이면 "잘못 입력했습니다." 출력하기
# student_number = '2100' 또는 student_number = '2000'
# <출력 예시>
# 1반 뉴미디어소프트웨어과 또는 잘못 입력했습니다.

# number = '2600'
# number=int(number)majors=['뉴미디어소프트웨어과', "뉴미디어웹솔루션과", "뉴미디어디자인과"]
# if 1<= number <= 6:
#     print(f'{number}반 {majors[(number-1)//2]}')
# else:
#     print("잘못 입력했습니다.")


# Quiz2-2. 학번을 함수의 인수(argument)로 전달하여 호출하면 학년과 학과를 리턴하는 함수 만들기
# <함수 호출>
# grade, major = get_major('2100')
# print(major, grade) #뉴미디어소프트웨어과 2

# def get_major(number):
#     global major
#     grade=number[0]
#
#     number=number[1]
#     if number == '1' or number =='2':
#         major = "뉴미디어소프트웨어과"
#     elif number == '3' or number =='4':
#         major = "뉴미디어웹솔루션과"
#     elif number == '5' or number =='6':
#         major = "뉴미디어디자인과"
#     return  major, grade
#
# major, grade= get_major('1200')
# print(major, grade)

# Quiz2-3. 인수의 개수에 상관없이 인수로 숫자를 여러개 넣고, 함수를 호출하면 그 인수들의 평균을 구하여 리턴하는 함수 만들기
# <함수 호출>
# print(average(10, 20, 30)) #20.0
# print(average(4, 23)) #13.5

# def average(*num):
#     sum = 0
#     for i in num:
#         sum += i
#         avg = sum/len(num)
#     return avg
# print(average(10, 20, 30))
# print(average(4, 23))

# Quiz2-4. 키(cm)와 몸무게(kg)를 인수로 넣고, 함수를 호출하여 BMI 지수를 리턴하는 함수 만들기
# (소수 첫째자리까지 반올림)
# * BMI 지수 계산법: 체중(kg) ÷ 키의 제곱(m²)
# 18.5 미만: 저체중
# 18.5 이상 23 미만: 보통
# 23 이상 25 미만: 과체중
# 25 이상: 비만

# <함수 호출>
# bmi = get_bmi(176, 69)
# print(bmi) #22.3

# def get_bmi(height, weight):
#     bmi = round(((weight) / ((height/100) * (height/100))), 1)
#     return bmi
# bmi = get_bmi(176,69)
# print(bmi)

# Quiz3-1. n_sum() 함수를 만든다. 함수의 인수(argument)로 10자리 숫자보다 작은 숫자를 넣으면, 각 자리의 숫자의 합계를 리턴한다.
# 10자리 이상이면 -1 리턴한다.


# def n_sum(argument):
#     str_num = str(argument) # 문자열로 바꿔줌
#     if (10 <= len(str_num)): # 배열의 길이 (문자열의 길이) len = 길이 구하는 함수
#         return -1
#     sum_value = 0
#     # for i in range(len(str_num)):   #range(3): i:0 1 2
#     #     sum_value += int(str_num[i])
#     for x in str_num : #str_num: '408'  x: '4' '0' '8'
#         sum_value += int(x)
#
#     return sum_value
#
# result = n_sum(10)
# print(result)        #1
# result = n_sum(331)
# print(result)         #7
# result = n_sum(408)
# print(result)         #12
# result = n_sum(1000000000)
# print(result)         #-1

# 선생님이랑 같이 한 것
# def n_sum(n):
#     # 하나씩 쪼개자
#     n = 123
#         # 1, 2, 3
#         # 123 /// 100 : 1
#         # 123 // 10 : 2
#         # 123 % 10 : 3
#     # 123 -> "123"
#     n = str(n)

# Quiz3-2. get_subway_fare() 함수를 만든다. 이 함수는 인수로 가는 거리(km)를 숫자로 넣으면, 요금을 리턴한다.
# * 지하철 요금계산법 10km 이내: 720원(청소년), 10~50km: 5km 마다 100원, 50km 초과 시 8km 마다 100원
# import math
# def get_subway_fare(km):
#     money = 720 # 남은 얘들은 계산할 수 없으니까 math.ceil 함수를 써서 반올림을 해주는 것이다.
#     if 10 < km and 50 >= km: # 11부터니까 km 에서 10을 빼주는 것이고, 5km 마다 이니까 끝이 5의 배수 0이나 5로 끝나니까 5로 나눠주는 것
#         money += math.ceil((km-10)/5)*100 # 10km 부터니까 -10을 한거고 5키로에 100원
#     elif km > 50:
#         money += 800 # 50km 까지 갔을 때가 800원
#         money += math.ceil((km-50)/8)*100
#     return money
#     # if 10 > km:
#     #     return money
#     #
#     # elif 10 < km or 50 > km:
#     #     while km % 5 == 0:
#     #         money = money + 100
#     #     return money
#
#     # for i in range(1, 50+1):
#
# fare = get_subway_fare(5)
# print(fare)        #720
# fare = get_subway_fare(26)
# print(fare)        #1120
# fare = get_subway_fare(61)
# print(fare)        #1720

# Quiz3-3. get_three_six_nine() 함수를 만든다. 이 함수에 숫자를 입력하면 369 게임에  해당하는 답변을 리턴한다.
# * 369게임: 숫자의 어느 자리든 3 또는 6 또는 9가 있다면 그 갯수만큼 '짝'을 외치고, 아니면 그냥 숫자를 외친다.
# 힌트: 문자열 함수 중에 특정 글자를 세는 함수가 있음

# def get_three_six_nine(number):
#     num = str(number)
#     count = 0
#     for i in num: # 31이면 숫자인가 짝인가
#
#         if (i == '3') or (i == '6') or (i == '9'):
#             count +=1
#     if count==0:
#         return number
#     return count * '짝'

# def get_three_six_nine(number):
#     num = str(number)
#     while num.count('3') or num.count('6') or num.count('9'):
#         if num==0:
#             return num
#             break
#         # if num != num.count('3') or num.count('6') or num.count('9'):
#         #     return num
#         else:
#             return num*'짝'
#             break

# def get_three_six_nine(number):
#     for num in range(1, 100+1):
#         c = str(num).count('3') + str(num).count('6') + str(num).count('9')
#         if c==0:
#             return num
#         else:
#             return num*'짝'

# def get_three_six_nine(number):
#     number = str(number)
#     count_369=0
#     for i in number:
#         if(i == '3') or (i == '6') or (i == '9'):
#             count_369 += 1
#     else:
#         return count_369 * '짝'
#
# result = get_three_six_nine(1)
# print(result)        #1
# result = get_three_six_nine(3)
# print(result)        #짝
# result = get_three_six_nine(16)
# print(result)        #짝
# result = get_three_six_nine(36)
# print(result)        #짝짝


# Quiz3-4. 나만의 재미난 문제를 만들어보세요. 단, 조건이 있습니다.
# 1. 함수의 이름을 정해준다.
# 2. 인수로 넣어야하는 자료형이나 개수를 말해준다.
# 3. 리턴하는 것을 말해준다.
# 4. 출력 예시를 보여준다.
# 5. 내가 낸 문제의 답안을 제출한다.

# 펙토리아 계산기
# 함수이름 : factoria(int형 숫자 하나 입력)
# def factoria(k):
#     result = 1
#     for i in range(2, k+1):
#         result *= i
#     return result
# print('펙토리아를 구할 숫자를 입력하세요 (ex 4) \n: ')
# k = int(input())
# print('결과는 : ' , factoria(k))

# 4 입력시 결과는 : 24 (4x3x2x1)
# 5 입력시 결과는 : 120 (5x4x3x2x1)


# Quiz8) 주어진 코드를 활용하여 부동산 프로그램을 작성하시오.
#
# (출력 예제)
# 총 3대의 매물이 있습니다.
# 강남 아파트 매매 10억 2010년
# 마포 오피스텔 전세 5억 2007년
# 송파 빌라 월세 500/50 2000년
#
# [코드]
# class House:
#     # 매물 초기화 : 위치, 건물 종류, 매물 종류, 가격, 준공년도
#     def __init__(self, location, house_type, deal_type, price, completion_year):
#         self.location = location
#         self.house_type = house_type
#         self.deal_type = deal_type
#         self.price = price
#         self.completion_year = completion_year
#
#     # 매물 정보 표시
#     def show_detail(self):
#         print(self.location, self.house_type, self.deal_type, self.price, self.completion_year)
#
# houses = []
# house1 = House("강남", "아파트", "매매", "10억", "2010년")
# house2 = House("마포", "오피스텔", "전세", "5억", "2007년")
# house3 = House("송파", "빌라", "월세", "500/50", "2000년")
# houses.append(house1)
# houses.append(house2)
# houses.append(house3)
#
# print("총 {0}대의 매물이 있습니다.".format(len(houses)))
# for house in houses:
#     house.show_detail()


# '''
# Quiz4-1. [학생퀴즈] 소수판별하기(소수: 1이나 자기자신으로만 나누어 떨어지는 수)
# is_prime() 함수를 만든다.
# 인수로 1개의 숫자를 받는다.
# 인수로 넘어온 숫자가 소수(prime number)이면 "소수" 아니면, "소수 아님" 리턴한다.
# '''
# def is_prime(num):
#     if num == 0 or num == 1:
#         return "소수아님"
#     else:
#         n = int(num ** 0.5)
#
#         for i in range(2, n + 1):
#             if num % i == 0:
#                 return "소수아님"
#         return "소수"
#
#
# result = is_prime(2)
# print(result)     #소수
# result = is_prime(13)
# print(result)     #소수
# result = is_prime(36)
# print(result)     #소수 아님


# '''
# Quiz4-2. [학생퀴즈] get_compliment() 함수를 만든다. 이 함수에 '고구마' 또는 '맛있는'이 들어가는 말을 입력하면 그에 해당하는 답변을 리턴한다.
# '고구마'가 들어가는 말을 입력하면 '왓쇼이!', '맛있는'이 들어가는 말을 입력하면 '우마이!',
# '놀랄 만한', '황당한', '굉장한'이 들어가는 말을 입력하면 '요모야..!', 특정 단어가 하나라도 들어가지 않는다면 '으무!'를 리턴한다.
# '''

# def get_compliment(answer):
#     if '고구마' in answer:
#         return '왓쇼이!'
#     elif '맛있는' in answer:
#         return '우마이!'
#     # elif '놀랄 만한' or '황당한' or '굉장한' in answer:
#     #     return '요모야..!'
#     elif '놀랄 만한' in answer:
#         return '요모야..!'
#     elif '황당한' in answer:
#         return '요모야..!'
#     elif '굉장한' in answer:
#         return '요모야..!'
#     else:
#         return '으무!'
#
#
# result = get_compliment('고구마 된장국')
# print(result) # 왓쇼이!
# result = get_compliment('맛있는 크레이프')
# print(result) # 우마이!
# result = get_compliment('놀랄 만한 상황')
# print(result) # 요모야..!
# result = get_compliment('좋은 마음가짐이다!')
# print(result) # 으무!



# ------------------------------------
# 2학기 첫 시작 !


'''
Quiz5-1. 모듈이란?

어떤 필요한 것들끼리 부품처럼 잘 만들어진 파일이다.
예를들어, 만약 자동차를 이용하다가 타이어가 마모되거나 펑크가 났을 때 타이어만 교체하면 되는 것과,
혹은 사고가 났는데 범퍼만 파손된 상황에서 범퍼만 교체하면 되는 것과 같다.
이런식으로 소프트웨어도 타이어나 범퍼처럼 부품만 교체하거나 추가할 수 있도록 만들면 유지보수가 쉽고 코드의 재사용도 수월해지는 장점이 있다.

정리하면, 딱 필요한 것들끼리 부품처럼 잘 만드는 것이 모듈화이고,
함수정의나 클래스 등의 어떤 파이썬 문장들을 담고 있는 파일을 모듈이라고 한다.
그리고 확장자는 .py 이다.



Quiz5-2. 패키지란?

모듈들을 모아놓은 집합이다.
하나의 디렉토리에 여러 모듈 파일들을 가져다 놓은 것이라고 이해하면 된다.



Quiz5-3. theater_module.py 모듈(파일)의 price 함수를 p학번 이라는 이름으로 호출 하도록 import문을 작성하세요

from theater_module import price as p



Quiz5-4. __all__의 역할은?

파이썬은 패키지 내에서 import가 되기를 원하는 것만 공개를 하고, 
원하지 않는 것은 비공개로 설정할 수 있는데, 
__all__은 공개가 되기를 원하는 내용만 공개할 수 있도록 만들어 주는 역할을 한다.



Quiz5-5. 지금 파이썬 파일을 직접실행할 때만 실행되고, 다른 모듈에서 import할 때는 실행되지 않도록 하는 제어문은?

if __name__ == "__main__"



Quiz5-6. travel 패키지(폴더) 안에 vietnam.py 모듈(파일) 안의 VietnamPackage 클래스를 생성하고 detail 함수를 호출하는 < 가 >, < 나 >, < 다 > 에 들어갈 각 방법은?


import travel.vietnam
< 가 > 
trip_to = travel.vietnam.VietnamPackage()
trip_to.detail()


from travel import vietnam
< 나 > 
trip_to = vietnam.VietnamPackage()
trip_to.detail()



from travel.vietnam import VietnamPackage
< 다 > 
trip_to = VietnamPackage()
trip_to.detail()
'''

