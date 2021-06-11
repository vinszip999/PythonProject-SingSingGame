def solution(s):
    # 문자열의 갯수가 홀수일 때는 (한 개만 반환)
    # 5개일 때 -> index : 2 // 7개일 때 -> index : 3 // 9개일 때 -> index : 4
    if len(s) % 2 == 1:
        return s[len(s)//2] # 정수여야하니까 // 슬래쉬 두 개
    # 문자열의 갯수가 짝수일 때는 (두 개를 반환)
    # 4개일 때 -> index : 1,2 // 6개일 때 -> index : 2,3 8개일 떄 -> index : 3,4
    else:
        return  s[len(s)//2-1] + s[len(s)//2]

s1 = "abcde"
print(solution(s1))
s2 = "qwer"
print(solution(s2))