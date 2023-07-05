import text

def menu() -> int:
    print(text.main_menu[0])
    for i in range(1, len(text.main_menu)):
        print(f'\t{i}. {text.main_menu[i]}')
    select = input(text.select_menu)
    if select.isdigit() and 0 < int(select) < int(len(text.main_menu)):
        return int(select)
    print(text.input_error)

def show_contacts(book: dict[int:dict[str,str]]):
    if book:
        max_name = []
        max_phone = []
        max_comment = []
        for contact in book.values():
            print(contact)
            # max_name.append(len(contact.name))
            # max_phone.append(len(contact.phone))
            # max_comment.append(len(contact.comment))
        size_name = max(max_name)
        size_phone = max(max_phone)
        size_comment = max(max_comment)
        print('\n' + '='*(size_name + size_phone + size_comment +7))
        for index, contact in book.items():
            print(f'{index:>3}. {contact.name:<{size_name}} {contact.phone:<{size_phone}} ' 
                  '{contact.comment:<{size_comment}}')
        print('=' * (size_name + size_phone + size_comment + 7) + '\n')
    else:
        print_message(message)


def print_message(message: str):
    print('\n' + '='*len(message))
    print(message)
    print('=' * len(message) + '\n')

def add_contact():
    new = {}
    for key, value in text.new_contact.items():
        new[key] = value
    return new

def search_word() -> str:
    return input(text.search_word)