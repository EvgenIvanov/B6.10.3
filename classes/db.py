from classes.account import Account

class Storage(Account):
    __id = 0
    def __init__(self):
        self.entitys = {}

    def add_account(self, Account):
        Storage.__id += 1
        self.entitys[Storage.__id] = Account.__dict__
        return Storage.__id

    def delete_account_by_id(self, id):
        print('==>id=' + str(id))
        return self.entitys.pop(id, 'not found')

    def get_account_by_id(self, id):
        entity = self.entitys.get(id, 'not found')
        if entity == 'not found':
            return entity
        return Account(*entity.values())