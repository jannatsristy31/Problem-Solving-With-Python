def find_max(list):
    max_value = list[0]
    print(list[1:])
    for x in list[1:]:
        if max_value < x:
            max_value = x
    return max_value


list = [2, 3, 45, 650, 46, 1, 26]
max_value=find_max(list)
print(max_value)
