def record():
    entry = []
    surname = input('Введите фамилию: ')
    entry.append(surname)
    name = input('Введите имя: ')
    entry.append(name)
    phone = input('Введите телефон: ')
    entry.append(phone)
    city = input('Введите город: ')
    entry.append(city)
    description = input('Введите описание контакта: ')
    entry.append(description)
    print('Вами введена запись: ', entry)
    return entry

# num = int(input('Пополнение словаря, нажмите 1\nПоиск контакта, нажмите 2\n Введите цифру : '))
# if num == 1:
#     add.add_directory()
# elif num == 2:
#     num2 = int(input('\nПоиск по фамилии 1\nПоиск по Имени 2\nПоиск по городу 3\n Введите цифру : '))
#     if num2 == 1:
#         lm = input('\nВведите фамилию : ')
#         request.request_number('last_name', lm)
#     elif num2 == 2:
#         nm = input('\nВведите имя : ')
#         request.request_number('name', nm)
#     elif num2 == 3:
#         ct = input('\nВведите город : ')
#         request.request_number('city', ct)