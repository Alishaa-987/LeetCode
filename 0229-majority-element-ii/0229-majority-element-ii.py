class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n =  len(nums)
        a = n//3
        res = []
        dict = {}
        for i in range(len(nums)):
            if nums[i]  not in dict:
                dict[nums[i]] = 1
            else:
                dict[nums[i]]+= 1
        for i in dict:
            if dict[i] > a :
                res.append(i)
        return res
        
