class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        n = len(arr)
        window_sum = sum(arr[:k])
        count = 0
        if window_sum >= k*threshold:
            count += 1
        for i in range(k, n):
            window_sum += arr[i]
            window_sum -= arr[i-k]
            if window_sum >= k*threshold:
                count += 1
        return count
