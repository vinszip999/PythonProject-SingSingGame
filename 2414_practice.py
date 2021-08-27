# 숫자 자료형
# print(5)
# print(-10)
# print(3.14)
# print(1000)
# print(5+3)
# print(4*(2+1))

# # 문자 자료형
# print('풍선')
# print('나비')
# print("ㅋ"*9)
# # boolean 타입 (참/거짓)
# print(5>10)
# print(5<10)
# print(True)
# print(False)
# print(not True)
# print(not False)
# print(not (5>10))
#
# # 변수
# # 애완동물을 소개해 주세요~
# animal = "강아지"
# name = "프리"
# age = 5
# hobby = "산책"
# is_adult = age >= 3
# ''' 이렇게 하면
# 여러 문장이
# 주석처리가 되용'''
# print("우리집 " + animal + "의 이름은 " + name + "입니다.")
# hobby = "공놀이"
# # print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요")
# print(name, "는 ", age, "살이며, ", hobby,"을/를 아주 좋아해요")
# print(name + "는 어른일까요? " + str(is_adult))
#
# # 연산자
# print(1+1)
# print(3-2)
# print(5*2)
# print(6/3)
#
# print(2**3) # 2의 3제곱 = 8
# print(5%3) #2
# print(10%3)
# print(5//3) # 몫 구하는 방법
# print(10//3)
#
# print(10>3)
# print(4>=7) #False
# print(10<3)
# print(5<=5) # True
#
# print( 3==3)
# print(4==2) #False
# print( 3+2 == 7)
#
# print(1 != 3) #True ! = 같지 않다
# print(not(1!=3)) # False
#
# print((3>0) and (3<5))
# print((3>0) & (3<5))
#
# print((3>0) or (3<5))
# print((3>0) | (3<5))
#
# print(5>4>3)
# print(5>4>7) #False
#
# print(2 + 3 * 4)
# print((2+3) * 4)
# number = 2 + 3 * 4
# print(number)
# number = number + 2
# print(number)
# number += 2
# print(number)
# number *= 2
# print(number)
# number /= 2
# print(number)
# number -= 2
# print(number)
#
# number %= 2
# print(number)
#
# #숫자 처리 함수
# print(abs(-5)) # 절댓값 반환 함수
# print(pow(4,2)) # 4의 2승
# print(max(5,12)) #최대값
# print(min(5,12))
# print(round(3.14)) #반올림
# print(round(4.99))
#
# from math import *
# print(floor(4.99))
# print(ceil(3.14))
# print(sqrt(16))
#
# #랜덤함수
# from random import *
# print(random()) #0.0 ~ 1.0 미만의 임의의 값 생성
# print(random() * 10) # 0.0 ~ 10.0 미만의 임의의 값 생성
# print(int(random()*10)) # 0~10미만의 임의의 값 생성
# print(int(random()*10) + 1) # 1~10 이하의 임의의 값 생성
#
# print(int(random() * 45) + 1) # 1~45 이하의 임의의 값 생성
# print(randrange(1,46)) # 1~45 미만의 임의의 값 생성 (45포함하려면 46)
#
# print(randint(1,45)) # 1도 포함하고 45도 포함 1~45 이하의 임의의 값 생성
#
# #문자열
# sentence = '나는 소년입니다'
# print(sentence)
# sentence2 = "파이썬은 쉬워요"
# print(sentence2)
# sentence3 = """
# 나는 소년이고,
# 파이썬은 쉬워요
# """
# print(sentence3)
#
# #슬라이싱
# jumin = "990120-1234567"
#
# print("성별 : " + jumin[7])
# print("연 : " + jumin[0:2]) # 실제 자리수보다 한자리 더 해야함 (0~2직전까지)
# print("월 : " + jumin[2:4])
# print("일 : " + jumin[4:6])
# print("생년 월일 : " + jumin[:6]) # 처음부터 6직전까지
# print("뒤 7자리 : " + jumin[7:]) # 7부터 끌까지
# print("뒤 7자리 (뒤에부터) : " + jumin[-7:])
# # 맨 뒤에서(7번째부터) 끝까지
#
# #문자열 처리 함수
# python = "Python is Amazing"
# print(python.lower())
# print(python.upper())
# print(python[0].isupper())
# print(len(python))
# print(python.replace("Python", "Java"))
#
# index = python.index("n")
# print((index))
# index = python.index("n", index + 1)
# print(index)
#
# print(python.find("Java")) # find에선 원하는 값이 없을 땐 -1을 반환해주고
# #print(python.index("Java")) #index에선 원하는 값이 없을 땐 오류를 내버리면서 프로그램을 종료한다.
# print("hi")
#
# print(python.count("n"))
#
# #문자열 포멧
# # print("a" + "b")
# # print("a", "b")
#
# print("나는 %d살입니다." % 20)
# print("나는 %s을 좋아해요." % "파이썬")
# print("Apple은 %c로 시작해요. " % "A")
# # %s
# print("나는 %s살입니다." % 20)
# print("나는 %s색과 %s색을 좋아해요." %("파란", "빨간"))
#
# #방법 2
# print("나는 {}살입니다.".format(20))
# print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
# print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨간"))
# print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))
#
# # 방법 3
# print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color= "빨간"))
# print("나는 {age}살이며, {color}색을 좋아해요.".format(color= "빨간", age = 20))
#
# # 방법 4
# age = 20
# color = "빨간"
# print(f"나는 {age}살이며, {color}색을 좋아해요.")
#
# # 탈출 문자
# print("백문이 불여일견\n백견이 불여일타") #줄바꿈
#
# # \" \' : 문장 내에서 따옴표
# print('저는 "나도코딩"입니다.')
# print("저는 '나도코딩'입니다.")
# print("저는 \"나도코딩\"입니다.")
#
# # \\ : 문장 내에서 \
# print("C:\\Users\\")
#
# # \r : 커서를 맨 앞으로 이동
# print("Red Apple\rPine")
#
# # \b: 백스페이스 (한 글자 삭제)
# print("Redd\bApple")
#
# # \t : 탭
# print("Red\tApple")
#
# #리스트 []
#
# # 지하철 칸별로 10명, 20명, 30명
# subway = [10,20,30]
# print(subway)
#
# subway = ["유재석", "조세호", "박명수"]
# print(subway)
#
# # 조세호씨가 몇번째 칸에 타고 있는지
# print(subway.index("조세호"))
#
# # 하하씨가 다음 정류장에서 다음 칸에 탐
# subway.append("하하")
# print(subway)
#
# # 정형돈씨를 유재석 / 조세호 사이에 태워봄
# subway.insert(1, "정형돈")
# print(subway)
#
# # 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
# print(subway.pop())
# print(subway)
#
# # print(subway.pop())
# # print(subway)
# #
# # print(subway.pop())
# # print(subway)
#
# # 같은 이름의 사람이 몇 명 있는지 확인
# subway.append("유재석")
# print(subway)
# print(subway.count("유재석"))
#
# # 정렬도 가능
# num_list = [5,2,4,3,1]
# num_list.sort()
# print(num_list)
#
# # 순서 뒤집기도 가능
# num_list.reverse()
# print(num_list)
#
# # 모두 지우기
# num_list.clear()
# print(num_list)
#
# # 다양한 자료형과 함께 사용
# num_list = [5,2,4,3,1]
# mix_list = ["조세호", 20, True]
# # print(mix_list)
#
# # 리스트 확장
# num_list.extend(mix_list)
# print(num_list)
#
# # 사전
# cabinet = {3:"유재석", 100:"김태호"}
# print(cabinet[3])
# print(cabinet[100])
#
# print(cabinet.get(3))
# # print(cabinet[5]) 오류나고 프로그램이 바로 종료됨
# print(cabinet.get(5))
# print(cabinet.get(5,"사용 가능"))
# print("hi")
#
# print(3 in cabinet) # True
# print(5 in cabinet) # False
#
# cabinet = {"A-3":"유재석", "B-100":"김태호"}
# print(cabinet["A-3"])
# print(cabinet["B-100"])
#
# # 새 손님
# print(cabinet)
# cabinet["A-3"] = "김종국" # 유재석 빠지고 김종국 들어감
# cabinet["C-20"] = "조세호" # C-20에 조세호씨 대입
# print(cabinet)
#
# # 간 손님
# del cabinet["A-3"]
# print(cabinet)
#
# # Key들만 출력
# print(cabinet.keys())
#
# # value들만 출력
# print(cabinet.values())
#
# # key, value 쌍으로 출력
# print(cabinet.items())
#
# # 목욕탕 폐점
# cabinet.clear()
# print(cabinet)
#
# # 튜플 값을 추가하거나 변경하는 것 금지
# menu = ("돈까스", "치즈돈까스")
# print(menu[0])
# print(menu[1])
#
# name = "김종국"
# age = 20
# hobby = "코딩"
# print(name, age, hobby)
#
# (name, age, hobby) = ("김종국", 20, "코딩")
# print(name, age, hobby)
#
# # 세트(집합)
# # 중복 안됨, 순서 없음
# my_set = {1,2,3,3,3}
# print(my_set)
#
# java = {"유재석", "김태호", "양세형"}
# python = set(["유재석", "박명수"])
#
# # 교집합 (java와 python을 모두 할 수 있는 개발자)
# print(java & python)
# print(java.intersection(python))
#
# # 합집합 (java 할 수 있거나 python도 할 수 있는 개발자)
# print(java | python)
# print(java.union(python))
#
#
# # 차집합 (java는 할 수 있지만 python은 할 줄 모르는 개발자)
# print(java - python)
# print(java.difference(python))
#
# # python 할 줄 아는 사람이 늘어남
# python.add("김태호")
# print(python)
#
# # java를 까먹음
# java.remove("김태호")
# print(java)
#
# # 자료구조의 변경
# # 커피숍
# menu = {"커피", "우유", "주스"}
# print(menu, type(menu))
#
# menu = list(menu)
# print(menu, type(menu))
#
# menu = tuple(menu)
# print(menu, type(menu))
#
# menu = set(menu)
# print(menu, type(menu))

