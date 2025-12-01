class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        seen = set()  # to store all unique substrings of length k
        n = len(s)
        
        # sliding window of size k
        for i in range(n - k + 1):
            substring = s[i:i+k]  # current substring of length k
            seen.add(substring)    # add to set
        
        # total possible binary codes of length k = 2^k
        return len(seen) == 2 ** k
