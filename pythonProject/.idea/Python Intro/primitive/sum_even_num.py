def sum_even_numbers(list):
    total = 0
    for x in list:
        if x % 2 == 0:
            total = total + x
    return total


list = (3, 4, 67, 54, 34, 55, 7, 1)
sum = sum_even_numbers(list)
print(sum)
