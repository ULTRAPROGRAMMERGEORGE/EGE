from itertools import *

s = ''
k = 0
# Короче тут мы типо берём значения которые можно ебать а дальше повторяем их 5 раз для 5 значного числа
for i in product('0234567', repeat=5):
    s.join(i)
for j in range(4):
    for h in range(5):  # Ищем значения где рядом чётных нет и нет нечётных
        if (int(s[j]) % 2 != 0 or int(s[h]) % 2 != 0) and s[j] != s[h]:
            if (int(s[j]) % 2 == 0 or int(s[h]) % 2 == 0) and s[j] != s[h]:
                k += 1
print(k)
