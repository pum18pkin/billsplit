balance = float(input("input your balance:" ))


def realBalance ():
    if balance >= 0:
        rate = 0.10
        tip_rate = balance * rate
        print(f"your tip is {tip_rate}")
        return balance + tip_rate
for i in range (6):
    eachPerson=realBalance()/5
    print(f"each person has {eachPerson} to pay")
    break
    