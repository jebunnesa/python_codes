def search_ceiling_number(arr, key):
    if arr[len(arr) - 1] < key:
        return -1
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left+right)//2
        if arr[mid] < key:
            left = mid + 1
        elif arr[mid] > 1:
            right = mid-1
    return left


def search_floor_of_a_number(arr, key):
    if arr[0] > key:
        return -1
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (right+left)//2
        if arr[mid] < key:
            left = mid + 1
        elif arr[mid] > key:
            right = mid-1
        else:
            return mid
    return right


def main():
    print("search ceiling term")
    print(search_ceiling_number([4, 6, 10], 6))
    print(search_ceiling_number([1, 3, 8, 10, 15], 12))
    print(search_ceiling_number([4, 6, 10], 17))
    print(search_ceiling_number([4, 6, 10], -1))
    print("search floor term")
    print(search_floor_of_a_number([4, 6, 10], 6))
    print(search_floor_of_a_number([1, 3, 8, 10, 15], 12))
    print(search_floor_of_a_number([4, 6, 10], 17))
    print(search_floor_of_a_number([4, 6, 10], -1))


main()