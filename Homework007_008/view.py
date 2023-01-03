
def print_data(data):
    if len(data) > 0:
        print("ФАМИЛИЯ".center(15), "ИМЯ".center(15), "ОТЧЕСТВО".center(15),
              "ТЕЛЕФОН".center(15), "АДРЕС".center(20), "ЗАРПЛАТА".center(20))
        print("-" * 90)
        for item in data:
            print(item[0].ljust(15), item[1].ljust(15), item[2].ljust(15),
                  item[3].ljust(15), item[4].ljust(20), item[5].ljust(20))
    else:
        print("В справочнике нет данных!")


def selection_search_menu():
    print("\nИскать по:\n\
        1 - Фамилия;\n\
        2 - Имя;\n\
        3 - Отчество;\n\
        4 - Телефон;\n\
        5 - Адрес;\n\
        6 - Нижней планке ЗП;\n\
        0 - выйти из программы")
    choice = input("Выберите параметр, по которому нужно произвести поиск: ")
    return choice


def search_data(data):
    choice = selection_search_menu()
    search = input("Введите данные для поиска: ")
    match choice:
        case '1':
            if len(data) > 0:
                for item in data:
                    if search in item:
                        print(f'search {search} item-{item}')
                        print(item, sep=',')
                        # return item
        case '2':
            if len(data) > 0:
                for item in data:
                    if search in item[1]:
                        print(item, sep=',')
                        # return item
        case '3':
            if len(data) > 0:
                for item in data:
                    if search in item[2]:
                        print(item, sep=',')
                        # return item
        case '4':
            if len(data) > 0:
                for item in data:
                    if search in item[3]:
                        print(item, sep=',')
                        # return item
        case '5':
            if len(data) > 0:
                for item in data:
                    if search in item[4]:
                        print(item, sep=',')
                        # return item
        case '6':
            if len(data) > 0:
                for item in data:
                    if int(search) < int(item[5]):
                        print(item, sep=',')
        case '0':
            exit(0)
        case _:
            print("Такой команды нет!")
