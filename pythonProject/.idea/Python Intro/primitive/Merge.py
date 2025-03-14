def remove_duplicates(list):
    U_L = []
    for x in list:
        if x not in U_L:
            U_L.append(x)
    return U_L

def merge_lists(list1, list2):
    for x in list1:
        list2.append(x)
    return list2


list1 = [1, 2, 34, 5]
list2 = [5, 55, 3]
merge = merge_lists(list1, list2)
print(merge)
U_L= remove_duplicates(merge)
print(U_L)
