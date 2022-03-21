def open_count():
    print("새로운 계정 생성.")


def calculator(balance, money):
    print("현재 남은 금액 {0} 원입니다. ".format(balance + money))
    return balance + money

def withdraw(balance, money):
    if(balance >= money):
        print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0} 원입니다.".format(balance))
        return balance

def withdrawNight(balance, money):
    commission = 100 # 수수료 100원
    return commission,balance - money - commission
    # 튜플 형식으로 반환

balance = 0
balance = calculator(balance, 2000) # 입금시
# balance = withdraw(balance, 500) # 출금시


commission, balance = withdrawNight(balance, 500)
print("{0} 원이 잔액이 남았습니다. {1} 원의 수수료가 부과되었습니다.".format(balance, commission))