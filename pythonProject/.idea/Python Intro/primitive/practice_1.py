def sum_diff(list):
    num1, num2 = list
    sum = num1 + num2
    difference = num2 - num1
    output = [sum, difference, -difference]
    print(output)
    return None


numbers = [7, 10]

print(sum_diff(numbers))


# Create a Python function called "find_max" that takes a list of numbers as input and returns
# the maximum value in the list.
def find_max(list):
    max_number = list[0]
    for x in list[:10]:
        if x > max_number:
            max_number = x
    return max_number


list = [3, 45, 1, 4, 63, 76, 88, 99, 4, 90, 9]
max_number = find_max(list)
print(max_number)
