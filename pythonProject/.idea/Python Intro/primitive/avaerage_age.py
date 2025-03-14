def get_avg_age(students_dict):
    no_of_items = len(students_dict)
    total_age = 0
    for item in students_dict.values():
        total_age = item + total_age
    return total_age // no_of_items


students = {
    '1': 20,
    '2': 34,
    '3': 21,
    '4': 32,
}

avg = get_avg_age(students)
print(avg)
