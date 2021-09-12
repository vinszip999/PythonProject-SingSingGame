# 숫자를 입력하고 *1부터 입력받은 숫자까지*

def solution(number):
   count = 0
   for i in range(1, number + 1):
       current = i
       temp = count
       while current != 0:
           if current%10%3 == 0 and current%10 !=0:
           # if current % 10 == 3 or current % 10 == 6 or current % 10 == 9
           # if current % 10 in [3, 6, 9]:
               count += 1
           current = current // 10
   return count

# The following is code to output testcase.
number = 40
ret = solution(number)
print(ret)



# # 방법 1 : 사람이 생각하는 방법
# a = 33
# # # print(type(a))
# 문자열 = str(a)
# # # print(type(문자열)
# # type를 확인하는 방법 type(변수명)
#
# count = 0
# for x in 문자열:
#     if x in ['3', '6', '9']:
#         # 카운트를 증가시킨다
#         count += 1
# print(count)




# # 방법 2 : 컴퓨터가 생각하는 방법
# a = 33
# count = 0
#
# for x in range(1, a+1):
#     while x:
#         # if a % 10 == 3 or a % 10 == 6 or a % 10 == 9:
#         if x % 10 in [3, 6, 9]:
#             count += 1
#         x = x // 10 # 소수점 자르기 //
#
# print(count)


