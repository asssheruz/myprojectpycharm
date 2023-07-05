import json

phone_book = {}
path = 'phones.json'

def open_file():
    global phone_book
    try:
        with open(path, 'r', encoding='UTF-8') as file:
            phone_book = json.load(file)
            return True
    except:
            return False


def save_file():
    try:
        with open(path, 'w', encoding='UTF-8') as file:
            json.dump(phone_book, file, ensure_ascii=False)
            return True
    except:
            return False

def check_id():
    if phone_book:
        return max(list(map(int, phone_book))) + 1
    return 1

def add_contact(new: {int: dict[str, str]}):
    contact = {check_id(): new}
    phone_book.update(contact)