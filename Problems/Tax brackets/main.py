income = int(input())

if income < 15528:
    tax = 0
elif income < 42708:
    tax = 15
elif income < 132407:
    tax = 25
else:
    tax = 28

calculated_tax = round(income * tax / 100)

print(f'The tax for {income} is {tax}%. That is {calculated_tax} dollars!')
