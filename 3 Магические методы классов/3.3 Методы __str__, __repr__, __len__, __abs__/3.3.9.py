"""
Подвиг 9. Объявите класс Recipe для представления рецептов. Отдельные ингредиенты рецепта должны определяться классом Ingredient. Объекты этих классов должны создаваться командами:

ing = Ingredient(name, volume, measure)
recipe = Recipe()
recipe = Recipe(ing_1, ing_2,..., ing_N)
где ing_1, ing_2,..., ing_N - объекты класса Ingredient.

В каждом объекте класса Ingredient должны создаваться локальные атрибуты:

name - название ингредиента (строка);
volume - объем ингредиента в рецепте (вещественное число);
measure - единица измерения объема ингредиента (строка), например, литр, чайная ложка, грамм, штук и т.д.;

С объектами класса Ingredient должна работать функция:

str(ing)  # название: объем, ед. изм.
и возвращать строковое представление объекта в формате:

"название: объем, ед. изм."

Например:

ing = Ingredient("Соль", 1, "столовая ложка")
s = str(ing) # Соль: 1, столовая ложка
Класс Recipe должен иметь следующие методы:

add_ingredient(ing) - добавление нового ингредиента ing (объект класса Ingredient) в рецепт (в конец);
remove_ingredient(ing) - удаление ингредиента по объекту ing (объект класса Ingredient) из рецепта;
get_ingredients() - получение кортежа из объектов класса Ingredient текущего рецепта.

Также с объектами класса Recipe должна поддерживаться функция:

len(recipe) - возвращает число ингредиентов в рецепте.
"""



class Ingredient:
    def __init__(self, name="", volume=0.0, measure=""):
        self.name = name
        self.volume = volume
        self.measure = measure
    
    def __str__(self):
        return f"{self.name}: {self.volume}, {self.measure}"
    
    
    
    
class Recipe:    
    def __init__(self, *args, **kwargs):
        self.recipe = [] + [*args]        
        
    def add_ingredient(self, *args):        
        self.recipe.append([*args])        
    
    def get_ingredients(self):
        return tuple(self.recipe)
    
    def remove_ingredient(self, ing):
        self.recipe.remove(ing)
#        for i in self.recipe: 
#            if i.name.lower() == ing.name.lower():
#                self.recipe.remove(i)        
    
    def __len__(self):
        return len(self.recipe)



i1 = Ingredient("Соль", 1, "столовая ложка")
i2 = Ingredient("Мука", 1, "кг")
i3 = Ingredient("Мясо баранины", 10, "кг")
i4 = Ingredient("Масло", 100, "гр")
recipe = Recipe(i1, i2, i3)
print(len(recipe))
recipe.add_ingredient(i4)
print(len(recipe))
recipe.remove_ingredient(i3)
print(len(recipe))
"""
# ing = Ingredient("Соль", 1, "столовая ложка")
# s = str(ing) # Соль: 1, столовая ложка
# print(s)
recipe = Recipe()
recipe.add_ingredient(Ingredient("Соль", 1, "столовая ложка"))
recipe.add_ingredient(Ingredient("Мука", 1, "кг"))
recipe.add_ingredient(Ingredient("Мясо баранины", 10, "кг"))
#print(recipe.recipe)
ings = recipe.get_ingredients()
print(ings)
n = len(recipe)
print(n)
recipe.remove_ingredient('Мука')
ings = recipe.get_ingredients()
print(ings)
n = len(recipe)
print(n)
"""