from functions import add, delete, get, edit

numbers = {
    "Алексей": ["89098467577", "89747587654"],
    "Александр": ["89881716274"],
    "Арина": ["88923227378"]
}

help_key = ['add', 'delete_one', 'delete_all', 'get_one', 'get_all', 'edit_name', 'edit_number', 'end']
while True:
    key = input('Введите "help",чтобы узнать список команд.\nВведите ключ функции: ')
    if key == "add":
        numbers = add.person(numbers)

    if key == 'help':
        print(*help_key, sep=', ', end='\n\n')

    if key == 'delete':
        numbers = delete.one(numbers)

    if key == 'get one':
        get.one_number(numbers)

    if key == 'get all':
        get.all_numbers(numbers)

    if key == 'delete all':
        numbers = delete.all(numbers)

    if key == 'edit_name':
        numbers = edit.edit_name(numbers)

    if key == 'edit_number':
        numbers = edit.edit_number(numbers)

    if key == 'end':
        break
