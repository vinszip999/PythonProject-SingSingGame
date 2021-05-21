# 숫자를 입력하고 입력받은 숫자가 몇 번 박수를 치는지 알아보자

# 방법 2 : 컴퓨터가 생각하는 방법
a = 33

count = 0

while a:
    # if a % 10 == 3 or a % 10 == 6 or a % 10 == 9:
    if a % 10 in [3, 6, 9]:
        count += 1

    a = a // 10 # 소수점 자르기 //

print(count)


