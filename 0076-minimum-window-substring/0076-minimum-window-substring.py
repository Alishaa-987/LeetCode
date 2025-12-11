class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(t), len(s)
        if m > n:
            return ""
        left = 0
        formed = 0
        count = {}
        res = ""
        length = float('inf')
        for i in t:
            count[i] = count.get(i, 0) + 1
        curr = {}
        for right in range(n):
            curr[s[right]] = curr.get(s[right], 0) + 1
            if s[right] in t and curr[s[right]] == count[s[right]]:
                formed += 1
            while formed == len(count):
                if right-left+1 <= length:
                    length = right-left+1
                    res = s[left:right+1]
                curr[s[left]] -= 1
                if s[left] in t and curr[s[left]] < count[s[left]]:
                    formed -= 1
                if curr[s[left]] == 0:
                    del curr[s[left]]
                left += 1
        return res