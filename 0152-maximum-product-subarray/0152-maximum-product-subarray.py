class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = nums[0]
        min_product = nums[0]
        answer = nums[0]
        for i in range(1, len(nums)):
            x = nums[i]
            temp_max = max(x, x*max_product, x*min_product)
            temp_min = min(x, x*max_product, x*min_product)
            max_product = temp_max
            min_product = temp_min
            answer = max(answer, max_product)
        return answer