class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)

        # dp[i][j] := the maximum dot product of the two sub-sequences nums[0..i) and nums2[0..j)
        dp = [[float('-inf') for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # (i, j) are paired and we get the optimum value from dp[i - 1][j -1]
                # or just only read dot and start from it
                prod = nums1[i - 1] * nums2[j - 1] + max(dp[i - 1][j - 1], 0)

                # or we skip and use prev row or column in dp
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j], prod)


        return dp[-1][-1]