# if
# weather = input("오늘 날씨는 어때요? ")
# if weather == "비" or weather == "눈":
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물 필요 없어요.")

# temp = int(input("기온은 어때요? "))
# if 30 <= temp:
#     print("너무 더워요. 나가지 마세요")
# elif 10 <= temp and temp < 30:
#     print("괜찮은 날씨에요")
# elif 0 <= temp < 10:
#     print("외투를 챙기세요")
# else:
#     print("너무 추워요. 나가지 마세요")

# for
# print("대기번호 : 1")
# print("대기번호 : 2")

# for waiting_no in range(1, 6): # 0,1,2,3,4
#     print("대기번호 : {0}".format(waiting_no))

# starbucks = ["아이언맨", "토르", "아이엠 그루트"]
# for customer in starbucks:
#     print("{0}, 커피가 준비되었습니다.".format(customer))
#

# while
# customer = "토르"
# index = 5
# while index >= 1:
#     print("{0}, 커피가 준비 되었습니다. {1} 번 남았어요.".format(customer, index))
# index -= 1
# if index == 0:
#     print("커피는 폐기처분되었습니다.")

# customer = "아이언맨"
# index = 1
# while True:
#     print("{0}, 커피가 준비 되었습니다. {1} 번 남았어요. 호출 {1}회 ".format(customer, index))
#     index += 1

