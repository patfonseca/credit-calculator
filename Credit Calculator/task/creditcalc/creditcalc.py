import sys
import math


def factor(i, n):
    return i * math.pow(1 + i, n) / (math.pow(1 + i, n) - 1)


def differentiated(p, n, m, i):
    return (1 + i * (n - m + 1)) * p / n


def calculate_number(p, a, i):
    return math.ceil(math.log(a / (a - i * p), i + 1))


def calculate_interest(n):
    return n / 12 / 100


def months_to_years(months):
    if months < 12:
        years = 0
    else:
        years = months // 12
    rest_months = months - 12 * years
    return [years, rest_months]


args = sys.argv  # we get the list of arguments

if len(args) < 5:
    print('Incorrect parameters')
else:
    arguments = ['', '', '', '']
    arguments[0] = args[1]
    arguments[1] = args[2]
    arguments[2] = args[3]
    arguments[3] = args[4]

    type = ''
    principal = 0
    annuity = 0
    periods = 0
    interest = 0

    for d in arguments:
        if d[0:7] == '--type=':
            type = d[7:]
        elif d[0:12] == '--principal=':
            principal = int(d[12:])
        elif d[0:10] == '--payment=':
            annuity = int(d[10:])
        elif d[0:10] == '--periods=':
            periods = int(d[10:])
        elif d[0:11] == '--interest=':
            interest = float(d[11:])

    if type not in ['diff', 'annuity']:
        print('Incorrect parameters')
    elif type == 'diff' and annuity > 0:
        print('Incorrect parameters')
    elif interest <= 0:
        print('Incorrect parameters')
    elif principal < 0 or annuity < 0 or periods < 0:
        print('Incorrect parameters')

    elif type == 'diff':
        total_payment = 0
        for m in range(1, periods + 1):
            payment = math.ceil(differentiated(principal, periods, m, calculate_interest(interest)))
            total_payment += payment
            print('Month', m, ': payment is', payment)
        print('\nOverpayment =', total_payment - principal)

    elif type == 'annuity' and annuity == 0:
        annuity = math.ceil(principal * factor(calculate_interest(interest), periods))
        print('Your annuity payment =', annuity)
        print('Overpayment =', annuity * periods - principal)

    elif type == 'annuity' and principal == 0:
        principal = math.floor(annuity / factor(calculate_interest(interest), periods))
        print('Your credit principal =', principal)
        print('Overpayment =', annuity * periods - principal)

    elif type == 'annuity' and periods == 0:
        periods = calculate_number(principal, annuity, calculate_interest(interest))
        period_to_year = months_to_years(periods)

        if period_to_year[0] > 0 and period_to_year[1] > 0:
            print('It will take', period_to_year[0], 'years and', period_to_year[1], 'months to repay this credit!')
        elif period_to_year[0] > 0 and period_to_year[1] == 0:
            print('It will take', period_to_year[0], 'years to repay this credit!')
        elif period_to_year[1] > 1:
            print('It will take', period_to_year[1], 'months to repay this credit!')
        else:
            print('It will take', period_to_year[1], 'month to repay this credit!')
        print('Overpayment =', annuity * periods - principal)
