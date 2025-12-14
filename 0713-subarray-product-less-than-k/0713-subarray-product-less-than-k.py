class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l = 0
        total = 1
        count = 0
        for r in range(len(nums)):
            total *= nums[r]
            while l <= r and total >= k:
                total //= nums[l]
                l += 1
            count += r - l + 1
        return count
        