from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
	def __init__(self, value):
         super().__init__(value)


class Phone(Field):
    def __init__(self, value:str):
        if len(value) == 10 and value.isdigit():
            super().__init__(value)
        else:
            raise ValueError


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone:str):
        self.phones.append(Phone(phone))
    
    def remove_phone(self, phone:str):
        for item in self.phones:
            if phone == item.value:
                self.phones.remove(item)
                return
    
    def edit_phone(self, old, new):
        for phone in self.phones:
            if old == phone.value:
                self.remove_phone(old)
                self.add_phone(new)
                return
        raise ValueError
   
    def find_phone(self, phone:str)->Phone|None:
        for i in self.phones:
            if i.value == phone:
                return i
        return None
            
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record:Record):
        self.data.update({record.name.value:record})
        
    def find(self, name:str)->Record|None:
        return None if self.data.get(name) == -1 else self.data.get(name)
    
    def delete(self, name):
        self.data.pop(name, None)
    
    def __str__(self) -> str:
        string = "\nYour address book\n--------------------------\n"
        for value in self.data.values():
            string += str(value) + "\n"
        string += "--------------------------\n"
        return string


if __name__=="__main__":
    # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
     
    print(book)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555

    # Видалення запису Jane
    book.delete("Jane")