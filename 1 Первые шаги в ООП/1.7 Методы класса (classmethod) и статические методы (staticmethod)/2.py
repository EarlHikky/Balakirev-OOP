"""Выберите все верные варианты вызова метода json_parse:"""
class Loader:
    @classmethod
    def json_parse(cls):
        return ""
    
ld = Loader()

ld.json_parse()
#Loader.json_parse(ld)
#ld.json_parse(Loader)
Loader.json_parse()
res = ld.json_parse()
res = Loader.json_parse()
