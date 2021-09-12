minutes = input('PC방 이용 시간은 몇 분?')
minutes = int(minutes)
fare = minutes//10 * 1000
minutes %= 10
if minutes > 0:
    fare += 1000
print('이용금액은 ', fare, '원 입니다.')
