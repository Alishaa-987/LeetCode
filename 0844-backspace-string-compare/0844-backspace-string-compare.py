class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1=[]
        t1=[]
        for ch in s:
            if ch == '#' and s1:
                s1.pop()
            elif ch != '#':
                s1.append(ch)
        for ch in t:
            if ch == '#' and t1:
                t1.pop()
            elif ch != '#' :
                t1.append(ch)
        return s1 == t1

