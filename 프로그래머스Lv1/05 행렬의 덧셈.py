import copy

def solution(arr1, arr2):
    row_length = len(arr1)  # row = 행
    col_length = len(arr1[0])  # col = 열
    answer = [0] * col_length
    answer = [copy.deepcopy(answer) for _ in range(row_length)]
    # answer = [answer] * row_length
    for i in range(row_length):
        for j in range(col_length):
            answer[i][j] = arr1[i][j] + arr2[i][j]

    return answer