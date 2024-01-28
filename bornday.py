# 6 июня 1799
years = str(input('Введите год рождения Пушкина: '))
days = int(input('День рождения: ')) if years == '1799' else print('Неверный год рождения')
if days != 'NoneType':
    print('Верно') if days == 6 else print('Неверный день рождения')
