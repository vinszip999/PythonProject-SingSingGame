class Icecream:

    def __init__(self, name): # 생성자, 주로 변수 초기화
        self.name = name
        # 이름 : name
        # 설명 : explanation

    def set_explanation(self, explanation):
        self.explanation = explanation

    def __str__(self): # 객체를 우리가 알아보기 쉽게 문자열로 리턴, 주로 print() 함수에서 호출
        return f'이름: {self.name}'

# 아이스홈런볼 = Icecream('아이스홈런볼')
# 아이스홈런볼.set_explanation('홈런볼이 들어간 초코 아이스크림')
# print(아이스홈런볼)
# print(아이스홈런볼.explanation)
#
# 슈팅스타 = Icecream('슈팅스타')
# 슈팅스타.set_explanation('입안에서 톡톡터지는 체리블렛 아이스크림')
# print(슈팅스타)
# print(슈팅스타.explanation)
#
# 엄마는외계인 = Icecream('엄마는외계인')
# 엄마는외계인.set_explanation('몰티져스가 들어간 초코 아이스크림')
# print(엄마는외계인)
# print(엄마는외계인.explanation)
#
# 아몬드봉봉 = Icecream('아몬드봉봉')
# 아몬드봉봉.set_explanation('아몬드가 들어간 초코아이스크림')
# print(아몬드봉봉)
# print(아몬드봉봉.explanation)

class Order:
    _CATEGORIES = ('싱글레귤러', '더블레귤러', '파인트')
    _PRICES = (3200, 6200, 8200)

    def __init__(self):
        # 종류 : 콘인지 파인트인지...
        self.set_cateries()
        # 메뉴
        self.menu = []
        self.init_menu() # 메뉴 초기화
        # 주문한 메뉴
        self.order_menu = []
    
    def __str__(self):
        pass

    def set_cateries(self):
        for index, category in enumerate(Order._CATEGORIES):
            print(index+1, category)
        category_num = input('종류를 골라주세요: ')
        self.category = int(category_num)

    def init_menu(self):
        self.menu.append(Icecream('슈팅스타'))
        self.menu.append(Icecream('엄마는외계인'))
        self.menu.append(Icecream('아몬드봉봉'))

    def show_menu(self):
        for index, icecream in enumerate(self.menu):
            print(f'{index + 1}. {icecream}')
# 윈도우 +  방향키 : 옆으로 옮기기

    def order(self):
        # 종류를 고른다(싱글레귤러,더블레귤러,파인트)
        # 메뉴 초기화
        # 아이스크림 보여주기(메뉴)
        self.show_menu()
        # 종류에 따라 반복
        for _ in range(self.category): # _ : 안쓴다는 표시
            #  메뉴 선택
            icecream = input('아이스크림을 골라주세요 : ')
            icecream = int(icecream)
            #  주문한 메뉴에 추가
            self.order_menu.append(self.menu[icecream - 1])
        # 종류 출력하기
        print('-'*10 + '주문 내역입니다.' + '-'*10)
        print(Order._CATEGORIES[self.category - 1])
        print(str(Order._PRICES[self.category - 1]) + '원')
        # 주문한 메뉴 츌력하기
        for icecream in self.order_menu:
            print(icecream)

order = Order()
order.order()