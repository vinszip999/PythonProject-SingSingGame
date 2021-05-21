# 숫자를 입력하고 입력받은 숫자가 몇 번 박수를 치는지 알아보자

# 방법 1 : 사람이 생각하는 방법
a = 33
# # print(type(a))
문자열 = str(a)
# # print(type(문자열)
# type를 확인하는 방법 type(변수명)

count = 0
for x in 문자열:
    if x in ['3', '6', '9']:
        # 카운트를 증가시킨다
        count += 1
print(count)


