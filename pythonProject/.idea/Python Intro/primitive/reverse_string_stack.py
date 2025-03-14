def create_stack():
    return []


def push(stack, item):
    # print(f"inside the push function: {id(stack)}")

    # stack.append(item)
    stack += [item]

    # print(f"inside the push_function: {id(stack)}")


def pop_office():
    if len(stack) != 0:
        item = stack[-1]
        del stack[-1]
    # item = stack.pop()
    return item


def reverse_string(input):
    # print(f"inside the reverse_string function: {id(stack)}")
    for char in input:
        push(stack, char)

    r_s = ""

    for i in range(0, len(input)):
        char = pop_office()
        r_s = r_s + char

    return r_s


stack = create_stack()
# print(f"stack initialization: {id(stack)}")
input = "Hello ML!"
# print(f"input string: {id(input)}")
print(reverse_string(input))
