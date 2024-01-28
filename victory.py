#Скала Джонсон 1972, Стетхем 1967, Пол Уокер 1973, Клюев 1944, Марк Богатырев 1984
while True:
    dates = ['1972', '1967', '1973', '1944', '1984']
    names = ['Скала Джонсон', 'Стетхем', 'Пол Уокер', 'Борис Клюев', 'Марк Богатырев']
    answers, yep = [], 0

    for i in range(5):
        answers.append(str(input('{} - год рождения?: '.format(names[i]))))
    for i in range(len(dates)):
        if answers[i] == dates[i]:
            yep += 1
    yep_proc = int((yep * 100) / 5)

    print('\nВаши результаты:')
    print('Количество правильных ответов:', yep)
    print('Количество ошибок:', (5 - yep))
    print('Процент правильных ответов:', yep_proc, '%')
    print('Процент неправильных ответов:', (100 - yep_proc), '%')

    rez = str(input('\nХотите перепройти викторину?(Да/Нет): '))
    rez = rez.lower()
    if rez == 'нет':
        print('Викторина завершена!')
        break
