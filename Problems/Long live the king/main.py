column = int(input())
row = int(input())

limits = [1, 8]

if column in limits and row in limits:
    print('3')
elif column in limits and row not in limits:
    print('5')
elif column not in limits and row in limits:
    print('5')
else:
    print('8')
