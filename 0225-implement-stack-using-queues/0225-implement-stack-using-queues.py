from collections import deque

class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        # Step 1: naya element q2 me daalo
        self.q2.append(x)
        # Step 2: q1 ke saare elements q2 me daalo
        while self.q1:
            self.q2.append(self.q1.popleft())
        # Step 3: q1 aur q2 swap kar do
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        return self.q1.popleft()  # top element remove

    def top(self) -> int:
        return self.q1[0]  # front element hi top hai

    def empty(self) -> bool:
        return len(self.q1) == 0
