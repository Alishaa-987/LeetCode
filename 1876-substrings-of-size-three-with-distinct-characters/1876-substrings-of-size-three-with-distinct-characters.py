class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        l=0 
        r=2
        count=0
        while r<len(s):
            if s[l]!=s[l+1] and s[l]!=s[r] and s[l+1]!=s[r]:
                count+=1
                l+=1
                r+=1
            else:
                l+=1
                r+=1
        return count