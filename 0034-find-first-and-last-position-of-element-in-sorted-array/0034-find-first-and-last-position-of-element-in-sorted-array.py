class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        left =self.findleftvalue(nums,target)
        right=self.findrightvalue(nums,target)
        
        return [left,right]
    
    def findleftvalue(self,nums,target):
        left = 0
        right = len(nums)-1
        
        
        
        while left <= right:
            mid = (left+right) //2
            if (nums[mid] == target):
                if mid == 0 or nums[mid-1] != target and mid-1 >=0:
                    return mid
                right=mid-1
            elif (nums[mid] > target):
                right = mid-1
            else:
                left = mid + 1
        return -1
    
    def findrightvalue(self,nums,target):
        left = 0
        right = len(nums)-1
        
        
        
        while left <= right:
            mid = (left+right) //2
            if (nums[mid] == target):
                if mid == len(nums)-1 or nums[mid+1] != target and mid+1<len(nums):
                    return mid
                left=mid+1
            elif(nums[mid] > target):
                right = mid-1
            else:
                left = mid + 1
        return -1