# customer = "토르"
# person = "Unknown"
#
# while person != customer :
#     print("{0}, 커피가 준비 되었습니다. ".format(customer))
#     person = input("이름이 어떻게 되세요?")

# continue, break
# absent = [2, 5] # 결석
# no_book = [7] # 책을 안가져옴
# for student in range(1, 11):
#     if student in absent:
#         continue
#     elif student in no_book:
#         print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
#         break
#     print("{0}, 책을 읽어봐".format(student))

# 한 줄 for
# 출석번호가 1 2 3 4, 앞에 100을 붙이기로 함
# students = [1, 2, 3, 4, 5]
# print(students)
# students = [i+100 for i in students]
# print(students)
#
# # 학생 이름을 길이로 변환
# students = ["Iron man", "Thor", "I am groot"]
# students = [len(i) for i in students]
# print(students)
#
# # 학생 이름을 대문자로 변환
# students = ["Iron man", "Thor", "I am groot"]
# students = [i.upper() for i in students]
# print(students)

# 함수
# def open_account():
#     print("새로운 계좌가 생성되었습니다.")
#
# # open_account()
#
# # 전달값과 반환값
# def deposit(balance, money): # 입금
#     print("입금이 완료되었습니다. 전액은 {0} 원입니다.".format(balance + money))
#     return balance + money
#
# def withdraw(balance, money): # 출금
#     if balance >= money: # 잔액이 출금보다 많으면
#         print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance - money))
#         return balance - money
#     else:
#         print("출금이 완료되지 않았습니다. 잔액은 {0} 원입니다.".format(balance))
#         return balance
#
# def withdraw_night(balance, money): # 저녁에 출금
#     commission = 100 # 수수료 100원
#     return commission, balance - money - commission
#
#
# balance = 0 # 잔액
# balance = deposit(balance, 1000)
# # balance = withdraw(balance, 2000)
# # balance = withdraw(balance, 500)
# commission, balance = withdraw_night(balance, 500)
# print("수수료 {0} 원이며, 잔액은 {1} 원입니다.".format(commission, balance))


# 기본값
# def profile(name, age, main_lang):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}" \
#           .format(name, age, main_lang))
# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")

# 같은 학교 같은 학년 같은 반 같은 수업.

# def profile(name, age=17, main_lang="파이썬"):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}" \
#           .format(name, age, main_lang))
# profile("유재석")
# profile("김태호")


# 키워드 값
# def profile(name, age, main_lang):
#     print(name, age, main_lang)
#
# profile(name = "유재석", main_lang="파이썬", age=20)
# profile(main_lang="자바", age=25, name="김태호")


# 가변인자
# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
#     print(lang1, lang2, lang3, lang4, lang5)

# def profile(name, age, *language):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
#     for lang in language:
#         print(lang, end=" ")
#     print()
#
# profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "JavaScript")
# profile("김태호", 25, "Kotlin", "Swift", "", "", "")


# 지역변수와 전역변수
# gun = 10
#
# def checkpoint(soldiers): # 경계근무
#     global gun # 전역 공간에 있는 gun 사용
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))
#
# def checkpoint_ret(gun, soldiers):
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))
#     return gun
#
# print("전체 총 : {0}".format(gun))
# # checkpoint(2) # 2명이 경계 근무 나감
# gun = checkpoint_ret(gun, 2)
# print("남은 총 : {0}".format(gun))
#
# #클래스
#
# #마린 : 공격 유닛, 군인. 총을 쏠 수 있음
#
# name = "마린" # 유닛의 이름
# hp = 40 # 유닛의 체력
# damage = 5 # 유닛의 공격력
#
# print("{0} 유닛이 생성되었습니다.".format(name))
# print("체력 {0}, 공격력 {1}\n".format(hp, damage))
#
# # 탱크 : 공격 유닛, 탱크, 포를 쏠 수 있는데, 일반 모드 / 시즈 모드.
# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35
#
# print("{0} 유닛이 생성되었습니다.".format(tank_name))
# print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))
#
# tank2_name = "탱크"
# tank2_hp = 150
# tank2_damage = 35
#
# print("{0} 유닛이 생성되었습니다.".format(tank2_name))
# print("체력 {0}, 공격력 {1}\n".format(tank2_hp, tank2_damage))
#
# def attack(name, location, damage):
#     print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format( \
#         name, location,damage ))
# attack(name, "1시", damage)
# attack(tank_name, "1시", tank_damage)
# attack(tank2_name, "1시", tank2_damage)

