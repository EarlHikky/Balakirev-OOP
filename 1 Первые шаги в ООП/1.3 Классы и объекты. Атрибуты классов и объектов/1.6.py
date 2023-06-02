"""Подвиг 6. Объявите класс с именем Notes и определите в нем следующие атрибуты:

uid: 1005435
title: "Шутка"
author: "И.С. Бах"
pages: 2
Затем, с помощью функции getattr() прочитайте и выведите на экран значение атрибута author."""

class Notes:
    pass
d = {
        'uid': 1005435,
        'title': "Шутка",
        'author': "И.С. Бах",
        'pages': 2}

[setattr(Notes,k,v) for k,v in d.items()]

#print(Notes.__dict__['color'])
print(getattr(Notes, 'author'))
