"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/bj0BeZtWghE

Подвиг 6 (на повторение). Ваша команда создает небольшой фреймворк для веб-сервера. Для этого был объявлен класс:

class Router:
    app = {}

    @classmethod
    def get(cls, path):
        return cls.app.get(path)

    @classmethod
    def add_callback(cls, path, func):
        cls.app[path] = func
И его предполагается использовать следующим образом:

@Callback('/', Router)
def index():
    return '<h1>Главная</h1>'


route = Router.get('/')
if route:
    ret = route()
    print(ret)
Здесь Callback - это класс-декоратор с параметрами: path = '/' - маршрут; router_cls = Router - класс роутера. Декоратор Callback должен обеспечивать добавление функции (в примере index) в словарь app класса Router. Ключом словаря выступает маршрут (path), а значением - ссылка на декорируемую функцию. Для этого следует использовать метод add_callback класса Router.

Затем, из роутера (Router) методом get выбирается ранее добавленная функция (в примере index), и если она существует, то вызывается с выводом результата в консоль.

Ваша задача реализовать класс-декоратор Callback.

Небольшая справка.

Для реализации декоратора с параметрами на уровне класса в инициализаторе __init__(self, methods) прописываем параметр для декоратора, а магический метод __call__() объявляем для декорирования функции:

class Handler:
    def __init__(self, path, route_cls):
        # здесь нужные строчки

    def __call__(self, func):
        # здесь строчки
P.S. В программе нужно объявить только классы. На экран выводить ничего не нужно.
"""


class Router:
    app = {}

    @classmethod
    def get(cls, path):
        return cls.app.get(path)

    @classmethod
    def add_callback(cls, path, func):
        cls.app[path] = func

class Callback:
    def __init__(self, path, router_cls):
        self.path = path
        self.router_cls = router_cls

    def __call__(self, func):
        self.router_cls.add_callback(self.path, func)
        return func

@Callback('/', Router)
def index():
    return '<h1>Главная</h1>'


route = Router.get('/')
if route:
    ret = route()
    print(ret)