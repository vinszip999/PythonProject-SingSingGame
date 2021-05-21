# 숫자를 입력하고 *1부터 입력받은 숫자까지*

def solution(number):
   count = 0
   for i in range(1, number + 1):
       current = i
       temp = count
       while current != 0:
           if current % 10 == 3 or current % 10 == 6 or current % 10 == 9:
           # if current % 10 in [3, 6, 9]:
               count += 1
           current = current // 10
   return count

# The following is code to output testcase.
number = 40
ret = solution(number)
print(ret)