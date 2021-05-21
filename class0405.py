# range() 함수
# 1부터 10까지 홀수를 나열하세요
range(1,11,2) # 10까지니까 11로 써야함
# 10 이하 짝수 큰수부터
range(11,1,-2)
# 구구단 7단 출력하기
# i : 1~9
for i in range(1, 10): # (1, 9 + 1) 이렇게 해도 됨!!
    print(f'7 x {i} = {7*i}')

print('---------')
# 2~9단 까지 출력
for dan in range(2, 10): # 2~9
    for i in range(1, 9+1): # x1~x9
        print((f'{dan} x {i} = {dan*i}'))
    print() # 단 끝내고 한칸씩 뛰기


# 2~7단까지 출력 break 사용
for dan in range(2, 9 + 1):
    for i in range(1, 9 + 1):
        # if(dan == 7) break 이 조건문이 위에 있으면 안됨!
        print((f'{dan} x {i} = {dan*i}'))
    print()
    if dan == 7: # 7단까지 출력하고 끝내라
        break

# 구구단 2~7단을 출력하되, x1, x3, x5, x7, x9 인 것만 출력 break, continue
for dan in range(2, 9 + 1):
    for i in range(1, 9 + 1):
        # if i == 2 or i == 4 or i == 6 or i == 8:
        if i % 2 == 0:
            continue
        print((f'{dan} x {i} = {dan*i}'))
    print()
    if dan == 7: # 7단까지 출력하고 끝내라
        break
