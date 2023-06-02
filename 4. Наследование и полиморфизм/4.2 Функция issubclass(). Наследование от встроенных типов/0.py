class Geom:
    pass

print(Geom.__class__)


class Geom(object):
    pass

print(Geom.__class__)


class Geom(object):
    pass


class Line(Geom):
    pass

l = Line()
print(l.__class__)

print(issubclass(Line, Geom))
print(issubclass(Geom, Line))
try:
    print(issubclass(l, Geom))
except Exception as e:
    print(e)

print(isinstance(l, Geom))
print(isinstance(l, Line))
print(isinstance(l, object))

issubclass(int, object)
issubclass(list, object)


class Vector(list):
    def __str__(self):
        return " ".join(map(str, self))


v = Vector([1, 2, 3])
print(v)

print(type(v))