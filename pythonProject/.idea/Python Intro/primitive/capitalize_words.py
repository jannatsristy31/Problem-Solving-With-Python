def capitalize_words(list):
    items = []
    for x in list:
        # items = x.upper()
        items.append(x.upper())
    return items


list = ["this is fun"]
list1 = capitalize_words(list)
print(list1)
