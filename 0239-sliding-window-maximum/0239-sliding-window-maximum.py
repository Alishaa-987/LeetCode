class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans=[]
        q=collections.deque()
        l=r=0

        for r in range(len(nums)):
            while q and nums[q[-1]]<nums[r]: # Always maintain desc order so larger ele in left position
                q.pop() # if incomig ele is large then pop until it follows order of desc
            q.append(r)

            while q[0]<l: # if large ele in left is out of boubd for window size we don't consider that.
                q.popleft() 
            
            if r>=k-1: # search for largest only after reaching window size k
                ans.append(nums[q[0]])
                l+=1 # left update starts when window reaches valid size
        return ans