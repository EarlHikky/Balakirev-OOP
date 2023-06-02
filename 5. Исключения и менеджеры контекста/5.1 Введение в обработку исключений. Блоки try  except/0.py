try:
    x, y = map(int, input().split())
    res = x / y
except ZeroDivisionError:
    print("Делить на ноль нельзя!")
except ValueError:
    print("Ошибка типа данных")


def get_number(x):
    try:
        return int(x)
    except:
        try:
            return float(x)
        except:
            return x