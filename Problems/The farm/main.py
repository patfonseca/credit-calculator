animals = {'sheep': 6769,
           'cow': 3848,
           'pig': 1296,
           'goat': 678,
           'chicken': 23}

money = int(input())
buy = 'None'

if money >= animals['sheep']:
    buy = 'sheep'
elif money >= animals['cow']:
    buy = 'cow'
elif money >= animals['pig']:
    buy = 'pig'
elif money >= animals['goat']:
    buy = 'goat'
elif money >= animals['chicken']:
    buy = 'chicken'
else:
    print(buy)

if buy != 'None':
    if money - animals[buy] < animals[buy]:
        print(1, buy)
    elif buy == 'sheep':
        print(money // animals[buy], buy)
    else:
        print(money // animals[buy], buy + 's')