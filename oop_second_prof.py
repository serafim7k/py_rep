
class Profile:
    """ Create profile class - get 7 params input """
    def __init__(self, name, surname, phone_number, address, email, age, sex):
        self.name = name
        self.surname = surname
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.age = age
        self.sex = sex

    def save(self):
        return self.name, self.surname, self.phone_number, self.address,\
               self.email, self.age, self.sex


profile_1 = Profile(
    'Mark',
    'Lutz',
    '0665869832',
    'Kiyv',
    'mark@gmail.com',
    '25 years',
    'male'
)

print(profile_1.save())

profile_2 = Profile(
    'Serafim',
    'Lutz',
    '0665869832',
    'Kiyv',
    'serafim@gmail.com',
    '25 years',
    'male'
)

print(profile_2.save())

# print(Profile.__doc__)