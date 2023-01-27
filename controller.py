import model
import view


def input_processing(num: int):
    match num:
        case 1:
            if not model.count:
                model.read_db('data_base.txt', model.db_list)
                view.db_success(model.db_list)
            else:
                view.db_success(model.db_list)
        case 2:
            view.show_db(model.db_list)
        case 3:
            create = view.create_contact()
            if create:
                model.db_list.append(create)
        case 4:
            (chan_cont, chan_ID) = view.change_contact(model.db_list)
            if chan_cont:
                model.db_list[chan_ID - 1] = chan_cont
        case 5:
            delete = view.delete_contact(model.db_list)
            if delete:
                model.db_list.pop(delete - 1)
        case 6:
            view.search_contact(model.db_list)
        case 7:
            model.save_db(model.db_list, 'data_base.txt')
            model.source_db = model.db_list
        case 8:
            model.read_db('data_base.txt', model.source_db)
            ex_choice = view.exit_programm(model.source_db, model.db_list)
            if ex_choice == '1':
                model.save_db(model.db_list, 'data_base.txt')
                exit()
            else:
                exit()


def start():
    while True:
        user_choice = view.main_menu()
        input_processing(user_choice)
