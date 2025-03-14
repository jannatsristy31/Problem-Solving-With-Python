def count_words(txt):
    x = txt.split()
    return x


list = count_words("abc cde rfg his")
print(list)
count = 0
for y in list:
    count += 1  # count=count+1

print(count)
