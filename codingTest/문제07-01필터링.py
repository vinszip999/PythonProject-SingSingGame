sentence1 = "never odd or even."

str = ' '
# 문자열에 있는 원소 하나씩 출력해보기
for x in sentence1:
    if x != ' ' and x != ' ':
        str += x

print(str)

# def solution(number):
#    count = 0
#    for i in range(1, number + 1):  # for(int i=1; i<number+1)
#        current = i
#        temp = count
#        while current != 0:
#            if (i == 3) or (i == 6) or (i == 9):
#                count += 1
#                print("pair", end = '') # 디버깅을 위한 출력(없어도 무관)
#            current = current // 10
#        if temp == count:
#            print(i, end = '') # 디버깅을 위한 출력(없어도 무관)
#        print(" ", end = '') # 디버깅을 위한 출력(없어도 무관)
#    print("") # 디버깅을 위한 출력(없어도 무관)
#    return count
#
# #The following is code to output testcase.
# number = 40
# ret = solution(number)
