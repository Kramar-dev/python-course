keep_going = True

while keep_going:
    print('Jakie działanie chcesz wykonać?\n(D)dodawanie\n(O)dejmowanie\n(M)nożenie\nd(Z)ielenie\n(W)yjdz')
    action = input()

    if action == 'W':
        keep_going = False
        continue

    print('Podaj pierwszą liczbę')
    try:
        number_1 = float(input())
    except:
        print('Nie podano liczby')
        continue

    print('Podaj drugą liczbę')
    try:
        number_2 = float(input())
    except:
        print('Nie podano liczby')
        continue

    result = None

    if action == 'D':
        result = number_1 + number_2
    elif action == 'O':
        result = number_1 - number_2
    elif action == 'M':
        result = number_1 * number_2
    elif action == 'Z':
        if number_2 == 0:
            print('Nie można dzielić przez zero')
            continue
        result = number_1 / number_2
    else:
        print('Podano nieobsługiwane działanie')
        continue

    if result is not None:
        print(result)
else:
    print('Program zakończył działanie')

