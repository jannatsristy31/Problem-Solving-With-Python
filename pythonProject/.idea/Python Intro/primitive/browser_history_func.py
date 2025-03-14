def create_stack_back_history():
    return []


def create_stack_forward_history():
    return []


def backward_push(stack, items):
    stack.append(items)
    return stack


def backward_pop(stack):
    if len(stack) != 0:
        new_item = stack.pop()
        forward_push(forward_stack, new_item)
        return new_item


def forward_push(stack, items):
    stack.append(items)
    return stack


def forward_pop(stack):
    if len(stack) != 0:
        return stack.pop()


back_stack = create_stack_back_history()
backward_push(back_stack, 'selfie')
backward_push(back_stack, 'duplicate')
backward_push(back_stack, 'copy')
backward_push(back_stack, 'paste')
backward_push(back_stack, 'create')
print(back_stack)
forward_stack = create_stack_forward_history()

backward_pop(back_stack)
backward_pop(back_stack)
backward_pop(back_stack)


print(forward_stack)
print(back_stack)



