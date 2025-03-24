def verify_number(numbers):
    correct_number = []
    numbers = numbers.replace(" ", "")
    numbers = numbers.replace("+7", "8")
    for i in numbers.split(','):
        if len(i) == 11:
            correct_number.append('8' + i[1:])
    return correct_number


def verify_name(name: str) -> str:
    name = name[0].upper() + name[1:len(name)].lower()
    return name