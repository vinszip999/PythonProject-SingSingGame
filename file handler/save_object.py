import pickle

from person import Person

#객체 생성하기
num15 = Person('이재령', '하얀색')
num17 = Person('임사랑', '분홍색')

#리스트 만들기
bf = [num15, num17]
# for friend in bf:
#     print(friend)

#저장하기
# 1. 객체 하나 저장
import pickle

with open('object.bin', 'wb') as f:
    # f.write(num15) 이거 사용 안됨
    pickle.dump(num15, f)
# 2. 객체 여러 개 저장
with open('objects.bin', 'wb') as f:
    pickle.dump(bf, f)


