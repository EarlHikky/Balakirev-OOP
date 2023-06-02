class FRange:
    def __init__(self, start=0.0, stop=0.0, step=1.0):
        self.start = start
        self.stop = stop
        self.step = step
        self.value = self.start - self.step

    def __next__(self):
        if self.value + self.step < self.stop:
            self.value += self.step
            return self.value
        else:
            raise StopIteration

    def __iter__(self):
        self.value = self.start - self.step
        return self


fr = FRange(0, 2, 0.5)

print(fr.__next__())
print(fr.__next__())
print(fr.__next__())
print(fr.__next__())

fr = FRange(0, 2, 0.5)
print(next(fr))
print(next(fr))
print(next(fr))
print(next(fr))

for x in fr:
    print(x)

it = iter(fr)

fr = FRange(0, 2, 0.5)
it = iter(fr)
print(next(it))
print(next(it))
print(next(it))
print(next(it))

it = iter(fr)
print(next(it))
print(next(it))
print(next(it))
print(next(it))

it = iter(fr)
print(next(it))
print(next(it))
print(next(it))
print(next(it))


class FRange2D:
    def __init__(self, start=0.0, stop=0.0, step=1.0, rows=5):
        self.fr = FRange(start, stop, step)
        self.rows = rows

    def __iter__(self):
        self.value_row = 0
        return self

    def __next__(self):
        if self.value_row < self.rows:
            self.value_row += 1
            return iter(self.fr)
        else:
            raise StopIteration


fr = FRange2D(0, 2, 0.5, 4)

for row in fr:
    for x in row:
        print(x, end=" ")
    print()
