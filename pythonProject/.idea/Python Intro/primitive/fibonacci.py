def fibonacci(n):
    list = [0, 1]

    for i in range(2, n):
        sum = list[-2] + list[-1]
        list.append(sum)
    return list


n = 15
print(fibonacci(n))
