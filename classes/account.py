from classes.person import Person

class Account(Person):

    def __init__(self, first_name, last_name, balance = 0, login = "", password = ""):
        Person.__init__(self, first_name, last_name)
        self.balance = balance
        self.login = login
        self.password = password
    
    def get_info(self):
        return 'Баланс: ' + str(self.balance) + ' руб. '
    
    def __str__(self):
        return 'Клиент "' + Person.__str__(self) + '". ' + self.get_info()