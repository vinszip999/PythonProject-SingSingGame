class Drink:
    _CUPS = ('레귤러', '점보') # 기본값 '레귤러' # 내용을 수정하지 못하도록 () 요걸로 함
    _ICES = ('0%', '50%', '100%', '150%') # '100%'
    _SUGARS = ('0%', '50%', '100%', '150%') # '100%'

    def __init__(self, name, price): # 초기화
        self.name = name
        self.price = price
        self.cup = 0    # '레귤러' Drink._CUPS[self.cup]
        self.ice = 2    # '100%' Drink._ICES[self.ice]
        self.sugar = 2    # '100%' Drink._SUGARS[self.sugar]

    def set_cup(self):
        for index, cup in enumerate(Drink._CUPS): # 컵 종류 보여주기
            print(f'{index + 1}: {cup}')
        # 컵 선택하기
        cup = input('컵사이즈를 선택하세요 : ')
        if cup == '': # '' 문자열 빈칸을 뜻함
            self.cup = 0
        else:
            cup = int(cup)
            # 컵 self 에 넣기
            self.cup = cup - 1

        if self.cup == 1: # 점도일 때 // 점보면 + 500원
            self.price += 500

    def set_ice(self):
        # 얼음량 종류 보여주기
        for index, ice in enumerate(Drink._ICES): # 드링크 클래스에 아이시즈에서
            print(f'{index + 1}: {ice}')
        # 선택하기
        ice = input('얼음량을 선택하세요 : ')
        # if ice == '':
        #     self.ice = 2
        # else:
        #     self.ice = int(ice) - 1
        self.ice = 2 if ice == '' else int(ice) - 1 # ice 가 빈칸이면 self.ice 는 2이고 뒤에는 그대로!
        # self.ice 에 설정하기


    def set_sugar(self):
        # 당도 종류 보여주기
        for index, sugar in enumerate(Drink._SUGARS):
            print(f'{index + 1}: {sugar}')
        # 당도 선택하기
        sugar = input('당도를 선택하세요 : ')
        # self.sugar 에 넣기
        self.sugar = 2 if sugar == '' else int(sugar) - 1

    def order(self):
        self.set_cup()
        self.set_ice()
        self.set_sugar()

    def __str__(self): # print 할 떄 문자열 리턴
        return f'이름 : {self.name}\t가격 : {self.price}원' \
               + f'\t컵사이즈 : {Drink._CUPS[self.cup]}\t얼음량: {Drink._ICES[self.ice]}' \
                + f'\t당도 : {Drink._SUGARS[self.sugar]}'

class Coffee(Drink):
    pass

class Bubbletea(Drink):
    _PEARLS = ('타피오카', '코코아', '알로에', '젤리')

    def __init__(self, name, price):
        super().__init__(name, price)  # 부모 초기화 호출
        self.pearl = 0      # '타피오카'

    def set_pearl(self):
        # 펄 종류 보여주기
        for index, pearl in enumerate(Bubbletea._PEARLS):
            print(f'{index + 1}: {pearl}')
        # 펄 선택하기
        pearl = input('펄을 선택하세요 : ')
        # self.pearl 에 넣기
        self.pearl = 0 if pearl == '' else int(pearl) - 1

    def order(self):
        # 부모 클래스의 order() 호출
        super().order()
        # set_pearl 호출
        self.set_pearl()

    def __str__(self):
        # 부모클래스의 __str__()(이름, 가격, 컵사이즈, 얼음량, 당도), 펄
        result = super().__str__()
        return result + f'\t펄종류: {Bubbletea._PEARLS[self.pearl]}'

class Order:

    def __init__(self):
        # self.menu 매장에 있는 음료수 전체
        self.menu = []
        # init_menu()
        self.init_menu() # 꼭 self 해주기!
        # self.order_menu 내가 고른 메뉴들 
        self.order_menu = []

    def init_menu(self):
        유빈이꺼1 = Coffee('하동녹차오레오', 2500)
        유빈이꺼2 = Coffee('타로버블티', 3000)
        유빈이꺼3 = Coffee('크림치즈폼초코버블티', 6500)
        self.menu.append(유빈이꺼1)
        self.menu.append(유빈이꺼2)
        self.menu.append(유빈이꺼3)

    def show_menu(self):
        for index, drink in enumerate(self.menu):
            print(f'{index + 1}: {drink.name}\t{drink.price}원')

    def sum_price(self):
        # self.order_menu 에서 하나씩 꺼내서 Drink의 가격을 합산하고 리턴
        sum_value = 0
        for drink in self.order_menu:
            sum_value += drink.price
        return sum_value

    def order_drink(self):
        # 반복
        while True:
            # 메뉴 보여주기
            self.show_menu()
            # 메뉴 선택하기
            drink = input('메뉴를 선택하세요: ')
            drink = int(drink) - 1
            new_drink = self.menu[drink]
            # 옵션 선택하기
            new_drink.order()
            # self.order_menu 에 추가하기
            self.order_menu.append(new_drink)
            # 더 주문하실 건가요?
            is_add = input('더 주문하시겠습니까?(n: 종료) ')
            if is_add == 'n':
                break
        # 주문 내역 보여주기
        print(self) # str 함수 호출

    def __str__(self):
        # 주문내역 제목 보여주기
        s = '-' * 20 + '주문 내역' + '-' * 20 + '\n'
        # 주문한 음료수들 목록 보여주기
        for drink in self.order_menu:
            s += str(drink) + '\n'
        # 총 합계 가격 보여주기
        s += f'총금액: {self.sum_price()}원'

        return s


# vins = Coffee('카페모카', 2500)
# vins = Bubbletea('하동녹차오레오', 4500)
# vins.order()
# print(vins)
order = Order()
order.order_drink()