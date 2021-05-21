class Celebrity:
    def __init__(self, name): # 생성자메서드
        # 이름
        self.name = name
        # group
    def set_name(self, name):
        self.name = name

    def set_entertainment(self, entertainment):
        self.entertainment = entertainment

    # def info(self):
    #     print(f'이름: {self.name}\t소속사: {self.entertainment}')

    def __str__(self):
        return f'이름: {self.name}\t소속사: {self.entertainment}'

class Talent(Celebrity):
    def __init__(self, name):
        #self.name = name
        super().__init__(name) # Celebrity 클래스(부모클래스)의 생성자 호출

    def set_drama(self, drama):
        self.drama = drama


    def __str__(self):
        return super().__str__() + f'\t드라마: {self.drama}'
        # return f'이름: {self.name}\t소속사: {self.entertainment}\t드라마: {self.drama}'

class Singer(Celebrity):
    def __init__(self, name):
        super().__init__(name)
        self.song = song


    def __str__(self):
        return super().__str__() + f'\t노래: {self.song}'

현진 = Singer('현진', '신메뉴')
현진.set_entertainment('JYP')
print(현진)

필릭스 = Singer('필릭스', 'Back Door')
필릭스.set_entertainment('JYP')
print(필릭스)

스트레이키즈 = []
스트레이키즈.append(현진)
스트레이키즈.append(필릭스)
print(스트레이키즈)

for 멤버 in 스트레이키즈:
    print(멤버)

gnani = Celebrity('김진환') # new Celebrity() in java
# gnani.set_name('김진환')
gnani.set_entertainment('YG')
# gnani.info()
# print(gnani.name, gnani.entertainment)
print(gnani) # 클래스의 __str()함수 호출됨


uvini = Celebrity('이유빈')
# uvini.set_name('이유빈')
uvini.set_entertainment('미림과학고')
# uvini.info()

이광수 = Talent('이광수')
이광수.set_entertainment('킹콩')
이광수.set_drama('라이브')
print(이광수)


