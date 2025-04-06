from functions.verify import name


def one_number(numbers):
    print(*numbers.keys(), sep=', ')
    print(numbers[name(input('Введите имя: '))])


def all_numbers(numbers):
    for key, value in numbers.items():
        print(key, ':', value, end=', ')
