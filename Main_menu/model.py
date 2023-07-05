import json
class Contact:
    def __init__(self, name: str, phone: str, comment: str):
        self.name = name
        self.phone = phone
        self.comment = comment

        def __repr__(self):
            return f'{self.name} {self.phone} {self.comment}'
        def update(self, new):
            self.name = new.name if new.name else self.name
            self.phone = new.phone if new.phone else self.phone
            self.comment = new.comment if new.comment else self.comment

        def to_dict(self):
            return {'name': self.name, 'phone': self.phone, 'comment': self.comment}

class PhoneBook:

    def __init__(self, path: str = 'phones.json'):
        self.contact = {int: Contact}
        self.path = path

    def get(self, index: int | None = None):
        if index:
            return self.contact.get(index)
        return self.contact
    def open_file(self):

        try:
            with open(self.path, 'r', encoding='UTF-8') as file:
                self.contact = json.load(file)
                return True
        except:
                return False


    def save_file(slef):
        try:
            with open(self.path, 'w', encoding='UTF-8') as file:
                json.dump(self.phone_book, file, ensure_ascii=False)
                return True
        except:
                return False


    def search(word: str) -> dict[int: dict[str, str]]:
        result = {}
        for index, contact in self.phone_book.items():
            if word.lower() in ' '.join(contact.values()).lower():
                result[index] = contact
        return result


    def check_id(self):
        if self.phone_book:
            return max(list(map(int, self.phone_book))) + 1
        return 1

    def add_contact(self, new: {int: dict[str, str]}):
        contact = {self.check_id(): new}
        self.phone_book.update(contact)