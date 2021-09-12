import random
import string
import datetime


class VCafe:

    def __init__(self):
        self.fixed_seat = []
        self.security = 0
        self.show_menu = []
        self.money = 0
        self.money_sum = []

        self.drink_sum = 0
        self.drink_menu = []
        self.coffee = ["아메리카노","카라멜마끼아또"]
        self.latte = ["고구마라떼", "초코라떼", "녹차라떼", "카페라떼", "바닐라라떼"]
        self.smoothie = ["망고스무디", "블루베리스무디", "딸기스무디", "수박스무디"]
        self.tea = ["복숭아아이스티", "레몬아이스티", "블루레몬아이스티", "밀크티"]
        self.ade = ["블루레몬에이드", "자몽에이드", "오렌지에이드", "라임에이드"]

        self.side_sum = 0  # 사이드 메뉴 가격 계산하는 변수
        self.side_menu = []
        self.cake = ["티라미슈", "초코케잌", "치즈케잌", "녹차케잌"]
        self.sandwich = ["참치샌드위치", "모닝샌드위치", "야채샌드위치"]


    # 음료수 메뉴 보여주기
    def show_drink_menu(self):
        print('--------------------<음료수>--------------------\n'
              '1. 커피 (3000)\n'
              f'{self.coffee}\n'
              '2. 라떼(3500)\n'
              f'{self.latte}\n'
              '3. 스무디(3000)\n'
              f'{self.smoothie}\n'
              '4. 티(2500)\n'
              f'{self.tea}\n'
              '5. 에이드(3000)\n'
              f'{self.ade}')
        print('='*50)

    # 음료수 선택하기
    def choice_drink(self):
        while True:
            choice_menu = input('"1. 커피 2. 라떼 3. 스무디 4. 티 5. 에이드" 중 마실 음료수 종류를 고르세요:')

            self.drink_sum = 0
            if choice_menu == '1':
                self.drink_sum += 3000
                print('=' * 50)
                print(f'1. 커피 (3000)\n'
                      f'{self.coffee}')
                print('=' * 50)

                while True:
                    choice_coffee = input(f'>> 원하는 음료수를 선택하세요: ')

                    for co in self.coffee:
                        if co == choice_coffee:
                            self.drink_menu.append(choice_coffee)
                            print(self.drink_menu)
                            break
                    if choice_coffee == 'esc':
                            break
                    elif len(self.drink_menu) == 1:
                        break
                    else:
                        print('-' * 30)
                        print(f' *** "{self.coffee}" 중 다시 고르세요 ***\n'
                            ' << 나가려면 "esc"를 치세요 >>')
                        print('-'*30)


            elif choice_menu == '2':
                self.drink_sum += 3500
                print('=' * 50)
                print('2. 라떼(3500)\n'
                      f'{self.latte}')
                print('=' * 50)

                while True:
                    choice_latte = input(f'>> 원하는 음료수를 선택하세요: ')
                    for la in self.latte:
                        if la == choice_latte:
                            self.drink_menu.append(choice_latte)
                            print(self.drink_menu)
                            break
                    if choice_latte == 'esc':
                        break
                    elif len(self.drink_menu) == 1:
                        break
                    else:
                        print('-' * 30)
                        print(f' *** "{self.latte}" 중 다시 고르세요 ***\n'
                              ' << 나가려면 "esc"를 치세요 >>')
                        print('-' * 30)


            elif choice_menu == '3':
                self.drink_sum += 3000
                print('=' * 50)
                print('3. 스무디(3000)\n'
                      f'{self.smoothie}')
                print('=' * 50)

                while True:
                    choice_smoothie = input(f'>> 원하는 음료수를 선택하세요: ')
                    for smoo in self.smoothie:
                        if smoo == choice_smoothie:
                            self.drink_menu.append(choice_smoothie)
                            print(self.drink_menu)
                            break
                    if choice_smoothie == 'esc':
                        break
                    elif len(self.drink_menu) == 1:
                        break
                    else:
                        print('-' * 30)
                        print(f' *** "{self.coffee}" 중 다시 고르세요 ***\n'
                              ' << 나가려면 "esc"를 치세요 >>')
                        print('-' * 30)


            elif choice_menu == '4':
                self.drink_sum += 2500
                print('=' * 50)
                print('4. 티(2500)\n'
                      f'{self.tea}')
                print('=' * 50)

                while True:
                    choice_tea = input(f'>> 원하는 음료수를 선택하세요: ')
                    for te in self.tea:
                        if te == choice_tea:
                            self.drink_menu.append(choice_tea)
                            print(self.drink_menu)
                            break
                    if choice_tea == 'esc':
                        break
                    elif len(self.drink_menu) == 1:
                        break
                    else:
                        print('-' * 30)
                        print(f' *** "{self.tea}" 중 다시 고르세요 ***\n'
                              ' << 나가려면 "esc"를 치세요 >>')
                        print('-' * 30)


            elif choice_menu == '5':
                self.drink_sum += 3000
                print('=' * 50)
                print('5. 에이드(3000)\n'
                      f'{self.ade}')
                print('=' * 50)
                while True:
                    choice_ade = input(f'>> 원하는 음료수를 선택하세요: ')
                    for ad in self.ade:
                        if ad == choice_ade:
                            self.drink_menu.append(choice_ade)
                            print(self.drink_menu)
                            break
                    if choice_ade == 'esc':
                        break
                    elif len(self.drink_menu) == 1:
                        break
                    else:
                        print('-' * 30)
                        print(f' *** "{self.ade}" 중 다시 고르세요 ***\n'
                              ' << 나가려면 "esc"를 치세요 >>\n')
                        print('-' * 30)

            elif choice_menu == 'esc':
                print('--- 음료수 결제를 종료합니다. ---')
                break

            else:
                print('-' * 30)
                print(' *** "1. 커피 2. 라떼 3. 스무디 4. 티 5. 에이드" 중 마실 음료수 종류를 다시 고르세요 *** \n'
                      ' << 나가려면 "esc"를 치세요 >> ')
                print('-' * 30, '\n')

            break

    # 사이드 메뉴 추가 여부 물어보기
    def add_side_menu(self):
        while True:
            add_sidemenu = input('\n사이드 메뉴도 드시겠습니까? yes or no:')
            if add_sidemenu == 'yes':
            # 사이드 메뉴를 추가한다면
            # 사이드 메뉴판 보여주기
            # def show_side_menu(self):
                print('------------<사이드 메뉴>---------------\n'
                    '1. 케잌(5000)\n'
                      f'{self.cake}\n'
                    '2. 샌드위치(3000)\n'
                      f'{self.sandwich}')
                print('=' * 50)

                # 사이드 메뉴 선택하기
                while True:
                    choice_sidemenu = input('"1. 케잌 2. 샌드위치" 중 드실 메뉴를 고르세요:')

                    self.side_sum = 0
                    if choice_sidemenu == '1':
                        self.side_sum += 5000
                        print('=' * 50)
                        print(f'1. 케잌 (5000)\n'
                              f'{self.cake}')
                        print('=' * 50)

                        while True:
                            choice_cake = input(f'>> 원하는 케잌를 선택하세요:')
                            for ca in self.cake:
                                if ca == choice_cake:
                                    self.side_menu.append(choice_cake)
                                    print(self.side_menu)
                                    break
                            if choice_cake == 'esc':
                                break
                            elif len(self.side_menu) == 1:
                                break
                            else:
                                print('-' * 30)
                                print(f' *** "{self.cake}" 중 다시 고르세요 ***\n'
                                      ' << 나가려면 "esc"를 치세요 >>')
                                print('-' * 30)

                    elif choice_sidemenu == '2':
                        self.side_sum += 3000
                        print('=' * 50)
                        print(f'2. 샌드위치 (3000)\n'
                              f'{self.sandwich}')
                        print('=' * 50)

                        while True:
                            choice_sandwich = input(f'>> 원하는 샌드위치를 선택하세요:')
                            for sand in self.sandwich:
                                if sand == choice_sandwich:
                                    self.side_menu.append(choice_sandwich)
                                    print(self.side_menu)
                                    break
                            if choice_sandwich == 'esc':
                                break
                            elif len(self.side_menu) == 1:
                                break
                            else:
                                print('-' * 30)
                                print(f' *** "{self.sandwich}" 중 다시 고르세요 ***\n'
                                      ' << 나가려면 "esc"를 치세요 >>')
                                print('-' * 30)

                    elif choice_sidemenu == 'esc':
                        break
                    else:
                        print('-' * 30)
                        print(' *** "1. 케잌 2. 샌드위치" 중 마실 음료수 종류를 다시 고르세요 *** \n'
                              ' << 나가려면 "esc"를 치세요 >> ')
                        print('-' * 30)
                    break

            elif add_sidemenu == 'no':
                break

            else:
                print('-' * 30)
                print(' *** "yes, no" 중 다시 고르세요 *** \n'
                      ' << 나가려면 "esc"를 치세요 >> ')
                print('-' * 30)
            break

    #결제하기
    def payment(self):
        self.money_sum = 0
        self.show_menu = self.drink_menu + self.side_menu
        self.money_sum = self.drink_sum + self.side_sum
        print(f'\n주문하신 메뉴는 {self.show_menu}입니다.')
        print(f'총 결제 금액은 {self.money_sum}원 입니다.')
        while True:
            self.money = int(input('>> 금액을 입력하세요: '))
            if self.money == self.money_sum:
                print('결제가 완료되었습니다.')
                break
            elif self.money > self.money_sum:
                pay = self.money - self.money_sum
                print(f'거스름돈 {pay}원 입니다. 결제가 완료되었습니다.')
                break
            else:
                print('*** 올바른 금액을 입력해주세요 ***')
            # self.show_menu = 0
            # self.money_sum = 0
            # self.drink_menu = 0
            # self.side_menu = 0


    # 좌석 고르기
    def choice_seat(self):
        # fixed_seat = []
        print('\n<사용중인 좌석>')  # 사용 가능 좌석
        print(self.fixed_seat)
        while True:
            seat = int(input('1~10 좌석 중 앉을 좌석을 고르세요 ex) 1 :'))
            if seat != self.fixed_seat:
                self.fixed_seat.append(seat)
                print(self.fixed_seat)
                break
            elif seat == 'esc':
                break
            else:  # seat == fixed_seat
                print('*** 이미 사용중인 좌석입니다. 미사용 좌석으로 다시 골라주세요 *** ')

    # 보안번호
    def check_drink(self):
        number_of_strings = 1
        length_of_string = 5
        self.security = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(length_of_string))
        #for x in range(number_of_strings):
        print(f'보안번호: {self.security}')

    def return_drink(self):
        while True:
            print(f'사용중인 좌석: {self.fixed_seat}')
            seat = int(input('사용한 좌석 번호 입력: '))
            ate_drink = input('드셨던 음료수 입력: ')
            ate_side = input('드셨던 사이드음식 입력: ')
            self.fixed_seat.remove(seat)
            self.drink_menu.remove(ate_drink)
            self.side_menu.remove(ate_side)
            print('반납이 완료되었습니다.')
            print(self.fixed_seat)
            print(self.drink_menu)
            print(self.side_menu)
            if seat == 'esc':
                break
            break

    # 영수증(음료수/ 좌석/보안번호 확인)
    def all_show_receipt(self):
        now = datetime.datetime.now()
        day = now.strftime('%Y-%m-%d %H:%M:%S')
        print('\n\t\t[영수증]')
        print('-' * 30)
        print('[매장명]\tVins카페')
        print(f'[거래일시]\t{day}')
        print('-' * 30)
        print('\t상품명\t\t금액')
        print('-'*30)
        print(f'{self.drink_menu}\t  {self.drink_sum}')
        if len(self.side_menu) != 0:
            print(f'{self.side_menu}\t   {self.side_sum}')
        print('-' * 30)
        print(f'합계 금액\t\t{self.money_sum}')
        print('-' * 30)
        print(f'받을 금액\t\t{self.money_sum}')
        print(f'받은 금액\t\t{self.money}')
        print('-' * 30)
        print(f'사용 좌석\t\t{self.fixed_seat}')
        print(f'[보안 번호]\t\t{self.security}')
        print('-' * 30,'\n')
        self.drink_menu.clear()
        self.side_menu.clear()
        #self.money_sum.clear()

    def add_drink_Menu(self):
        pass



# sidemenu = Drink()
# sidemenu.choice_drink()