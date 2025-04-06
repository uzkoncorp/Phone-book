from functions.verify import name


def one(numbers):
    print(*numbers.keys(), sep=', ')
    deleted = name(input('Введите имя: '))
    numbers = numbers.pop(deleted, 'Такого контака нет')
    return numbers


def all(numbers):
    return numbers.clear()
