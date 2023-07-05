import text

def menu() -> int:
    print(text.main_menu[0])
    for i in range(1, len(text.main_menu)):
        print(f'\t{i}. {text.main_menu[i]}')
    select = imput(text.select_menu)
    if select.isdigit(and 0 < int(select) < int(len(text.main_menu)):
        return int(select)
    print(text.input_error)

def show_contacts(book: dict[int: dict[str,str]]):
    if book:
        for contact in book.items():
            print(f'{index:>3}. {contact.get("name"):<20} {contact.get("phone"):<20} {contact.get("comment"):<20}')
    else:
        print(message)


def add_contact():
    new = {}
    for key, value in text.new_contact.items():
        new[key] = value
    return new