from collections import deque
from typing import List
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        q = deque(students)
        stack = sandwiches[:]
        count = 0

        while q and count < len(q):
            if stack[0] == q[0]:
                q.popleft()
                stack.pop(0)
                count = 0
            else:
                q.append(q.popleft())
                count +=1
        return len(q)
        