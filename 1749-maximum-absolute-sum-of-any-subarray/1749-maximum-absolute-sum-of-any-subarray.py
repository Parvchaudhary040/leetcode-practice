class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_curr = max_sum = nums[0]
        min_curr = min_sum = nums[0]
        for i in range(1, len(nums)):
            max_curr = max(nums[i], max_curr + nums[i])
            max_sum = max(max_sum, max_curr)
            min_curr = min(nums[i], min_curr + nums[i])
            min_sum = min(min_sum, min_curr)
        return max(max_sum, abs(min_sum))