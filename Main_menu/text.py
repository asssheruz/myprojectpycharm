main_menu = ['Главное меню',
            'Открыть файл',
            'Сохранить файл',
            'Показать все контакты',
            'Добавить контакт',
            'Найти контакт',
            'Изменить контакт',
            'Удалить контакт',
            'Выход']

select_menu = 'Выберете пункт меню: '


input_error = f'Ошибка ввода. Введите число от 1 до {len(main_menu)-1}: '

new_contact = {'name': 'Ввудите имя контакта: ',
                'phone': 'Введите телефон: ',
                'comment': 'Введите комментарий'}

empty_book = 'Телефонная книга пуста или не открыта'

load_successful = 'Телефонная книга успешно загружена'
save_successful = 'Телефонная книга успешно сохранена'
error_load = 'Ошибка загрузки телефонной книги'
error_save = 'Ошибка сохранения телефонной книги'

def add_successful(name: str) -> str:
    return f'Контакт {name} успешно добавлен в книгу!'
