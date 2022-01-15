def subarray_sum(k, arr):
    max_sum = 0
    window_sum = 0
    window_start, window_end = 0, 0
    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        if window_end >= k-1:
            max_sum = max(max_sum, window_sum)
            window_sum -= arr[window_start]
            window_start += 1
    return max_sum


def main():
    print(str(subarray_sum(3, [2, 1, 5, 1, 3, 2])))
    print(str(subarray_sum(2, [2, 3, 4, 1, 5])))


main()