def solution(a, b):
    result = 0
    for i in range(len(aa)):
        result += a[i] * b[i]
    return result

aa = [1, 2, 3, 4]
bb = [-3, -1, 0, 2]

print(solution(aa, bb))