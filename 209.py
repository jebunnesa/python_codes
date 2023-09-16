from typing import List

class Solution:
    """
    Given an array of positive integers nums and a positive integer target, return the minimal length of a
    subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

    Input: target = 7, nums = [2, 3, 1, 2, 4, 3], Output: 2
    Input: target = 4, nums = [1, 4, 4], Output: 1
    Input: target = 11, nums = [1, 1, 1, 1, 1, 1, 1, 1], Output: 0
    """
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length_subarray, way_to_target_sum = None, 0
        k = 0
        for i in range(len(nums)):
            way_to_target_sum += nums[i]
            while way_to_target_sum >= target:
                if min_length_subarray is None:
                    min_length_subarray = i - k + 1
                min_length_subarray = min(i - k + 1, min_length_subarray)
                way_to_target_sum -= nums[k]
                k += 1

        if min_length_subarray is None:
            min_length_subarray = 0
        return min_length_subarray

obj = Solution()

print(obj.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
print(obj.minSubArrayLen(4,  [1, 4, 4]))
print(obj.minSubArrayLen(11,   [1, 1, 1, 1, 1, 1, 1, 1]))
print(obj.minSubArrayLen(11,   [1, 2,3,4,5]))
