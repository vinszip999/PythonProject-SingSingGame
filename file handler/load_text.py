print('<전체 한꺼번에 읽기>')

f = open('text.txt', 'r', encoding='utf-8')
data = f.read()
f.close()
print(data)

print('<한 줄식 읽기>')

f = open('text.txt', 'r', encoding='utf-8')
while True:
    line = f.readline()  # line: 이유빈:초록색\n
    if line == '':  # 빈칸이라면 끝내라 ***중요***
        break
    print(line.rstrip())  # line.replace('\n', '') '\n' -> '<br>' 가능 이렇게 해도 됨*

f.close()

print('<전체를 한꺼번에 읽고, 줄별로 리스트>')
f = open('text.txt', 'r', encoding='utf-8')
lines = f.readlines()
f.close()
for line in lines:
    print(line.rstrip())


