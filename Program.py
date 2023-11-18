import os



class Contact:

    def __init__(self, name, surname, patronymic, phone):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.phone = phone
    
    def get_data(self):
        return f"Name = {self.name}\nSurname = {self.surname}\nPatronymic = {self.patronymic}\nPhone = {self.phone}"

class Phonebook:

    def __init__(self):
        self.contacts = []
    
    def add_contact(self, name, surname, patronymic, phone):
        self.contacts.append(Contact(name, surname, patronymic, phone))

    def find_contact(self, atribute_name, atribute_data):
        if atribute_name == "name":
            for contact in self.contacts:
                if contact.name == atribute_data:
                    return contact.get_data()
        elif atribute_name == "surname":
            for contact in self.contacts:
                if contact.surname == atribute_data:
                    return contact.get_data()
        elif atribute_name == "patronymic":
            for contact in self.contacts:
                if contact.patronymic == atribute_data:
                    return contact.get_data()
        elif atribute_name == "phone":
            for contact in self.contacts:
                if contact.phone == atribute_data:
                    return contact.get_data()
        else:
            return
                
    def print_data(self):
        for contact in self.contacts:
            print(contact.get_data() + "\n")

    def export_data(self):
        contacts = open("contacts.txt", "w")
        for contact in self.contacts:
            contacts.write(contact.get_data() + "\n")
        contacts.close()

    def copy_string(self, file, line):
        contacts = open("contacts.txt", "r")
        somefile = open(file, "a")
        string = ""
        for i in range(1, line + 1):
            string = contacts.readline()
        somefile.write(string)
        contacts.close()
        somefile.close() 


phonebook = Phonebook()
while(True):
    os.system('clear')
    print(f"Welcome! Make your choose:\n1. Add contact.\n2. Find contact.\n3. Print data.\n4. Export data.\n5. Copy line.")
    choose = input()
    if choose == "1":
        name = input("Input name: ")
        surname = input("Input surname: ")
        patronymic = input("Input patronymic: ")
        phone = input("Input phone: ")
        phonebook.add_contact(name, surname, patronymic, phone)
    elif choose == "2":
        atribute_name = input("Input atribute name: ")
        atribute_data = input("Input atribute data: ")
        print(phonebook.find_contact(atribute_name, atribute_data))
        input()
    elif choose == "3":
        phonebook.print_data()
        input()
    elif choose == "4":
        phonebook.export_data()
    elif choose == "5":
        file = input("Input name of file: ")
        line = int(input("Input number of line: "))
        phonebook.copy_string(file, line)
    else:
        continue