from classes.account import Account
from classes.db import Storage

# person_account = Account('Дональд','Трамп',10)
# print(person_account)
db = Storage()
# a = 
print('id = ' + str(db.add_account(Account('Дональд', 'Трамп', 10))))
print('id = ' + str(db.add_account(Account('Барак', 'Абама', 13))))
print('id = ' + str(db.add_account(Account('Джейн', 'Псаки', 1))))
# print(db.delete_account_by_id(int(1)))

while True:
    id = input('delete id: ')
    if id=="":
        break
    res = db.delete_account_by_id(int(id))
    if res == 'not found':
        print(f'id: {id} {res}')
    else:
        print(f'id: {id} deleted')
# 
# print('rec count: ' + str(db.rec_count))
# print(db.get_account_by_id(1))
# print(db.delete_account_by_id(1))


# db = {}
# question = (
#     'Введите имя: ',
#     'Введите фамилию: ',
#     'Текущий баланс: '
# )
# id_ = 0
# while True:
#     ## ввод данных и их запись в словарь в формате JSON
#     qlist = []
#     for q in question:
#         qlist.append(input(q))

#     person_account = Account(*qlist) #'Дональд','Трамп',10)
#     print('Вы ввели:', person_account)

#     id_ += 1
#     db[id_] = person_account.__dict__

#     if input('Продолжим? (y/n) ') == "n":
#         break

# print('\n А теперь будем выводить записи :) \n')

# while True:
#     ## отображение записей
#     id_ = int(input("Введите ID записи: "))

#     if id_ > len(db):
#         print(f'ID {id_} not found')
#     else:
#         person = Account(*db[id_].values())
#         print(person)

#     if input('Продолжим? (y/n) ') == "n":
#         print('Goodbye')
#         break