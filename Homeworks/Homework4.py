class Contact:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

    @staticmethod
    def validate_phone_number(phone_number):
        return phone_number.isdigit() and len(phone_number) == 10


class ContactList:
    all_contacts = []

    @classmethod
    def add_contact(cls, name, phone_number):
        if Contact.validate_phone_number(phone_number):
            new_contact = Contact(name, phone_number)
            cls.all_contacts.append(new_contact)
        else:
            raise ValueError("Некорректный номер телефона! Он должен содержать ровно 10 цифр.")


print(ContactList.all_contacts)

ContactList.add_contact("Кинг Конг", "0700100200")
ContactList.add_contact("Виктор Цой", "0500123456")

for contact in ContactList.all_contacts:
    print(contact.name, contact.phone_number)
# Кинг Конг 0700100200
# Виктор Цой 0500123456

# Этот вызовет ошибку:
# ContactList.add_contact("Mr Beast", "5551234")  # Ошибка
