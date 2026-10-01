class Solution:
    def findMin(self, nums: List[int]) -> int:
        nums.sort()
        left = nums[0]
        right = len(nums) - 1
        return left

