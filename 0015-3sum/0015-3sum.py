class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []  # answer array
        nums.sort() # sort the orignal array when you use two pointer approch

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            j = i + 1
            k = len(nums) - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    j+=1
                    k-=1
                    while nums[j] == nums[j-1] and j < k:
                        j += 1
                    while nums[k] == nums[k+1] and j< k:
                        k-=1

                elif total < 0:
                    j+= 1
                else :
                    k-= 1
           

        return res