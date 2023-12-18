# Write a Python program to create a person class. Include attributes like name, country and date of birth. Implement a method to determine the person's age.
from datetime import date

class Person():
    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = date_of_birth

    def person_age(self):
        year = date.today().year

        return year - self.date_of_birth


prs1 = Person("necmi", "türkiye", 1986)

yas = prs1.person_age()

print(yas, prs1.name, prs1.country, prs1.date_of_birth)