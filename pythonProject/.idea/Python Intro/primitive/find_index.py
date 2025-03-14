def find_index(list):
    target_element = "kiwi"
    index_list = []
    count = 0
    for x in list:
        if target_element == x:
            index_list.append(count)

        count = count + 1
    return index_list


list = ["apple", "orange", "kiwi", "kiwi", "cherry", "mango"]
index = find_index(list)
print(index)