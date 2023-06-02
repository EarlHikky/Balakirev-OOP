"""Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/nT_sMhJsw1E

Подвиг 2. Объявите класс Money так, чтобы объекты этого класса можно было создавать следующим образом:

my_money = Money(100)
your_money = Money(1000)
Здесь при создании объектов указывается количество денег, которое должно сохраняться в локальном свойстве (атрибуте) money каждого экземпляра класса.

P.S. На экран в программе ничего выводить не нужно."""

# здесь объявляйте класс Money
class Money():
    
    def __init__(self, money):
        self.money = money
    

my_money = Money(100)
your_money = Money(1000)