import text

def menu():
    print(text.main_menu[0])
    for i, in range(1, len(text.main_menu)):
        print(f'\t{i}. {text.main_menu[i]}')


menu()