# 클래스
# class Unit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print("{0} 유닛이 생성 되었습니다.".format(self.name))
#         print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))
# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)

# __init__

# class Unit:
#     def __init__(self, name, hp, damage): # 파이썬에서 쓰이는 생성자
#         self.name = name # 멤버변수 name 에 전달값 name 저장
#         self.hp = hp
#         self.damage = damage
#         print("{0} 유닛이 생성되었습니다.".format(self.name))
#         print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))
#
# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)
# marine3 = Unit("마린")
# marine3 = Unit("마린", 40)

# ===========================================
# 멤버변수
# class Unit:
#     def __init__(self, name, hp, damage):
#         self.name = name # 멤버변수 name
#         self.hp = hp # 멤버변수 hp
#         self.damage = damage # 멤버변수 damage
#         print("{0} 유닛이 생성되었습니다.".format(self.name))
#         print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))
#
# # 레이스 : 공중 유닛, 비행기. 클로킹 (상대방에게 보이지 않음)
# wraith1 = Unit("레이스", 80, 5) # 체력 80, 공격력 5
# print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))
#
# # 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것 (빼앗음)
# wraith2 = Unit("빼앗은 레이스", 80, 5)
# wraith2.cloaking = True
#
# if wraith2.cloaking == True:
#     print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))

# ===========================================
# 메소드
# class AttackUnit: # 공격 유닛
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#
#     def attack(self, location): # 공격 방향
#         print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]" \
#             .format(self.name, location, self.damage))
#
#     def damaged(self, damage): # damage 만큼 유닛 피해
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage # 유닛의 체력에서 전달받은 damage 만큼 감소
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0: # 남은 체력이 0 이하이면?
#             print("{0} : 파괴되었습니다.".format(self.name))
#
# # 파이어뱃 : 공격 유닛, 화염방사기.
# firebat1 = AttackUnit("파이어뱃", 50, 16)
# firebat1.attack("5시")
#
# # 공격 2번 받는다고 가정
# firebat1.damaged(25)
# firebat1.damaged(25)

# ===========================================
# 상속
# 일반 유닛
# class Unit:
#     def __init__(self, name, hp):
#         self.name = name
#         self.hp = hp
#
# 공격 유닛
# class AttackUnit(Unit):
#     def __init__(self, name, hp, damage):
#         Unit.__init__(self, name, hp)
#         self.damage = damage
#
#     def attack(self, location): # 공격 방향
#         print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]" \
#             .format(self.name, location, self.damage))
#
#     def damaged(self, damage): # damage 만큼 유닛 피해
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage # 유닛의 체력에서 전달받은 damage 만큼 감소
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0: # 남은 체력이 0 이하이면?
#             print("{0} : 파괴되었습니다.".format(self.name))
# #메딕 : 의무병
#
# # 파이어뱃 : 공격 유닛, 화염방사기.
# firebat1 = AttackUnit("파이어뱃", 50, 16)
# firebat1.attack("5시")
#
# # 공격 2번 받는다고 가정
# firebat1.damaged(25)
# firebat1.damaged(25)

# ===========================================
# 다중 상속
# 일반 유닛
# class Unit:
#     def __init__(self, name, hp): # 공격력인 damage 제외
#         self.name = name
#         self.hp = hp
#
# 공격 유닛
# class AttackUnit(Unit):
#     def __init__(self, name, hp, damage):
#         Unit.__init__(self, name, hp)
#         self.damage = damage
#
#     def attack(self, location): # 공격 방향
#         print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]" \
#             .format(self.name, location, self.damage)) # 공간이 좁아서 2줄에 걸쳐 출력
#
#     def damaged(self, damage): # damage 만큼 유닛 피해
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage)) # 데미지 정보 출력
#         self.hp -= damage # 유닛의 체력에서 전달받은 damage 만큼 감소
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp)) # 남은 체력 출력
#         if self.hp <= 0: # 남은 체력이 0 이하이면?
#             print("{0} : 파괴되었습니다.".format(self.name)) # 유닛 파괴 처리
#
# #드랍쉽 : 공중 유닛, 수송기. 마린 / 파이어뱃 / 탱크 등을 수송. 공격 x
#
# # 날 수 있는 기능을 가진 클래스
# class Flyable:
#     def __init__(self, flying_speed): # 공중 이동 속도
#         self.flying_speed = flying_speed
#
#     def fly(self, name, location): # 유닛 이름, 이동 방향
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
#             .format(name, location, self.flying_speed))
#
# # 공중 공격 유닛
# class FlyableAttackUnit(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed): # 이름, 체력, 공격력, 공중 이동 속도
#         AttackUnit.__init__(self, name, hp, damage) # 이름, 체력, 공격력
#         Flyable.__init__(self, flying_speed) # 공중 이동 속도
#
# # 발키리 : 공중 공격 유닛, 한번에 14발 미사일 발사.
# valkyrie = FlyableAttackUnit("발키리", 200, 6, 5) # 이름, 체력, 공격력, 공중 이동 속도
# valkyrie.fly(valkyrie.name, "3시") # 3시 방향으로 발키리를 이동

