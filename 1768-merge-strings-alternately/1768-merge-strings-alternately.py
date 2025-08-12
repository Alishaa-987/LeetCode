class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        n1 = len(word1)
        n2 = len(word2)
        n = min(n1 , n2)
        for i in range(n):
            res += word1[i] + word2[i]
        if n1 == n2 :
            return res
        elif n1 > n2 :
            return res + word1[n:]
        else:
            return res + word2[n:]
        