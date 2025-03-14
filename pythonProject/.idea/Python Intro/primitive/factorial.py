def factorial(n):
    if n < 0:
        return False
    elif n == 0:
        return 1
    result = 1

    for i in range(1, n + 1):
        result = result * i
    return result


n = 4
print(factorial(n))
