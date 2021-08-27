class ThailandPackage:
    def detail(self):
        print("[태국 패키지 3박 5일] 방콕, 파타야 여행 (야시장 투어) 50만원")


if __name__ == "__main__":  # __name__이 만약 "__main__" 이면,
    print("Thailand 모듈을 직접 실행")
    # thailand.py 에서 코드를 수정하고 직접 실행했을 때 이 구문이 실행된다.

    print("이 문장은 모듈을 직접 실행할 때만 실행이 됩니다.")
    trip_to = ThailandPackage()
    trip_to.detail()
else:
    print("Thailand 외부에서 모듈 호출")
    # practice.py 에서 thailand.py 를 가져다 쓸 때에는 이 구문이 실행된다.

# 정리 : practice.py 에서 thailand.py 를 가져다 쓸 때에는 else 구문의 문장 내용이 실행되고,
# thailand.py 에서 직접 이 내용을 실행할 때는 if 구문의 문장 내용이 실행된다.




