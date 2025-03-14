def average_grades(list):
    count=0
    total=0
    for x in list:
        count = count + 1
        total = total + x
    return total/count


list = [1, 2, 73, 4, 7, 5, 3]
avg=average_grades(list)
print(avg)
