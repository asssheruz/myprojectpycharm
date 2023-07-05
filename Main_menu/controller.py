import view
import model


def start():
    while True:
        select = view.menu()
        match select:
            case 1:
                if model.open_file()
                    view.print_message(text.load_successful)
                else
                    view.print_message(text.error_load)
            case 2:
                if model.save_file()
                    view.print_message(text.save_successful)
                else
                    view.print_message(text.error_save)
            case 3:
                view.show_contacts(model.phone_book, text.empty_book)
            case 4:
                new = view.add_contact()
                model.add_contact(new)
                view.print_message(text.add_successful(new.get('name')))
            case 5:
                pass
            case 6:
                pass
            case 7:
                pass
            case 8:
                pass



