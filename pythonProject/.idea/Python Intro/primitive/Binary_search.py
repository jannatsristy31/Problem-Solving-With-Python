def binary_search(list, target):
    start = 0
    end = len(list) - 1
    while start <= end:
        mid = (start + end) // 2
        x = list[mid]
        if target == x:
            return mid, list[mid]
        elif target > x:
            start = mid + 1
        elif target < x:
            end = mid - 1
    return -1, None


list = [11, 20, 25, 31, 47, 49, 67, 88, 90]
target = 67
index, value = binary_search(list, target)
print(f"index: {index}, value: {value}")