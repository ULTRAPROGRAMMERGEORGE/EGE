max_count = 0
number = -1
for n in range(84052, 84130):
    count = 0
    for i in range(1, int(n ** 0.5)):
        if n % i == 0:
            count += 1
            if n % i != i:
                count += 1
    if max_count < count:
        max_count = count
        number = n
print(number, max_count)
