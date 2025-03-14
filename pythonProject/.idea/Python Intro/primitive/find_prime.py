def find_prime_number(num):
    if num <= 1:
        return -1
    elif num == 2:
        return num
    x = int(num ** 0.5)

     # for i in range(3, x + 1):
    for i in range(3, num):
        if num % i == 0:
            return -1

    return num


list = []
for i in range(98, 100):
    y = find_prime_number(i)
    if y != -1:
        list.append(y)

print(list)
