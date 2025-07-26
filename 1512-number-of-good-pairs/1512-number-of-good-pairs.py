class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0 
        hash_map = {}
        for i in nums:
            if i in hash_map:
                count+= hash_map[i]
                hash_map[i] += 1
            else:
                hash_map[i] = 1
        return count
