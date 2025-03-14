def create_stack():
    return []


def push(stack, num):
    stack += [num]


def pop():
    if len(stack) != 0:
        num = stack[-1]
        del stack[-1]
    return num


def reverse_list(list):
    for x in list:
        push(stack, x)

    n_list = []

    for i in range(0, len(list)):
        x = pop()
        n_list = n_list + [x]

    return n_list


stack = create_stack()
list = [1, 23, 31, 60, 45, 87]
print(reverse_list(list))
