# 디렉터리의 현재 파일과 디렉터리 리스트 보여주자
import os

# data = os.listdir('c:\\')  # c:\ - c 폴더 보기
# data = os.listdir('..')  # .. 상위 디렉토리
data = os.listdir('.')  # . 현재 디렉터리
data = os.listdir('my_directory')  # 하위 디렉토리
for d in data:
    print(d)
    print('is directory?: ' + str(os.path.isdir(d)))
    print('is file?: ' + str(os.path.isfile(d)))


