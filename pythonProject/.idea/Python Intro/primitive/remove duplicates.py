def remove_duplicates(list):
    U_L = []
    for x in list:
        if x not in U_L:
            U_L.append(x)
    return U_L


if __name__ == "__main__":
    list = [2, 3, 1, 4, 1, 5, 6, 6, 7, 9, 0, 11, 3]
    duplicates = remove_duplicates(list)
    print(duplicates)
