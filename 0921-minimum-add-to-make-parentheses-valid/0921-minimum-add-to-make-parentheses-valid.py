class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        cnt = 0
        for char in s:
            if char == "(":
                stack.append(char)
            else:
                if stack:
                    stack.pop()
                else:
                    cnt += 1
        return cnt + len(stack)