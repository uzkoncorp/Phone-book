from functions.verify import name
def person(numbers):
    add_contact = name(input('Введите имя: '))
    add_number = input('Введите номер: ').split(",")
    numbers[add_contact] = add_number
    return numbers