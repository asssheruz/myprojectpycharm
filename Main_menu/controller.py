import view
import model


def start():
    while True:
        select = view.menu()
        match select:
            case 1:
                pass
            case 2:
                pass
            case 3:
                view.show_contacts(model.phone_book, text.empty_book)
            case 4:
                new = view.add_contact()
                model.add_contact(new)
            case 5:
                pass
            case 6:
                pass
            case 7:
                pass
            case 8:
                pass



