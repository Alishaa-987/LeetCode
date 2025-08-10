class Solution:
    def validPalindrome(self, s: str) -> bool:
        p1=0
        p2=len(s)-1
        while p1 < p2:
            if s[p1] != s[p2]:
                return s[p1+1:p2+1] == s[p1+1:p2+1][::-1] or \
                s[p1:p2] == s[p1:p2][::-1]
            p1+=1
            p2-=1
            
        return True