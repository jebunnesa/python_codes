import math


def triplet_sum_close_to_target(arr, target_sum):
    min_diff = math.inf
    arr.sort()
    for i in range(len(arr)-2):
        left = i+1
        right = len(arr)-1
        while left < right:
            diff = target_sum - arr[i] - arr[left] - arr[right]
            if diff == 0:
                return target_sum
            if abs(min_diff) > abs(diff) or (abs(min_diff) == abs(target_sum) and min_diff<target_sum):
                min_diff = diff
            if diff > 0:
                left += 1
            else:
                right -= 1
    # print(target_sum - min_diff)
    return target_sum- min_diff


if __name__ == '__main__':
    print(triplet_sum_close_to_target([2, 0, 1, 2], 2))
    print(triplet_sum_close_to_target([-3, -1, 1, 2], 1))