# ===========================================
# 메소드 오버라이딩
# # 일반 유닛
# class Unit:
#     def __init__(self, name, hp, speed): # speed 추가
#         self.name = name
#         self.hp = hp
#         self.speed = speed # 지상 이동 속도
#
#     def move(self, location): # 이동 함수 정의
#         print("[지상 유닛 이동]")
#         print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
#             .format(self.name, location, self.speed))
#
# # 공격 유닛
# class AttackUnit(Unit):
#     def __init__(self, name, hp, speed, damage): # speed 추가
#         Unit.__init__(self, name, hp, speed) # speed 추가
#         self.damage = damage
#
#     def attack(self, location): # 공격 방향
#         print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]" \
#             .format(self.name, location, self.damage)) # 공간이 좁아서 2줄에 걸쳐 출력
#
#     def damaged(self, damage): # damage 만큼 유닛 피해
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage)) # 데미지 정보 출력
#         self.hp -= damage # 유닛의 체력에서 전달받은 damage 만큼 감소
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp)) # 남은 체력 출력
#         if self.hp <= 0: # 남은 체력이 0 이하이면?
#             print("{0} : 파괴되었습니다.".format(self.name)) # 유닛 파괴 처리
#
# #드랍쉽 : 공중 유닛, 수송기. 마린 / 파이어뱃 / 탱크 등을 수송. 공격 x
#
# # 날 수 있는 기능을 가진 클래스
# class Flyable:
#     def __init__(self, flying_speed): # 공중 이동 속도
#         self.flying_speed = flying_speed
#
#     def fly(self, name, location): # 유닛 이름, 이동 방향
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
#             .format(name, location, self.flying_speed))
#
# # 공중 공격 유닛
# class FlyableAttackUnit(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed 0
#         Flyable.__init__(self, flying_speed)
#
#     def move(self, location):
#         print("[공중 유닛 이동]")
#         self.fly(self.name, location)
#
# # 벌쳐 : 지상 유닛, 기동성이 좋음
# vulture = AttackUnit("벌쳐", 80, 10, 20) # 지상 speed 10
#
# # 배틀크루저 : 공중 유닛, 체력도 굉장히 좋음, 공격력도 좋음
# battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)
#
# vulture.move("11시")
# # battlecruiser.fly(battlecruiser.name, "9시")
# battlecruiser.move("9시") # 오버라이딩된 move() 호출

# ===========================================
# pass
# # 일반 유닛
# class Unit:
#     def __init__(self, name, hp, speed): # speed 추가
#         self.name = name
#         self.hp = hp
#         self.speed = speed # 지상 이동 속도
#
#     def move(self, location): # 이동 함수 정의
#         print("[지상 유닛 이동]")
#         print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
#             .format(self.name, location, self.speed))
#
# # 공격 유닛
# class AttackUnit(Unit):
#     def __init__(self, name, hp, speed, damage): # speed 추가
#         Unit.__init__(self, name, hp, speed) # speed 추가
#         self.damage = damage
#
#     def attack(self, location): # 공격 방향
#         print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]" \
#             .format(self.name, location, self.damage)) # 공간이 좁아서 2줄에 걸쳐 출력
#
#     def damaged(self, damage): # damage 만큼 유닛 피해
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage)) # 데미지 정보 출력
#         self.hp -= damage # 유닛의 체력에서 전달받은 damage 만큼 감소
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp)) # 남은 체력 출력
#         if self.hp <= 0: # 남은 체력이 0 이하이면?
#             print("{0} : 파괴되었습니다.".format(self.name)) # 유닛 파괴 처리
#
# #드랍쉽 : 공중 유닛, 수송기. 마린 / 파이어뱃 / 탱크 등을 수송. 공격 x
#
# # 날 수 있는 기능을 가진 클래스
# class Flyable:
#     def __init__(self, flying_speed): # 공중 이동 속도
#         self.flying_speed = flying_speed
#
#     def fly(self, name, location): # 유닛 이름, 이동 방향
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
#             .format(name, location, self.flying_speed))
#
# # 공중 공격 유닛
# class FlyableAttackUnit(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed 0
#         Flyable.__init__(self, flying_speed)
#
#     def move(self, location):
#         print("[공중 유닛 이동]")
#         self.fly(self.name, location)
#
# # 건물
# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         pass
#
# # 서플라이 디폿 : 건물, 1개 건물 = 8 유닛.
# supply_depot = BuildingUnit("서플라이 디폿", 500, "7시") # 체력 500, 생성 위치 7시
#
# def game_start():
#     print("[알림] 새로운 게임을 시작합니다.")
#
# def game_over():
#     pass
#
# game_start()
# game_over()

