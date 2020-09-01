import math

number_1 = float(input())
number_2 = int(input())

if number_2 > 1:
    print(round(math.log(number_1, number_2), 2))
else:
    print(round(math.log(number_1), 2))