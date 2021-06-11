def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        # True 에 해당하는 요소(item)는 더한다
        if signs[i] is True: # 참과 거짓을 비교할 땐 == 보단 is를 많이 쓴다
            answer += absolutes[i]
        # False 에 해당하는 요소(item)는 뺀다
        else:
            answer -= absolutes[i]
    return answer

if __name__ == "__main__":
    a = [4, 7, 12]
    s = [True, False, True]
    print(solution(a, s))