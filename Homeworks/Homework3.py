class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.__occupation = occupation
        self.__higher_education = higher_education

    def introduce(self):
        edu_status = "да" if self.__higher_education else "нет"
        print(f"Привет, меня зовут {self.name}. Моя профессия {self.__occupation}. "
              f"У меня высшее образование: {edu_status}.")


    def get_occupation(self):
        return self.__occupation

    def get_higher_education(self):
        return self.__higher_education


class Classmate(Person):
    def __init__(self, name, birth_date, occupation, higher_education, group_name, classmate_name):
        super().__init__(name, birth_date, occupation, higher_education)
        self.group_name = group_name
        self.classmate_name = classmate_name

    def introduce(self):
        edu_status = "да" if self._Person__higher_education else "нет"
        print(f"Привет, меня зовут {self.name}. Моя профессия {self._Person__occupation}. "
              f"Я учился с {self.classmate_name} в группе {self.group_name}. "
              f"У меня высшее образование: {edu_status}.")


class Friend(Person):
    def __init__(self, name, birth_date, occupation, higher_education, hobby, friend_name):
        super().__init__(name, birth_date, occupation, higher_education)
        self.hobby = hobby
        self.friend_name = friend_name

    def introduce(self):
        edu_status = "да" if self._Person__higher_education else "нет"
        print(f"Привет, меня зовут {self.name}. Моя профессия {self._Person__occupation}. "
              f"Мое хобби {self.hobby}. Я друг {self.friend_name}. "
              f"У меня высшее образование: {edu_status}.")


class BestFriend(Friend):
    def __init__(self, name, birth_date, occupation, higher_education, hobby, friend_name, shared_memory):
        super().__init__(name, birth_date, occupation, higher_education, hobby, friend_name)
        self.shared_memory = shared_memory

    def introduce(self):
        super().introduce()
        print(f"У нас с {self.friend_name} есть общее воспоминание: {self.shared_memory}.")



classmate1 = Classmate("Нурэл", "06.10.2010", "студент", True, "9-Б", "Абидина")
classmate2 = Classmate("Муслим", "13.09.2010", "студент", False, "9-Б", "Абидина")

friend1 = Friend("Алмаз", "12.07.1999", "инженер", True, "играть в шахматы", "Абидина")
friend2 = Friend("Диана", "22.11.2000", "врач", True, "читать книги", "Абидина")

best_friend = BestFriend("Арман", "15.03.1998", "архитектор", True, "рисовать", "Абидином", "наша поездка в горы")


classmate1.introduce()
classmate2.introduce()
friend1.introduce()
friend2.introduce()
best_friend.introduce()

print("\nДоп. задание:")
people = [classmate1, classmate2, friend1, friend2, best_friend]
for person in people:
    person.introduce()