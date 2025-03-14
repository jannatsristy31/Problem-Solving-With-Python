def reverse_string(input_s):
    r_s = ""
    for x in input_s:
        r_s = x + r_s
    return r_s


input_s = "I wonder how this will look"
reverse_s = reverse_string(input_s)
print(reverse_s)
