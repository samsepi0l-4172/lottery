import random

# 로또 번호 추첨 함수
def lotto():
    numbers = list(range(1, 46))
    random.shuffle(numbers)
    return sorted(numbers[:6])

# 프로그램 시작
print("로또 추첨을 시작합니다!")

while True:
    # 사용자 입력 받기
    input("Enter를 눌러 로또 번호를 추첨하세요...")

    # 추첨 결과 출력
    lucky_numbers = lotto()
    print("당신의 행운의 번호는 다음과 같습니다:", lucky_numbers)

    # 계속할지 묻기
    again = input("다시 추첨하시겠습니까? (Y/N) ")
    if again.upper() != "Y":
        break

print("로또 추첨을 종료합니다!")
