11:48 15/01/2022 yoav eshed - LeetCode - Sum of two numbers - Python3

class Solution:
    def twoSum(self,nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            for j in range(1,len(nums)):
                if (target - nums[i]) == nums[j] and i !=j:
                    return [i, j]