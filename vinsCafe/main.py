from vinsCafe.vCafe import VCafe
# from vinsCafe.vCafe import Drink
# from vinsCafe.vCafe import SideMenu


def print_menu():

    print('-------------------\n'
          '<< Vins Cafe >>')
    print('1. 음료수 결제 (+ 사이드 메뉴)')
    print('2. 음료수 종류 추가 ( 사이드 메뉴 x)')
    print('3. 음료수 반납')
    print('4. 종료')
    print('-------------------')
    number = input('>> 메뉴를 선택하세요: ')
    return number


def main():

    cafemenu = VCafe()
    # drinkmenu = Drink()
    # sidemenu = SideMenu()

    while True:
        number = print_menu()

        # 1. 음료수 결제
        if number == '' \
                     '1':
            # 음료수 메뉴 보여주기
            cafemenu.show_drink_menu()
            # 음료수 선택하기
            cafemenu.choice_drink()
            # 음료수 결제하기
            # cafemenu.drink_payment()
            # 사이드 메뉴 추가 여부 물어보기, 추가한다면, 메뉴판 보여주기, 메뉴 선택하기
            cafemenu.add_side_menu()
            # 사이드 메뉴 결제하기
            # sidemenu.side_menu_payment()
            cafemenu.payment()
            # 사이드 메뉴를 추가한다면

            # 사이드 메뉴판 보여주기
            # sidemenu.show_side_menu()
            #
            # # 사이드 메뉴 선택하기
            # sidemenu.choice_side_menu()

            # 사이드 메뉴 추가 안하면

            # 영수증 보여주기 ("~ 음료수 ( ~ 사이드 메뉴) 맞으십니까?")
            cafemenu.all_show_receipt()

            # 결제하기
            # cafemenu.payment()

            # 좌석 고르기
            cafemenu.choice_seat()
            # 음료수, 사이드메뉴 + 보안번호, 좌석 확인
            # cafemenu.all_show_receipt()

        # 2. 음료수 종류 추가
        elif number == '2':
            # 어떤 타이틀 음료수 메뉴 추가할건지 물어보기 ("1. 커피, 2. 라떼, 3. 스무디, 4. 티, 5. 에이드 메뉴 중 어떤 메뉴의 음료수를 추가하시겠습니까?")
            cafemenu.add_drink_menu()

        # 3. 음료수 반납
        elif number == '3':
            # ("몇번자리: 음료수는 : 보안번호는 : ") 맞으면 퇴실처리, 틀리면 반복하거나 종료
            cafemenu.return_drink()

        # 4. 종료
        elif number == '4':
            break

        else:
            print('==================================================')
            print('*** "1, 2, 3, 4" 메뉴 중 다시 입력하세요 ***')


if __name__ == '__main__':
    main()
