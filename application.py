from functions import add, delete, get



numbers = {
    "Алексей": ["89098467577", "7974758"],
    "Александр": ["78986362"],
    "Арина": ["7892322737"]
}
#add
while True:
    key = input('Введите ключ функции: ')
    if key == "add":
        numbers = add.person(numbers)

    if key == 'delete':
        numbers = delete.person(numbers)

    if key == 'get one':
        get.one_number(numbers)


    if key == 'get all':
        get.all_numbers(numbers)
#
#     if key == 'delete all':
#         numbers.clear()
#     # print(numbers)
#
#     if key == 'f': #edit_name
#         print(numbers.keys())
#         name = verify.name(input('Введите имя человека, которое хотите поменять: '))
#         edited_name = verify.name(input('Введите новое имя: '))
#         numbers[edited_name] = numbers.pop(name)
#         print(numbers)
#
#
#     if key == 'o': #'edit_number':
#         print(numbers.keys())
#         name = verify.name(input('Введите человека, номер которого вы хотите поменять: '))
#         all_numbers = numbers[name]
#         print(all_numbers)
#         number = verify.number(input('Введите номер: '))[0]
#         edited_number = verify.number(input('Введите новый номер: '))[0]
#         if edited_number not in all_numbers and number in all_numbers:
#             print('yes')
#     print(numbers)
#
#
#
#
#
#     if key == 'end':
#         break
# print(numbers)
