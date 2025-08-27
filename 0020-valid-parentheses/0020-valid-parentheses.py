class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for char in s:
            if char in "({[":  
                stack.append(char)  # opening ko stack me daalo
            else:
                if not stack:  # closing aayi lekin stack empty hai
                    return False
                top = stack.pop()
                if (char == ')' and top != '(') or \
                    (char == ']' and top != '[') or \
                    (char == '}' and top != '{'):
                    return False  # match nahi kiya
    
        return len(stack) == 0  # stack empty hai to valid
