# random
import random

print(random.randrange(1, 10))

# slicing string
b = "Hello, World!"
print(b[2:5])

# slicing from the start
b = "Hello, World!"
print(b[:5])

# slicing from the end
b = "Hello, World!"
print(b[2:])

# negative slicing
b = "Hello, World!"
print(b[-5:-2])

# upper case
a = "Hello, World!"
print(a.upper())

# lower case
a = "Hello, World!"
print(a.lower())

# remove whitespace
# Whitespace is the space before and/or after the actual text, and very often you want to remove this space.
# The strip() method removes any whitespace from the beginning or the end
a = " Hello, World! "
print(a.strip())

# The replace() method replaces a string with another string
a = "Hello, World!"
print(a.replace("H", "J"))


# The split() method splits the string into substrings if it finds instances of the separator
a = "Hello, World!"
print(a.split(","))


# concat
a = "Hello"
b = "World"
c = a + " " + b
print(c)


# The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are.
# Use the format() method to insert numbers into strings
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

# You can use index numbers {0} to be sure the arguments are placed in the correct placeholders
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

# The escape character allows you to use double quotes when you normally would not be allowed
txt = "We are the so-called \"Vikings\" from the north."
print(txt)

# isinstance() function can be used to determine if an object is of a certain data type
x = 200
print(isinstance(x, int))

# To change the value of items within a specific range, define a list with the new values,
# and refer to the range of index numbers where you want to insert the new values
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

# The insert() method inserts an item at the specified index
theselist = ["apple", "banana", "cherry"]
theselist.insert(2, "watermelon")
print(theselist)

# To append elements from another list to the current list, use the extend() method.
thatlist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thatlist.extend(tropical)
print(thatlist)


