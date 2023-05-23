import onlinerequests

LIST = onlinerequests.response.json()
CURRENCIES = LIST.get('data')

print('Добро пожаловать в конвертер!')
print('''
Наша программа поможет вам конвертировать валюту
1. Введение имеющейся валюты
2. Количество валюты
3. Выбор валюты для конвертации
''')

while True:
    print('Вам предложены следующие валюты:')
    key_counter = 1
    for key in CURRENCIES:
        print(f'{key_counter}. {key}')
        key_counter += 1

    while True:
        user_currency = input('Введите имеющуюся валюту: ')
        if user_currency in CURRENCIES.keys():
            print('Отлично! Идем дальше...')
            break
        else:
            print('Неверные данные...')

    while True:
        current_amount = input('Введите имеющуюся сумму: ')
        try:
            x = float(current_amount)
            print('Отлично! Продолжаем...')
            break
        except:
            print("Неверные данные...")

    sum_amount = float(current_amount)

    while True:
        conversion_currency = input('Введите необходимую валюту: ')
        if conversion_currency in CURRENCIES.keys():
            break
        else:
            print('Неверные данные...')

    converted_amount = sum_amount / CURRENCIES.get(user_currency) * CURRENCIES.get(conversion_currency)
    print(f'Вы получите: {round(converted_amount, 2)} {conversion_currency}')

    finish = input('Хотите повторить рассчеты? Выберите: Y/N')
    if finish == 'N':
        break
    while finish != 'Y':
        print('Неверные данные...')
        finish = input('Хотите повторить рассчеты? Выберите: Y/N')




