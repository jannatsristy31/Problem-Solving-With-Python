def create_stack():
    return []


def push():
    item = 100
    list1 = [1, 2, 15, 25, 20]
    list2 = [item]
    list = list1 + list2
    return list


def pop():
    global new_list
    new_list = new_list[0:-1]
    return new_list


def peek():
    global new_list
    top_item = new_list[-1]
    return top_item


new_list = push()
print(push())
remove = pop()
print(remove)

print(peek())
