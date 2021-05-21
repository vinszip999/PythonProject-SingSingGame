# price : 원가, grade : 회원등급
# def solution(price, grade):
#     # 5프로 할인하는 코드
#     reduced_price = 0 # 할인가 선언 / 이름 바꿀 때 단축키 shift + F6
#     if grade == "S": # S 5%, G 10%, V 15%
#         reduced_price = price * 0.05
#     elif grade == "G":
#         reduced_price = price * 0.10
#     elif grade == "V":
#         reduced_price = price * 0.15
#     return price - reduced_price

# ------------------- 2번째 방법
    # if grade == "S":
    #     return  price * 0.95
    # if grade == "G":
    #     return  price * 0.90
    # if grade == "V":
    #     return  price * 0.85

# #testcase를 위한 output
# price1 = 2500
# grade1 = "V"
# ret1 = solution(price1, grade1)
# print("Solution : return value of the function is" , ret1, ".")
#
# price2 = 96900
# grade2 = "S"
# ret2 = solution(price2, grade2)
# print("Solution : return value of the function is" , ret2, ".")

# def 보조함수(month, day):
#    month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#    total = 0;
#    for i in range(month-1): # 꼭 알아놔야함 중요!
#        total += @@@
#    total += @@@
#    return total - 1
#
# def solution(start_month, start_day, end_month, end_day):
#    start_total = 보조함수(start_month, start_day)
#    end_total = 보조함수(end_month, end_day)
#    return end_total - start_total
#
# # testcase를 위한 output
# start_month = 1
# start_day = 2
# end_month = 2
# end_day = 2
# ret = solution(start_month, start_day, end_month, end_day)
#
# # Run을 누르면 받게되는 output.
# print("Solution: return value of the function is", ret, ".")

