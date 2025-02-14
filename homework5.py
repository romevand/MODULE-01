# Неизменяемые и изменяемые объекты. Кортежи и списки

immutable_var = 'Объект "кортеж" не поддерживает назначение элементов', 1, 2, 3, True
print('Кортеж (tuple) Immutable:')
print(immutable_var)

print('\nОбъект "кортеж" не поддерживает назначение элементов.')
print('Поэтому, к примеру, такая команда')
print('immutable_var[1]= 100')
print('является некорректной.')

mutable_list = ['"Список" является изменяемым объектом', 10, 20, 30, False]
print('\nИсходный список (list) Mutable:')
print(mutable_list)

print('\nВ отличие от "кортежа", "список" является изменяемым объектом.')
print('К примеру, изменим значение пятого и добавим ещё два дополнительных элемента в конец списка.')
mutable_list[4] = True
mutable_list.extend(['Текст', 2024])
print('\nВ результате, получим изменённый список (list) Mutable:')
print(mutable_list)