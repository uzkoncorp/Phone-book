def number(numbers):
    correct_number = []
    numbers = numbers.replace(" ", "")
    numbers = numbers.replace("+7", "8")
    for i in numbers.split(','):
        if len(i) == 11:
            correct_number.append('8' + i[1:])
    return correct_number


def name(name_of_person: str) -> str:
    name_of_person = name_of_person[0].upper() + name_of_person[1:len(name_of_person)].lower()
    return name_of_person