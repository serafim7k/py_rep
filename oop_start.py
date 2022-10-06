class Person:
    info = "I'm a person"

    def create(self, name, age):
        self.name = name
        self.age = age
        return self.name, self.age

    def __str__(self):
        return f'{self.name}, {self.age}'

mark = Person()

print(mark.create("Mark", 15))

print(mark)
print(mark.info)
print(type(mark))
