import math

def smallest_subarray_sum(s, arr):
    max_sum, window_sum = 0, 0
    window_start, window_end = 0, 0
    min_len = math.inf
    k = 0
    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        k += 1
        while window_sum >= s:
            min_len = min(min_len, k)
            k -= 1
            window_sum -= arr[window_start]
            window_start += 1
    return min_len


if __name__ == '__main__':
    print(str(smallest_subarray_sum(8, [3, 4, 1, 1, 6])))
