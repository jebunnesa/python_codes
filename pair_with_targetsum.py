def pair_with_targetsum(arr, target_sum):
    left = 0
    right = len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target_sum:
            return [left, right]
        elif current_sum > target_sum:
            right -= 1
        else:
            left +=1

if __name__ == '__main__':
    print(str(pair_with_targetsum([2, 5, 9, 11], 11)))