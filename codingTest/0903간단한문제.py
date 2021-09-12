# 8.movie_rank = ["닥터 스트레인지", "스플릿", "럭키"] 리스트에 "배트맨"을 추가하라.
# movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]
# movie_rank.append("배트맨")
# print(movie_rank)
# a = movie_rank + ["배트맨"]  # *******
# print(a)  # *******


# 9.movie_rank 리스트에는 아래와 같이 네 개의 영화 제목이 바인딩되어 있다. "슈퍼맨"을 "닥터 스트레인지"와 "스플릿" 사이에 추가하라.
# movie_rank = ['닥터 스트레인지', '스플릿', '럭키', '배트맨']
# movie_rank = ['닥터 스트레인지', '스플릿', '럭키', '배트맨']
# movie_rank.insert(1, "슈퍼맨")
# print(movie_rank)
# a = [_movie_rank[0]_] + [_"슈퍼맨"_] + movie_rank[1:]  # *******
# print(a)  # *******


# 10.movie_rank 리스트에서 '럭키'를 삭제하라.
# movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '배트맨']
# movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '배트맨']
# del movie_rank[3]
# print(movie_rank)
# movie_rank.remove('럭키')  # *******
# print(movie_rank)  # *******
# # 1번 방법
# for x in movie_rank:
#     if x == '럭키':
#         movie_rank.remove('럭키')
# print(movie_rank)
# # 2번 방법 (강추!!!!) 새로운 공간 만들기
# result = list()
# for x in movie_rank:
#     if x != '럭키':
#         result.append(x)
#     else:
#         continue  # 건너뛰기
# print(result)


# 11.다음 리스트의 합을 출력하라.
# nums = [1, 2, 3, 4, 5]
# nums = [1, 2, 3, 4, 5]
# # 1번째 방법 (for문 사용)
# sum = 0
# for i in nums:
#     sum+=i
# print(sum)
# # 2번째 방법 (sum()함수 사용)
# # 2-1. 그냥 출력하기
# print(sum(nums))
# # 2-2. result에 넣어서 출력하기
# result = sum(nums)
# print(result)


# 12.다음 리스트에 저장된 데이터의 개수를 화면에 구하라.
# cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "쏘세지", "라면", "팥빙수", "김치전"]
# cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "쏘세지", "라면", "팥빙수", "김치전"]
#
# sum = 0
# for i in cook:
#     sum+=1
# print(sum)

# 선생님 방법!!!
# a = len(cook)
# a = set(cook)  # set 중복제거!!
# print(a)

# 선생님 방법 2 !!! (조금 위험한 방법)
# result = list()
# for x in cook:
#     if x not in result:  # 중복허용 x
#         result.append(x)
#     else:
#         continue
# a = len(result)
# print(a)

# 선생님 방법 3 dick셔너리 사용하기
# 선생님의 강추 방법!! 익숙치 않은 방법이라면 set함수 사용하기!
# result = dict()
# for x in cook:
#     result[x] = 1
# a = len(result)
# print(a)


# 13.다음 리스트의 평균을 출력하라.
# nums = [1, 2, 3, 4, 5]
# nums = [1, 2, 3, 4, 5]
# sum = 0
# avg = 0
# for i in nums:
#     sum+=i
# avg = sum/len(nums)
# print(avg)

# 선생님 방법
# print(sum(nums) / len(nums))


# 14.슬라이싱을 사용해서 리스트의 숫자를 역 방향으로 출력하라.
# nums = [1, 2, 3, 4, 5]
# nums = [1, 2, 3, 4, 5]
# nums.reverse()
# print(nums)

# 선생님 방법
# a = nums[::-1]
# print(a)

# 선생님 방법 2 (원본 유지) 강추!!!
# a = list(reversed(nums))
# print(a)


# 15.interest 리스트에는 아래의 데이터가 바인딩되어 있다.
# interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
#
# interest 리스트를 사용하여 아래와 같이 화면에 출력하라.
# 출력 예시:
# 삼성전자/LG전자/Naver/SK하이닉스/미래에셋대우

# a = '/'.join(interest)
# print(a)


# 선생님 방법 1
# string = ""
# string += (interest[0] + "/")
# string += (interest[1] + "/")
# string += (interest[2] + "/")
# string += (interest[3] + "/")
# string += (interest[4] + "/")
# print(string[:-1])

# 선생님 방법 2 (반복문 사용)
# string = ""
# for x in interest:
#     string += (x+"/")
# print(string[:-1])

# 선생님 방법 3
# a = "/".join(interest)
# print(a)



# 16.회사 이름이 슬래시 ('/')로 구분되어 하나의 문자열로 저장되어 있다.
# string = "삼성전자/LG전자/Naver"
# //4반
# 이를 interest 이름의 리스트로 분리 저장하라.
# 실행 예시
# >> print(interest)
# ['삼성전자', 'LG전자', 'Naver']

# a = string.split('/')
# print(a)


# 17.리스트에 있는 값을 오름차순으로 정렬하세요.
data = [2, 4, 3, 1, 5, 10, 9]

# 첫번째 방법
# a = sorted(data)  # 원본 유지
# print(a)

# 두 번째 방법
data.sort()
print(data)




















