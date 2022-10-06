
class Mazda:
    engine = '2.5 Gas'
    year = '2022 year'

    def __init__(self, owner_first, owner_second):
        self.owner_first = owner_first
        self.owner_second = owner_second

    def __str__(self):
        return f'{self.owner_first} and {self.owner_second} owners Mazda {Mazda.engine}, {Mazda.year} of create.'

    def color(self):
        print('Owner_1 -', self.owner_first, ': red')
        print('Owner_2 -', self.owner_second, ': blue')

    def run(self):
        print('Set and drive!')

    # def __str__(self):

car_1 = Mazda('Timur', 'Julia')
# car_1.get_info_owner()
print(car_1)
car_1.color()
car_1.run()

car_2 = Mazda('Max', 'Serafim')
print(car_2)