# ===========================================
# super
# # 일반 유닛
# class Unit:
#     def __init__(self, name, hp, speed): # speed 추가
#         self.name = name
#         self.hp = hp
#         self.speed = speed # 지상 이동 속도
#
#     def move(self, location): # 이동 함수 정의
#         print("[지상 유닛 이동]")
#         print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
#             .format(self.name, location, self.speed))
#
# # 공격 유닛
# class AttackUnit(Unit):
#     def __init__(self, name, hp, speed, damage): # speed 추가
#         Unit.__init__(self, name, hp, speed) # speed 추가
#         self.damage = damage
#
#     def attack(self, location): # 공격 방향
#         print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]" \
#             .format(self.name, location, self.damage)) # 공간이 좁아서 2줄에 걸쳐 출력
#
#     def damaged(self, damage): # damage 만큼 유닛 피해
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage)) # 데미지 정보 출력
#         self.hp -= damage # 유닛의 체력에서 전달받은 damage 만큼 감소
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp)) # 남은 체력 출력
#         if self.hp <= 0: # 남은 체력이 0 이하이면?
#             print("{0} : 파괴되었습니다.".format(self.name)) # 유닛 파괴 처리
#
# #드랍쉽 : 공중 유닛, 수송기. 마린 / 파이어뱃 / 탱크 등을 수송. 공격 x
#
# # 날 수 있는 기능을 가진 클래스
# class Flyable:
#     def __init__(self, flying_speed): # 공중 이동 속도
#         self.flying_speed = flying_speed
#
#     def fly(self, name, location): # 유닛 이름, 이동 방향
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
#             .format(name, location, self.flying_speed))
#
# # 공중 공격 유닛
# class FlyableAttackUnit(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed 0
#         Flyable.__init__(self, flying_speed)
#
#     def move(self, location):
#         print("[공중 유닛 이동]")
#         self.fly(self.name, location)
#
# # 건물
# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         super().__init__(name, hp, 0) # 부모 클래스 접근. self 없이 사용
#         self.location = location


# ===========================================
# 스타크래프트 프로젝트 전반전
# # 일반 유닛
# class Unit:
#     def __init__(self, name, hp, speed):
#         self.name = name
#         self.hp = hp
#         self.speed = speed
#         print("{0} 유닛이 생성되었습니다.".format(name))
#
#     def move(self, location):
#         # print("[지상 유닛 이동]") # 출력문 제외
#         print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
#             .format(self.name, location, self.speed))
#
#     def damaged(self, damage): # damage 만큼 유닛 피해
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage)) # 데미지 정보 출력
#         self.hp -= damage # 유닛의 체력에서 전달받은 damage 만큼 감소
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp)) # 남은 체력 출력
#         if self.hp <= 0: # 남은 체력이 0 이하이면?
#             print("{0} : 파괴되었습니다.".format(self.name)) # 유닛 파괴 처리
# # 공격 유닛
# class AttackUnit(Unit):
#     def __init__(self, name, hp, speed, damage): # speed 추가
#         Unit.__init__(self, name, hp, speed) # speed 추가
#         self.damage = damage
#
#     def attack(self, location): # 공격 방향
#         print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]" \
#             .format(self.name, location, self.damage)) # 공간이 좁아서 2줄에 걸쳐 출력
#
# # 마린
# class Marine(AttackUnit):
#     def __init__(self):
#         AttackUnit.__init__(self, "마린", 40, 1, 5) # 이름, 체력, 이동속도, 공격력
#
#     # 스팀팩 : 일정 시간 동안 이동 및 공격 속도를 증가, 체력 10 감소
#     def stimpack(self):
#         if self.hp > 10:
#             self.hp -= 10 # 체력 10 소모
#             print("{0} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
#         else:
#             print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다".format(self.name))
#
# # 탱크
# class Tank(AttackUnit):
#     # 시즈모드 : 탱크를 지상에 고정시켜, 더 높은 파워로 공격 가능. 이동 불가.
#     siege_developed = False # 시즈모드 개발여부
#
#     def __init__(self):
#         AttackUnit.__init__(self, "탱크", 150, 1, 35)
#         self.siege_mode = False
#
#     def set_siege_mode(self):
#         if Tank.siege_developed == False:  # 시즈모드가 개발되지 않은 경우 메소드 탈출
#             return
#
#         # 현재 시즈모드가 아닐 때 -> 시즈모드
#         if self.siege_mode == False:
#             print("{0} : 시즈모드로 전환합니다.".format(self.name))
#             self.damage *= 2  # 공격력 2배로 증가
#             self.siege_mode = True  # 시즈 모드 설정
#         # 현재 시즈모드일 때 => 시즈모드 해제
#         else:
#             print("{0} : 시즈모드를 해제합니다.".format(self.name))
#             self.damage /= 2  # 공격력 절반으로 감소
#             self.siege_mode = False  # 시즈 모드 해제
#
# #드랍쉽 : 공중 유닛, 수송기. 마린 / 파이어뱃 / 탱크 등을 수송. 공격 x
#
# # 날 수 있는 기능을 가진 클래스
# class Flyable:
#     def __init__(self, flying_speed): # 공중 이동 속도
#         self.flying_speed = flying_speed
#
#     def fly(self, name, location): # 유닛 이름, 이동 방향
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
#             .format(name, location, self.flying_speed))
#
# # 공중 공격 유닛 클래스
# class FlyableAttackUnit(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed 0
#         Flyable.__init__(self, flying_speed)
#
#     def move(self, location):
#         self.fly(self.name, location)
#
# # 레이스
# class Wraith(FlyableAttackUnit):
#     def __init__(self):
#         FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5) # 체력, 공격력, 공중 이동 속도
#         self.cloaked = False # 클로킹 모드 (해제 상태)
#
#         def cloaking(self):
#             if self.cloaked == True: # 클로킹 모드 -> 모드 해제
#                 print("{0} : 클로킹 모드 해제합니다.".format(self.name))
#                 self.cloaked = False
#             else: # 클로킹 모드 해제 -> 모드 설정
#                 print("{0} : 클로킹 모드 설정합니다.".format(self.name))
#                 self.cloaked = True

