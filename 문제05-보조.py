# 숫자를 입력하고 *1부터 입력받은 숫자까지*


# 방법 2 : 컴퓨터가 생각하는 방법
a = 33
count = 0

for x in range(1, a+1):
    while x:
        # if a % 10 == 3 or a % 10 == 6 or a % 10 == 9:
        if x % 10 in [3, 6, 9]:
            count += 1
        x = x // 10 # 소수점 자르기 //

print(count)


