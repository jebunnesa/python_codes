def unique_triplet_zero_sum(arr):
    arr.sort()
    triplet = []
    for i in range(len(arr)):
        if i > 0 and arr[i] == arr[i-1]:
            continue
        search_pair(arr, -arr[i], i+1, triplet)
    return triplet

def search_pair(arr, target_sum, left, triplet):
    right = len(arr) -1
    while left< right:
        current_sum = arr[left] + arr[right]
        if current_sum == target_sum:
            triplet.append([-target_sum, arr[left], arr[right]])
            left += 1
            right -= 1
            while left < right and arr[left] == arr[left-1]:
                left += 1
            while left < right and arr[right] == arr[right+1]:
                right -= 1
        elif current_sum < target_sum:
            left += 1
        else:
            right -= 1
    # return arr

if __name__ == '__main__':
    print(unique_triplet_zero_sum([-3, 0, 1, 2, -1, 1, -2]))