class Person:
    def __init__(self, name, birth_date, profession):
        self.name = name
        self.birth_date = birth_date
        self.profession = profession

    def introduce(self):
        print(f"Привет, меня зовут {self.name}, я родился {self.birth_date}, работаю {self.profession}.")


class Classmate(Person):
    def __init__(self, name, birth_date, profession, group_name, classmate_name):
        super().__init__(name, birth_date, profession)
        self.group_name = group_name
        self.classmate_name = classmate_name

    def introduce(self):
        print(f"Привет, меня зовут {self.name}, я одноклассник {self.classmate_name}, "
              f"я из группы {self.group_name}, родился {self.birth_date}, работаю {self.profession}.")


class Friend(Person):
    def __init__(self, name, birth_date, profession, hobby, friend_name):
        super().__init__(name, birth_date, profession)
        self.hobby = hobby
        self.friend_name = friend_name

    def introduce(self):
        print(f"Привет, меня зовут {self.name}, я друг {self.friend_name}, "
              f"я родился {self.birth_date}, работаю {self.profession}, люблю {self.hobby}.")


class BestFriend(Friend):
    def __init__(self, name, birth_date, profession, hobby, friend_name, shared_memory):
        super().__init__(name, birth_date, profession, hobby, friend_name)
        self.shared_memory = shared_memory

    def introduce(self):
        super().introduce()
        print(f"У нас с {self.friend_name} есть общее воспоминание: {self.shared_memory}.")


classmate1 = Classmate("Нурэл", "06.10.2010", "нет", "9-Б", "Абидина")
classmate2 = Classmate("Муслим", "13.09.2010", "нет", "9-Б", "Абидина")

friend1 = Friend("Алмаз", "12.07.1999", "инженер", "играть в шахматы", "Абидина")
friend2 = Friend("Диана", "22.11.2000", "врач", "читать книги", "Абидина")

best_friend = BestFriend("Арман", "15.03.1998", "архитектор", "рисовать", "Абидином", "наша поездка в горы")


classmate1.introduce()
classmate2.introduce()
friend1.introduce()
friend2.introduce()
best_friend.introduce()

print("\nДоп. задание 1:")
people = [classmate1, classmate2, friend1, friend2, best_friend]
for person in people:
    person.introduce()