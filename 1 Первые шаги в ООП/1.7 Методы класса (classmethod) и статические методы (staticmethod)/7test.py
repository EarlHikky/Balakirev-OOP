from string import ascii_lowercase, digits

CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
CHARS_CORRECT = CHARS + CHARS.upper() + digits
name = ';УЙ'

print(set(name))
print(set(CHARS_CORRECT))
print(set(name) <= set(CHARS_CORRECT))

