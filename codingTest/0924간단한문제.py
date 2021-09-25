# 1)

letters = 'python'
print(letters[0] + " " + letters[2])

# 2)

license_plate = "24가 2210"
print(license_plate[-4:])

# 3)

phone_number = '010-1111-2222'

# 문자열을 다 찾은 다음 '-'를 ''로 대체
phone_number = phone_number.replace('-', ' ')
print(phone_number)

# result = ''
#
# for x in phone_number:
#     if x == '-':
#         result += x
#     else:
#         result += ' '
#
# print(result)

# 4)

url = "http://sharebook.kr"
print(url[-2:])

# 5)

t1 = 'python'
t2 = 'java'

print((t1 + ' ' + t2 + ' ') * 4)

# 6)

상장주식수 = '5,969,782,550'
a = 상장주식수.replace(',', ' ')
print(a)

# 7)

ticker = "btc_krw"
ticker = ticker.replace('_', ' ')
print(ticker)

# 8)

movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]
movie_rank.append("배트맨")
print(movie_rank)

# 9)

movie_rank = ['닥터 스트레인지', '스플릿', '럭키', '배트맨']
movie_rank.insert(1, '슈퍼맨')
print(movie_rank)

# 10)

movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '배트맨']
movie_rank.remove('럭키')
print(movie_rank)

# 11)

nums = [1, 2, 3, 4, 5]
print(sum(nums))

# 12)

cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "쏘세지", "라면", "팥빙수", "김치전"]
print(len(cook))

# 13)

nums = [1, 2, 3, 4, 5]
avg = sum(nums, 0)/len(nums)
print(avg)

# 14)

nums = [1, 2, 3, 4, 5]
print(nums[::-1])

# 15)

interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print("/".join(interest))

# 16)

string = "삼성전자/LG전자/Naver"
print(string.split('/'))

# 17)

data = [2, 4, 3, 1, 5, 10, 9]
data = sorted(data, reverse=False)
print(data)

# 18)

time = input("현재 시간 : ")

if time[-2:] == "00":
    print("정각 입니다.")
else:
    print("정각이 아닙니다.")

# 19)

리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']

for i in 리스트:
    r = i.split('.')
    if r[1] == 'h':
        print(i)

# 20)

for num in range(10):
    print(num / 10)

# 21)

apart = [[101, 102], [201, 202], [301, 302]]

for row in apart:
    for col in row:
        print(col, "호")

# 22)

list = [3, 4, 5, 6, 7, 8]

def pickup_even(list):
    result = []
    for l in list:
        if list % 2 == 0:
            result.append(list)
    return result