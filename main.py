from classes.account import Account

# person_account = Account('Дональд','Трамп',10)
# print(person_account)

db = {}
question = (
    'Введите имя: ',
    'Введите фамилию: ',
    'Текущий баланс: '
)
id_ = 0
while True:
    ## ввод данных и их запись в словарь в формате JSON
    qlist = []
    for q in question:
        qlist.append(input(q))

    person_account = Account(*qlist) #'Дональд','Трамп',10)
    print('Вы ввели:', person_account)

    id_ += 1
    db[id_] = person_account.__dict__

    if input('Продолжим? (y/n) ') == "n":
        break

print('\n А теперь будем выводить записи :) \n')

while True:
    ## отображение записей
    id_ = int(input("Введите ID записи: "))

    if id_ > len(db):
        print(f'ID {id_} not found')
    else:
        person = Account(*db[id_].values())
        print(person)

    if input('Продолжим? (y/n) ') == "n":
        print('Goodbye')
        break