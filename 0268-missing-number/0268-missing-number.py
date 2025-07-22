class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        exp_sum = n*(n+1)//2
        act_sum = sum(nums)
        return exp_sum - act_sum

        # temp = n
        # for i in range(n) :
        #    temp ^= i
        #    temp ^= nums[i]
        # return temp

        # nums.sort()
        # for i in range(n) :
        #    if nums[i] != i :
        #        return i
        # return i+1