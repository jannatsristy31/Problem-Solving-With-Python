def create_stack():
    return []


def push(stack, x):
    stack.append(x)
    return stack


def pop():
    if len(stack) != 0:
        item = stack.pop()
    return item


def check_palindrome(input):
    for i in input:
        push(stack, i)

    n_s = ""
    for y in range(0, len(input)):
        i = pop()
        n_s = n_s + i
    if n_s == input:
        return True
    else:
        return False


stack = create_stack()
input = "abba"
print(check_palindrome(input))
