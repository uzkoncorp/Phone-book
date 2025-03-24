from verify import *



numbers = {
    "Алексей": ["89098467577", "7974758"],
    "Александр": ["78986362"],
    "Арина": ["7892322737"]
}
#add
while True:
    key = input()
    if key == "add":
        add_contact = verify_name(input('Введите имя: '))
        add_number = input('Введите номер: ').split(",")
        numbers[add_contact] = add_number


    if key == 'delete':
        deleted = verify_name(input('Введите имя: '))
        del numbers[deleted]
        #print(numbers.pop(deleted, 'Такого контака нет'))

    if key == 'get one':
        print(numbers.get(verify_name((input('Введите имя: ')))))


    if key == 'get all':
        for name, number in numbers.items():
            print(name,':',number,end = ', ')

    if key == 'delete all':
        numbers.clear()
    # print(numbers)

    if key == 'f': #edit_name
        print(numbers.keys())
        name = verify_name(input('Введите имя человека, которое хотите поменять: '))
        edited_name = verify_name(input('Введите новое имя: '))
        numbers[edited_name] = numbers.pop(name)
        print(numbers)


    if key == 'o': #'edit_number':
        print(numbers.keys())
        name = verify_name(input('Введите человека, номер которого вы хотите поменять: '))
        all_numbers = numbers[name]
        print(all_numbers)
        number = verify_number(input('Введите номер: '))[0]
        edited_number = verify_number(input('Введите новый номер: '))[0]
        if edited_number not in all_numbers and number in all_numbers:
            print('yes')
    print(numbers)





    if key == 'end':
        break
print(numbers)
