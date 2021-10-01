print('<전체 한꺼번에 읽기>')

f = open('text.txt', 'r', encoding='utf-8')
data = f.read()
f.close()
print(data)

print('<한 줄식 읽기>')  # 제일 많이 쓰이는 방법

f = open('text.txt', 'r', encoding='utf-8')
while True:
    line = f.readline()  # line: 이유빈:초록색\n
    if line == '':  # 빈칸이라면 끝내라 ***중요***
        break
    print(line.rstrip())  # line.replace('\n', '') '\n' -> '<br>' 가능 이렇게 해도 됨*

f.close()

print('<전체를 한꺼번에 읽고, 줄별로 리스트>')  # 두 번째로 많이 쓰이는 방법
f = open('text.txt', 'r', encoding='utf-8')
lines = f.readlines()
f.close()
for line in lines:
    print(line.rstrip())


# quiz
# 이름 : 이유빈[tab]좋아하는 색: 초록색
# 이름 : 김효진[tab]좋아하는 색: 하늘색

print('이름: ')
print('좋아하는 색: ')

print('<전체를 한꺼번에 읽고, 줄별로 리스트>')  # 두 번째로 많이 쓰이는 방법
f = open('text.txt', 'r', encoding='utf-8')
lines = f.readlines()
f.close()
for line in lines:
    # line = '프리:노랑색'
    data = line.split(':')  # ['프리', '노랑색']
    # print('이름: ', line.rstrip()[:3]+"\t좋아하는 색: "+line.rstrip()[6:])
    print('이름: ', data[0].rstrip()+"\t좋아하는 색: "+data[1].rstrip())


