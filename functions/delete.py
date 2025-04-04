from functions.verify import name
def person(numbers):
    print(numbers.keys())
    deleted = name(input('Введите имя: '))
    numbers = numbers.pop(deleted, 'Такого контака нет')
    return numbers