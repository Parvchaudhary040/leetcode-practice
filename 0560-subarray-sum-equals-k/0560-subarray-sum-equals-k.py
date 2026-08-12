class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = {0: 1}
        cur = 0
        count = 0

        for x in nums:
            cur += x
            count += seen.get(cur - k, 0)
            seen[cur] = seen.get(cur, 0) + 1

        return count