# ===========================================
# 스타크래프트 프로젝트 후반전
# from random import *
#
# # 일반 유닛
# class Unit:
#     def __init__(self, name, hp, speed):
#         self.name = name
#         self.hp = hp
#         self.speed = speed
#         print("{0} 유닛이 생성되었습니다.".format(name))
#
#     def move(self, location):
#         print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
#             .format(self.name, location, self.speed))
#
#     def damaged(self, damage): # damage 만큼 유닛 피해
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage)) # 데미지 정보 출력
#         self.hp -= damage # 유닛의 체력에서 전달받은 damage 만큼 감소
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp)) # 남은 체력 출력
#         if self.hp <= 0: # 남은 체력이 0 이하이면?
#             print("{0} : 파괴되었습니다.".format(self.name)) # 유닛 파괴 처리
# # 공격 유닛
# class AttackUnit(Unit):
#     def __init__(self, name, hp, speed, damage): # speed 추가
#         Unit.__init__(self, name, hp, speed) # speed 추가
#         self.damage = damage
#
#     def attack(self, location): # 공격 방향
#         print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]" \
#             .format(self.name, location, self.damage)) # 공간이 좁아서 2줄에 걸쳐 출력
#
# # 마린
# class Marine(AttackUnit):
#     def __init__(self):
#         AttackUnit.__init__(self, "마린", 40, 1, 5) # 이름, 체력, 이동속도, 공격력
#
#     # 스팀팩 : 일정 시간 동안 이동 및 공격 속도를 증가, 체력 10 감소
#     def stimpack(self):
#         if self.hp > 10:
#             self.hp -= 10 # 체력 10 소모
#             print("{0} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
#         else:
#             print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다".format(self.name))
#
# # 탱크
# class Tank(AttackUnit):
#     # 시즈모드 : 탱크를 지상에 고정시켜, 더 높은 파워로 공격 가능. 이동 불가.
#     siege_developed = False # 시즈모드 개발여부
#
#     def __init__(self):
#         AttackUnit.__init__(self, "탱크", 150, 1, 35)
#         self.siege_mode = False
#
#     def set_siege_mode(self):
#         if Tank.siege_developed == False:  # 시즈모드가 개발되지 않은 경우 메소드 탈출
#             return
#
#         # 현재 시즈모드가 아닐 때 -> 시즈모드
#         if self.siege_mode == False:
#             print("{0} : 시즈모드로 전환합니다.".format(self.name))
#             self.damage *= 2  # 공격력 2배로 증가
#             self.siege_mode = True  # 시즈 모드 설정
#         # 현재 시즈모드일 때 => 시즈모드 해제
#         else:
#             print("{0} : 시즈모드를 해제합니다.".format(self.name))
#             self.damage /= 2  # 공격력 절반으로 감소
#             self.siege_mode = False  # 시즈 모드 해제
#
# #드랍쉽 : 공중 유닛, 수송기. 마린 / 파이어뱃 / 탱크 등을 수송. 공격 x
#
# # 날 수 있는 기능을 가진 클래스
# class Flyable:
#     def __init__(self, flying_speed): # 공중 이동 속도
#         self.flying_speed = flying_speed
#
#     def fly(self, name, location): # 유닛 이름, 이동 방향
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
#             .format(name, location, self.flying_speed))
#
# # 공중 공격 유닛 클래스
# class FlyableAttackUnit(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed 0
#         Flyable.__init__(self, flying_speed)
#
#     def move(self, location):
#         self.fly(self.name, location)
#
# # 레이스
# class Wraith(FlyableAttackUnit):
#     def __init__(self):
#         FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5) # 체력, 공격력, 공중 이동 속도
#         self.cloaked = False # 클로킹 모드 (해제 상태)
#
#     def cloaking(self):
#         if self.cloaked == True:  # 클로킹 모드 -> 모드 해제
#             print("{0} : 클로킹 모드 해제합니다.".format(self.name))
#             self.cloaked = False
#         else: # 클로킹 모드 해제 -> 모드 설정
#             print("{0} : 클로킹 모드 설정합니다.".format(self.name))
#             self.cloaked = True
#
# def game_start():
#     print("[알림] 새로운 게임을 시작합니다.")
#
# def game_over():
#     print("Player : gg") # good game
#     print("[Player] 님이 게임에서 퇴장하셨습니다.")
#
# # 실제 게임 진행
# game_start()
#
# # 마린 3기 생성
# m1 = Marine()
# m2 = Marine()
# m3 = Marine()
#
# # 탱크 2기 생성
# t1 = Tank()
# t2 = Tank()
#
# # 레이스 1기 생성
# w1 = Wraith()
#
# # 유닛 일괄 관리 (생성된 모든 유닛 append)
# attack_units = []
# attack_units.append(m1)
# attack_units.append(m2)
# attack_units.append(m3)
# attack_units.append(t1)
# attack_units.append(t1)
# attack_units.append(w1)
#
# # 전군 이동
# for unit in attack_units:
#     unit.move("1시")
#
# # 탱크 시즈모드 개발
# Tank.siege_developed = True
# print("[알림] 탱크 시즈 모드 개발이 완료되었습니다.")
#
# # 공격 모드 준비 (마린 : 스팀팩, 탱크 : 시즈모드, 레이스 : 클로킹)
# for unit in attack_units:
#     if isinstance(unit, Marine):
#         unit.stimpack()
#     elif isinstance(unit, Tank):
#         unit.set_siege_mode()
#     elif isinstance(unit, Wraith):
#         unit.cloaking()
#
# # 전군 공격
# for unit in attack_units:
#     unit.attack("1시")
#
# # 전군 피해
# for unit in attack_units:
#     unit.damaged(randint(5, 20)) # 공격은 랜덤으로 받음 (5 ~ 20)
#
# # 게임 종료
# game_over()


