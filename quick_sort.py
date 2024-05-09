def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = len(arr) // 2
    left = [x for x in arr if x < arr[pivot]]
    middle = [x for x in arr if x == arr[pivot]]
    right = [x for x in arr if x > arr[pivot]]

    return quicksort(left) + middle + quicksort(right)



my_array = [3, 6, 8, 10, 1, 2, 1, 1000, 12, 13]
sorted_array = quicksort(my_array)
print(sorted_array)
