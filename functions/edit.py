from functions.verify import name, number


def edit_name(numbers):
    print(*numbers.keys(), sep=', ')
    old_name = name(input('Введите имя человека, которое хотите поменять: '))
    edited_name = name(input('Введите новое имя: '))
    numbers[edited_name] = numbers.pop(old_name)
    return numbers


def edit_number(numbers):
    print(*numbers.keys(), sep=', ')
    old_name = name(input('Введите человека, номер которого вы хотите поменять: '))
    all_numbers = numbers[old_name]
    print(*all_numbers)
    old_number = number(input('Введите номер: '))[0]
    if old_number not in all_numbers:
        return 'Такого номера не существует'
    edited_number = number(input('Введите новый номер: '))[0]
    if edited_number in all_numbers:
        return 'Такой номер уже закреплен за этим контактом'
    index = all_numbers.index(old_number)
    numbers[old_name][index] = edited_number
    return numbers
