def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left_arr = arr[:mid]
        right_arr = arr[mid:]
        merge_sort(left_arr)
        merge_sort(right_arr)
        i = j = k = 0
        while i<len(left_arr) and j<len(right_arr):
            if left_arr[i]<right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1


def print_sort(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print("\n")


if __name__ == '__main__':
    arr = [5, 3, 10, 9, 13, 18, 9, 21]
    
    try:
        arr = []
        while True:
            arr.append((int(input())))
    except:
        merge_sort(arr)
        print_sort(arr)