# ----------------------------------
# 2학기 첫 시작 !

# <모듈>

# import theater_module
# theater_module.price(3)  # 3명이서 영화 보러 갔을 때 가격
# theater_module.price_morning(4)  # 4명이서 조조 할인 영화 보러 갔을 때
# theater_module.price_soldier(5)  # 5명의 군인이 영화 보러 갔을 때

# import theater_module as mv  # 모듈에 mv 라는 별명을 붙여주어서 코드를 줄일 수 있는 것!
# # c언어의 구조체에서 별명을 붙여주는 것과 비슷함!
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

# from theater_module import *  # theater_module 에 있는 모든 걸 사용하겠다.
# # from random import *
# price(3)
# price_morning(4)
# price_soldier(5)

# from theater_module import price, price_morning  # price 함수와 price_morning 함수만 가져다 쓰겠다는 뜻!
# price(5)
# price_morning(6)

# from theater_module import price_soldier as price
# # price_soldier 함수를 "price"라는 별명 붙여쓰는 방법!
# price(5)


# <패키지>

# import travel.thailand # thailand 부분은 항상 모듈이나 패키지만 가능하다.
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel.thailand import ThailandPackage  # 이 구문에선 모듈이나 패키지, 클래스 함수 모두 import 할 수 있다.
# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()


# <__all__>

# from random import *  # random 모듈 안에 있는 모든 것들을 다 사용하겠다.

# from travel import *  # *을 쓰는 것은 travel 패키지 안에 있는 모든 것들을 가져오겠다.

# **실제로는 개발자가 이 문법 상애서 공개범위를 설정해주어야 한다.**
# 이 말은 패키지 내에서 import 되기를 원하는 것만 공개를 하고,
# 원하지 않는 것은 비공개로 설정을 할 수 있다는 말이다.

# trip_to = vietnam.VietnamPackage()
# trip_to = thailand.ThailandPackage()
# trip_to.detail()


# <모듈 직접 실행>

# if __name__ == "__main__" 제어문을 사용할 수 있다.

# thailand.py 파일에서의 if __name__ == "__main__" 사용 예시
# >>>
# if __name__ == "__main__":  # __name__이 만약 "__main__" 이면,
#     print("Thailand 모듈을 직접 실행")
#     # thailand.py 에서 코드를 수정하고 직접 실행했을 때 이 구문이 실행된다.
#
#     print("이 문장은 모듈을 직접 실행할 때만 실행이 됩니다.")
#     trip_to = ThailandPackage()
#     trip_to.detail()
# else:
#     print("Thailand 외부에서 모듈 호출")
#     # practice.py 에서 thailand.py 를 가져다 쓸 때에는 이 구문이 실행된다.

# 정리 : practice.py 에서 thailand.py 를 가져다 쓸 때에는 else 구문의 문장 내용이 실행되고,
# thailand.py 에서 직접 이 내용을 실행할 때는 if 구문의 문장 내용이 실행된다.


# <패키지, 모듈 위치>
# import inspect
# import random
# print(inspect.getfile(random))
# # random 이라는 모듈이 어느 위치에 있는지, 파일 정보를 알려준다.
# print(inspect.getfile(thailand))
