import random


class Cafe:
    def __init__(self):
        self.seat_list = []
        self.checkin_position = 0
        self.sum = 0
        self.random_number = 0
        self.empty_seat_list = []
        self.check_list = []

        for num in range(1, 10 + 1):
            self.seat_list.append(Seat(num))

    def time_choice(self):
        while True:
            pay = 2000
            print('='*60)
            time = int(input("| 1시간 - 2000원 | 2시간 - 4000원 | 3시간 - 6000원 | 4시간 - 8000원 |\n"
                             "| 5시간 - 10000원 | 6시간 - 12000원 | 7시간 - 14000원 | 8시간 - 16000원 |\n"
                             ">> 1:00(최소) ~ 8:00(최대) 원하시는 시간을 고르세요 ex) 1 : "))
            if 1 <= time <= 8:
                self.sum = pay * time
                break
            else:
                print('-'*30)
                print('\n*** 1~8 사이의 숫자만 입력하세요 ***')

    def checkin(self):
        while True:
            print('='*60)
            print('<입실 가능한 좌석>')
            self.show_empty_seat_list()  # 빈자리 보여주기
            print('-'*30)
            self.checkin_position = input('1~10까지 입실 가능한 좌석 중 사용할 좌석을 선택하세요 ex) 1 : ')  # 자리선택하기
            self.checkin_position = int(self.checkin_position)
            new_checkin = Checkin()  # Checkin 생성하기
            new_checkin.set_random_number()  # checkin 랜덤넘버 생성하기
            for empty_seat in self.empty_seat_list:
                if empty_seat == self.checkin_position:
                    if 1 <= self.checkin_position <= 10:
                        self.seat_list[self.checkin_position - 1].checkin = new_checkin
                        self.check_list.append(self.checkin_position)
                        self.empty_seat_list.remove(self.checkin_position)
                        return
                    print('-'*30)
                    print('\n*** 1~10까지 좌석 중에서 선택해주세요 ***')
            print('-'*40)
            print('\n*** 입실 가능한 좌석 중 다시 골라주세요 ***')

    # 주문 내역 보여주기
    def order_details(self):
        print('='*60)
        print(f'고객님의 좌석은 {self.checkin_position}번 입니다.\n'
              f'결제할 금액은 "{self.sum}"원 입니다.\n'
              f'고객님의 보안번호는 "{self.seat_list[self.checkin_position - 1].checkin.random_number}" 입니다.\n'
              f'이 번호는 퇴실시에 이용되니 주의해주십시오. * 분실시 퇴실 불가 *')

    # 결제하기
    def payment(self):
        while True:
            print('='*60)
            pay = input('결제 금액을 입력하세요 : ')
            pay = int(pay)
            if pay == self.sum:
                print('결제가 완료되었습니다~ 공부 열심히 하세요~')
                break
            else:
                print('-'*40)
                print('\n*** 주문 내역에 있는 결제 금액을 다시 입력하세요 ***')

    # 빈자리 보여주기
    def show_empty_seat_list(self):
        if len(self.empty_seat_list) == 0:
            for seat in self.seat_list:  # 전체 자리에서 하나씩 꺼냄
                if seat.checkin is None:  # checkin 정보가 없으면,
                    self.empty_seat_list.append(seat.position)  # 빈자리 리스트에 추가
        print(sorted(self.empty_seat_list))

    # 퇴실하기
    def checkout(self):
        if not self.check_list:
            print('-'*20)
            print('\n*** 퇴실 가능한 좌석이 없습니다. ***')
        else:
            while True:
                print('='*40)
                print('<사용중인 좌석>')
                print(sorted(self.check_list))
                print('--------------------')
                checkout_position = input('>> 퇴실하실 자리를 선택하세요: ')
                checkout_position = int(checkout_position)
                if 1 <= checkout_position <= 10:
                    if checkout_position not in self.empty_seat_list:  # [1,2,3,4,5,6,7,8,9,10]
                        while True:
                            print('='*60)
                            rn = input('입실시 받은 보안번호는: ')
                            rn = int(rn)
                            if self.seat_list[checkout_position - 1].checkin.random_number == rn:
                                self.seat_list[checkout_position - 1].checkin = None
                                self.check_list.remove(checkout_position)
                                self.empty_seat_list.insert(checkout_position - 1, checkout_position)  # insert(인덱스, 넣을 값)
                                print('퇴실이 성공적으로 완료되었습니다. 안녕히 가십시오~')
                                return
                            else:
                                print('-'*40)
                                print('\n*** 번호가 틀리셨습니다 재입력 해주십시오 ***')
                    else:
                        print('-'*40)
                        print('\n')
                        print('--- 퇴실 가능한 좌석이 아닙니다. ---\n'
                              '*** 입실하신 좌석 중 다시 입력하세요 ***')
                        break
                else:
                    print('*** 1~10 사이의 좌석 중 퇴실할 좌석을 입력해주세요 ***')
                    break


class Seat:
    def __init__(self, position):
        self.position = position  # 위치
        self.checkin = None  # 체크인정보 영수증

    def __str__(self):
        return str(self.position)


class Checkin:
    # 랜덤숫자
    def __init__(self):
        self.random_number = -1

    def set_random_number(self):
        rn = random.randint(10, 100)  # 랜덤숫자 뽑기
        self.random_number = rn
