def create_stack():
    return []


def push(stack, x):
    stack.append(x)
    return stack


def pop(stack):
    if len(stack) != 0:
        return stack.pop()


def reverse_words(input):
    for char in input.split():
        push(stack, char)

    output = ""
    for i in range(0, len(stack)):
        char = pop(stack)
        output = output + char + " "
    return output


stack = create_stack()
input = "confused anga unga bunga"
print(reverse_words(input))
