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
            print('=====================================================================')
            time = int(input("| 1시간 - 2000원 | 2시간 - 4000원 | 3시간 - 6000원 | 4시간 - 8000원 |\n"
                             "| 5시간 - 10000원 | 6시간 - 12000원 | 7시간 - 14000원 | 8시간 - 16000원 |\n"
                             ">> 1:00(최소) ~ 8:00(최대) 원하시는 시간을 고르세요 ex) 1 : "))
            if 1 <= time <= 8:
                self.sum = pay * time
                break
            else:
                print('--------------------------------\n'
                      '*** 1~8 사이의 숫자만 입력하세요 ***')

    def checkin(self):
        while True:
            print('=====================================================================')
            print('<입실 가능한 좌석>')
            self.show_empty_seat_list()  # 빈자리
            self.checkin_position = input('1~10까지 좌석 중 사용할 좌석을 선택하세요 ex) 1 : ')  # 자리선택
            self.checkin_position = int(self.checkin_position)
            new_checkin = Checkin()  # Checkin 생성
            new_checkin.set_random_number()  # checkin 랜덤넘버 생성
            if 1 <= self.checkin_position <= 10:
                self.seat_list[self.checkin_position - 1].checkin = new_checkin
                self.check_list.append(self.checkin_position)
                break
            else:
                print('-------------------------------------\n'
                      '*** 1~10까지 좌석 중에서 선택해주세요 ***')

    # 주문 내역 보여주기
    def order_details(self):
        # self.random_number = random.randint(10, 20 + 1)
        # random_num = Checkin.set_random_number()
        print('=====================================================================')
        print(f'고객님의 좌석은 {self.checkin_position}번 입니다.\n'
              f'결제할 금액은 "{self.sum}"원 입니다.\n'
              f'고객님의 보안번호는 "{self.seat_list[self.checkin_position - 1].checkin.random_number}" 입니다.\n'
              f'이 번호는 퇴실시에 이용되니 주의해주십시오. * 분실시 퇴실 불가 *')
        # Checkin.set_random_number()

    def payment(self):
        while True:
            print('=====================================================================')

            pay = input('결제 금액을 입력하세요 : ')
            pay = int(pay)
            if pay == self.sum:
                print('결제가 완료되었습니다~ 공부 열심히 하세요~')
                break
            else:
                print('----------------------------------------------\n'
                      '*** 주문 내역에 있는 결재 금액을 다시 입력하세요 ***')

    def show_empty_seat_list(self):
        empty_seat_list = []
        for seat in self.seat_list:
            if seat.checkin == None:
                empty_seat_list.append(seat)
        for seat in empty_seat_list:
            print(seat)


    def checkout(self):
        print('=====================================================================')
        print('<없는 자리 중 선택>')
        self.show_empty_seat_list()
        checkout_position = input('퇴실하실 자리를 선택하세요: ')
        checkout_position = int(checkout_position)
        while True:
            print('=====================================================================')
            rn = input('입실시 받은 보안번호는: ')
            rn = int(rn)
            if self.seat_list[checkout_position - 1].checkin.random_number == rn:
                self.seat_list[checkout_position - 1].checkin = None
                print('퇴실이 성공적으로 완료되었습니다. 안녕히 가십시오~')
                break
            else:
                print('----------------------------------------\n'
                      '*** 번호가 틀리셨습니다 재입력 해주십시오 ***')
            self.show_empty_seat_list()  # 빈자리 보여주자


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
        rn = random.randint(10, 100 + 1)  # 랜덤숫자 뽑기
        self.random_number = rn
