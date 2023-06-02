class DigitRetrieve:
#     def __init__(self, *args, **kwargs):
#         pass

    def __call__(self, value, *args, **kwargs):
        op = None
        if value.lstrip('-').isnumeric() and value.count('-') < 2:
            op = int(value)
        return op

dg = DigitRetrieve()
st = ["123", "abc", "-56.4", "0", "-5"]
digits = list(map(dg, st))  # [123, None, None, 0, -5]
print(digits)
