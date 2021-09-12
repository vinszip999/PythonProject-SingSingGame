'''
1. letters가 바인딩하는 문자열에서 첫번째와 세번째 문자를 출력하세요.
>> letters = 'python'

실행 예
p t
'''

# letters = 'python'
# print(letters[0], letters[2])



# 2. 자동차 번호가 다음과 같을 때 뒤에 4자리만 출력하세요.
# >> license_plate = "24가 2210"
#
# 실행 예: 2210

# license_plate = "24가 2210"
# # print(license_plate[4:8])
# print(license_plate[-4:])



# 3.아래의 전화번호에서 하이푼 ('-')을 제거하고 출력하세요.
# >> phone_number = "010-1111-2222"
#
# 실행 예
# 010 1111 2222

# phone_number = "010-1111-2222"
# # 문자열을 다 찾은 다음에 "-"를 " "로 대체하자 # '-' -> ' '
# # result = ""
# # for x in phone_number:  # 인덱스로 접근
# #     if x != '-':
# #         # phone_number = ''  # ***파이썬 문자열은 내부적으로 바꿀 수 없다!!!***
# #         result += x
# #     else:
# #         result += ' '
# # print(result)
#
# a = phone_number.replace('-', ' ')  # 새로운 공간할당, 그 주소값 반환
# print(a)
#
# b = phone_number.count('1')
# print(b)


# 4.url 에 저장된 웹 페이지 주소에서 끝 글자만 출력하시오.
# >> url = "http://sharebook.kr"
#
# 실행 예:
# kr
url = "http://share.book.kr"

# a = url.split('.')
# print(a[-1])

result = list()
start = 0
for i in range(len(url)):
    if url[i] == '.':
        result.append(url[start:i])
        start = i+1

# result.append(url[start:i])
print(result)


# 6.삼성전자의 상장주식수가 다음과 같습니다. 컴마를 제거한 후 이를 정수 타입으로 변환해보세요.
# 상장주식수 = "5,969,782,550"

상장주식수 = "5,969,782,550"

# print(int(상장주식수))

a = 상장주식수.replace(',', '')  # 새로운 공간할당, 그 주소값 반환
print(int(a))


# 7.다음과 같이 문자열이 있을 때 btc와 krw로 나눠보세요.
ticker = "btc_krw"
a = ticker.split('_')  # - 기준으로 쪼개기
print(a)  # print(a[0], a[1])








