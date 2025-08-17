class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        left = 0
        right =1
        n = len(nums)
        while left < n and right < n :
           
            if nums[left] % 2== 0:
                left += 2
            elif nums[right] % 2 == 1 :
                right -=2
            else :
                nums[left],nums[right] = nums[right],nums[left]
                left+=2
                right-=2
        return nums
        