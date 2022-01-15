def remove_duplicates(arr):
    next_unique = 1
    i = 1
    while i<len(arr):
        if arr[next_unique - 1] != arr[i]:
            arr[next_unique] = arr[i]
            next_unique += 1
        i += 1
    # return arr[:next_unique]
    return  next_unique


def remove_element(arr, key):
    next_key = 0
    for i in range(len(arr)):
        if arr[i] !=key:
            arr[next_key] = arr[i]
            next_key += 1
    # return arr[:next_key]
    return next_key


if __name__ == '__main__':
    print(remove_duplicates([2, 9, 9]))
    print("remains element "+ str(remove_element([2,11, 2, 2, 1], 2)))
    print("remains element "+ str(remove_element([3, 2, 3, 6, 3, 10, 9, 3], 3)))