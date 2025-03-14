def check_palindrome(input_s):
    n_s = ""
    for x in input_s:
        n_s = x + n_s
    if n_s == input_s:
        print("True")

    else:
        print("False")
    return None


input_s = "aca"
palindrome = check_palindrome(input_s)
print(palindrome)
