class Person:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_full_fio(self):
        return self.first_name.capitalize()  + ' ' + self.last_name.capitalize() + '.'

# test = Person('Иван','Иванов')
# print(test.get_full_fio())