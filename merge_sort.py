def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    return merge(left_half, right_half)


def merge(left_array, right_array):
    result = []

    i = j = 0

    while i < len(left_array) and j < len(right_array):
        if left_array[i] < right_array[j]:
            result.append(left_array[i])
            i += 1
        else:
            result.append(right_array[j])
            j += 1
    result.extend(left_array[i:])
    result.extend(right_array[j:])
    return result


a = [1,12,10,100, 11, 13,9,1, 229]
print(merge_sort(a))
