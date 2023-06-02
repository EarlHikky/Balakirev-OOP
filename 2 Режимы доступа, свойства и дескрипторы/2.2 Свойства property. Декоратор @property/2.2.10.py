"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/TMPPmryMKD0

Подвиг 10 (на закрепление). Вы создаете телефонную записную книжку. Она определяется классом PhoneBook. Объекты этого класса создаются командой:

p = PhoneBook()
А сам класс должен иметь следующий набор методов:

add_phone(phone) - добавление нового номера телефона (в список);
remove_phone(indx) - удаление номера телефона по индексу списка;
get_phone_list() - получение списка из объектов всех телефонных номеров.

Каждый номер телефона должен быть представлен классом PhoneNumber. Объекты этого класса должны создаваться командой:

note = PhoneNumber(number, fio)
где number - номер телефона (число) в формате XXXXXXXXXXX (одиннадцати цифр, X - цифра); fio - Ф.И.О. владельца номера (строка).

В каждом объекте класса PhoneNumber должны формироваться локальные атрибуты:

number - номер телефона (число);
fio - ФИО владельца номера телефона.

Необходимо объявить два класса PhoneBook и PhoneNumber в соответствии с заданием.
"""
class PhoneBook:
    def __init__(self):
        self.l = []
           
    def add_phone(self, phone):
        self.l.append(phone)

    def get_phone_list(self):
        return self.l
    
    def remove_phone(self, indx):
        self.l.pop(indx)
         
class PhoneNumber:
    def __init__(self, number, fio):
        self.number = number
        self.fio = fio

        
p = PhoneBook()
p.add_phone(PhoneNumber(12345678901, "Сергей Балакирев"))
p.add_phone(PhoneNumber(21345678901, "Панда"))
phones = p.get_phone_list()
print(phones)


"""

class PhoneBook:
    def __init__(self):
        self.book = {} 
          
    def add_phone(self, phone):        
        self.book.update({phone.fio: phone.number})
     
    def get_phone_list(self):
        return self.book
    
    def remove_phone(self, indx):
        self.l.pop(indx)
         
class PhoneNumber:
    def __init__(self, number, fio):
        self.number = number
        self.fio = fio
        
#     @classmethod
#     def check(cls, value):
#         return len(str(value)) == 11 and str(value).isdigit()        
        
p = PhoneBook()
p.add_phone(PhoneNumber(12349678901, "Сергей Балакирев"))
p.add_phone(PhoneNumber(21345678901, "Панда"))
#p.remove_phone(1)
#print(p.__dict__)
phones = p.get_phone_list()
print(phones)
"""