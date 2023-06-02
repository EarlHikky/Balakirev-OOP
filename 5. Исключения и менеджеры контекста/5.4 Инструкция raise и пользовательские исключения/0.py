print("Куда ты скачешь, гордый конь,")
print("И где опустишь ты копыта?")
print("О мощный властелин судьбы!")
# 1 / 0
raise ZeroDivisionError("Деление на ноль")
print("Не так ли ты над самой бездной")
print("На высоте, уздой железной")
print("Россию поднял на дыбы?")

e = ZeroDivisionError("Деление на ноль")
raise e
raise "деление на ноль"


class PrintData:
    def print(self, data):
        self.send_data(data)
        print(f"печать: {str(data)}")

    def send_data(self, data):
        if not self.send_to_print(data):
            raise Exception("принтер не отвечает")

    def send_to_print(self, data):
        return False


p = PrintData()
p.print("123")


class ExceptionPrintSendData(Exception):
    """Класс исключения при отправке данных принтеру"""
    def __init__(self, *args):
        self.message = args[0] if args else None

    def __str__(self):
        return f"Ошибка: {self.message}"

p = PrintData()
p.print("123")
class ExceptionPrintSendData(Exception):
    """Класс исключения при отправке данных принтеру"""

    def send_data(self, data):
        if not self.send_to_print(data):
            raise ExceptionPrintSendData("принтер не отвечает")


p = PrintData()

try:
    p.print("123")
except ExceptionPrintSendData:
    print("Ошибка печати")

class ExceptionPrint(Exception):
    """Общий класс исключения принтера"""

class ExceptionPrintSendData(ExceptionPrint):
    """Класс исключения при отправке данных принтеру"""


p = PrintData()

try:
    p.print("123")
except ExceptionPrintSendData as e:
    print(e)
except ExceptionPrint:
    print("Ошибка печати")

