#6 июня 1799
while True:
    year = str(input('Введите год рождения Пушкина: '))

    if year == '1799':
        print('Верно')
        while True:
            days = str(input('Введите день рождения: '))
            if days == '6':
                print('Верно')
                break
            else:
                print('Неверно')
        break
    else:
        print('Неверно')
