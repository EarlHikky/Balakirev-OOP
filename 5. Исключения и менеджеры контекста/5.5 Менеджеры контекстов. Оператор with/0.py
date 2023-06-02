fp = None
try:
    fp = open("myfile.txt")
    for t in fp:
        print(t)
except Exception as e:
    print(e)
finally:
    if fp is not None:
        fp.close()

try:
    with open("myfile.txt") as fp:
        for t in fp:
            print(t)
except Exception as e:
    print(e)

v1 = [1, 2, 3]
v2 = [1, 2]

class DefenerVector:
    def __init__(self, v):
        self.__v = v

    def __enter__(self):
        self.__temp = self.__v[:]  # делаем копию вектора v
        return self.__temp

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.__v[:] = self.__temp
        return False

with DefenerVector(v1) as dv:
    for i in enumerate(dv):
        dv[i] += v2[i]

print(v1)




try:
    with open("myfile.txt") as fin:
        with open("out.txt", "w") as fout:
            for line in fin:
                fout.write(line)
except Exception as e:
    print(e)