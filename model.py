import view
db_list = []
count = 0
source_db = []


def read_db(path: str, db_lst):
    # global db_lst
    with open(path, 'r', encoding='UTF-8') as file:
        my_list = file.readlines()
        for line in my_list:
            id_dict = dict()
            line = line.strip().split(';')
            id_dict['lastname'] = line[0]
            id_dict['firstname'] = line[1]
            id_dict['phone'] = line[2]
            id_dict['comment'] = line[3]
            db_lst.append(id_dict)


def save_db(db, path):
    if view.db_success(db):
        with open(path, 'w', encoding= 'UTF-8') as file:
            for i in range(len(db)):
                for v in db[i].values():
                    file.write(f'{v};')
                file.write('\n')
