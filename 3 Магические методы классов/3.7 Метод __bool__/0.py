bool(123)
bool(-1)
bool(0)
bool("python")
bool("")
bool([])


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        print("__len__")
        return self.x * self.x + self.y * self.y

p = Point(3, 4)
print(bool(p))


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __bool__(self):
        print("__bool__")
        return self.x == self.y


p = Point(3, 4)
print(bool(p))

p = Point(0, 0)

p = Point(10, 20)

if p:
    print("объект p дает True")
else:
    print("объект p дает False")
