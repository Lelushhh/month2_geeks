class Person:
    def __init__(self, name, birth_date, occupation, higher_education ):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education
    def introduce(self):
        edu_status = "имею высшее образование" if self.higher_education else "не имею высшее образование"
        print(f"Салам! Меня зовут {self.name}. Я {self.occupation}." 
              f"Дата моего рождения: {self.birth_date}. Я {edu_status}.\n")

person1 = Person("Ксено Хьюстон", "01.10.1993", "Ученый НАСА",True)
person2 = Person("Джеймс Барнс", "10.03.1917", "Офицер армии США", False)
person3 = Person("Леви Акерман", "25.12.1980", "капитан разведкорпуса", False)

for person in (person1, person2, person3):
    print(f"Имя: {person.name}")
    print(f"Дата рождения: {person.birth_date}")
    print(f"Профессия: {person.occupation}")
    print(f"Высшее образование: {person.higher_education}")
    person.introduce()

