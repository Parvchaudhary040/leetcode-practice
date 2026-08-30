class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = nums[0]
        curr_max = max_sum = nums[0]
        curr_min = min_sum = nums[0]

        for i in range(1, len(nums)):
            curr_max = max(nums[i], curr_max + nums[i])
            max_sum = max(max_sum, curr_max)
            curr_min = min(nums[i], curr_min + nums[i])
            min_sum = min(min_sum, curr_min)

            total += nums[i]

        if max_sum < 0:
            return max_sum
        circular_sum = total - min_sum
        return max(max_sum, circular_sum)