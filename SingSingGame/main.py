from SingSingGame.game import Game

def print_menu():
    print('-' * 20)
    print('<<SingSing Game>>')
    print('1. 씽씽게임하기')
    print('2. 노래추가하기')
    print('3. 종료')
    print('-' * 20)
    num = input('>> 메뉴를 선택하세요: ')
    return num


def main():
    pass
    # studymenu = Cafe()
    #
    # while True:
    #     num = print_menu()
    #     # 입실하기
    #     if num == '' \
    #               '1':
    #         # 시간 선택하기
    #         studymenu.time_choice()
    #         # 좌석 선택하기
    #         studymenu.checkin()
    #         # 주문 내역 보여주기 + 랜덤 숫자 배정
    #         studymenu.order_details()
    #         # 결제하기
    #         studymenu.payment()
    #
    #     # 퇴실하기
    #     elif num == '2':
    #         studymenu.checkout()
    #
    #     # 종료하기
    #     elif num == '3':
    #         break
    #
    #     else:
    #         print('=' * 50)
    #         print('*** "1.입실", "2.퇴실", "3.종료" 중 다시 입력하세요 ***')


if __name__ == '__main__':
    main()

