# Организация программ и методы строк

my_string = input('Введите произвольный текст:\n')
print('\nДлина введенного Вами текста –', len(my_string), 'символов')
print('\nПеревожу введённый Вами текст в верхний регистр:')
print(my_string.upper())
print('\nПеревожу введённый Вами текст в нижний регистр:')
print(my_string.lower())
print('\nУдаляю все пробелы из введённого Вами текста:')
print(my_string.replace(' ', ''))
print('\nОпределяю первый символ введённого Вами текста:', my_string[0])
print('Определяю последний символ введённого Вами текста:', my_string[-1])
print('\nБлагодарю за сотрудничество!\nВсего Вам доброго!')