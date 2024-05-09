import tabulate
def ask_data():
    s_name = input("Введите фамилию: ")
    f_name = input("Введите имя: ")
    m_name = input("Введите отчество: ")
    phone = input("Введите номер телефона: ")
    contact = {'second_name': s_name,
    'first_name': f_name,
    'middle_name': m_name,
    'phone_number': phone}
    return contact

def add_new_contact():
    contact = ask_data()
    with open('phonebook.txt', 'a', encoding='utf-8') as file:
        for value in contact.values():
            file.write(value)
            file.write('; ')
        file.write('\n')
        print('Контакт добавлен')

def open_phonebook():
    title = ['id', 'Фамилия', 'Имя', 'Отчество', 'Телефон']
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        contact_list = []
        for counter, line in enumerate(file):
            contact_list.append([str(counter)] + line.split(';'))
        print(tabulate.tabulate(contact_list, headers=title))

def find_contact():
    flag = True
    title = ["id", "Фамилия", "Имя", "Отчество", "Телефон"]
    s_name = input("Введите фамилию: ")
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        contact_list = []
        for counter, line in enumerate(file):
            line = line.split(';')
            if s_name in line[0]:
                contact_list.append([str(counter)] + line)
    if len(contact_list) == 0:
        print('\nКонтакта не существеут')
        flag = False
        return flag             
    else:
        print(tabulate.tabulate(contact_list, headers=title))
        flag = True
        return flag  

# Выполнение задания к уроку 8.
# Дополнить справочник возможностью копирования данных из одного файла в другой
# Пользователь вводит номер строки, которую необходимо перенести из одного файла в другой:

def copy_contact():
    '''Функция копирует один контакт в отдельный файл: 
    1. По запросу выводит список контактов с id по введенной фамилии. 
    2. Запрашивает id нужного контакта. 
    3. Копирует контакт в отдельный файл с названием: "Фамилия_id"'''
    list_output = int(input('\nДля экспорта необходимо ввести id конакта\nВыберете действие: \n\t1 Узнать id контакта по фамилии\n\t2 Перейти к вводу id\n\t>'))
    if list_output == 1:
        flag = find_contact()
    if list_output == 2 or flag == True: 
        with open('phonebook.txt', 'r', encoding='utf-8') as data:
            id_copy_contact = int(input("Введите id контакта для копирования: "))
            count = False
            for id, line in enumerate(data):
                line = line.split()
                if id_copy_contact == id: 
                    count = True
                    with open((f'{line[0]}_id{id}.txt'), 'w', encoding='utf-8') as data:
                        for j in line:
                            data.write(j)
                            data.write(' ')
                        print('Копирование выполнено')
            if count == False:
                print('\nВведен не верный id, копрование не выполнено')

    
def main():
    isStop = 10
    while isStop != 0:
        print()
        print(f"Выберете что хотите сделать:\n1 Найти контакт\n2 Добавить новый контакт\n3 Открыть всю книгу\n4 Скопировать контакт в отдельный файл\n0 выход")
        isStop = int(input(">"))
        if isStop in [0, 1, 2, 3, 4]:
            if isStop == 1:
                find_contact()
            elif isStop == 2:
                add_new_contact()
            elif isStop == 3:
                open_phonebook()
            elif isStop == 4:
                copy_contact()
            print()
            input("Нажмите Enter чтобы продолжить")
        else:
            print("Введен некорректный запрос, введите команду от 0 до 4")
            
main()