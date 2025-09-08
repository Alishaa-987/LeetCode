class MyQueue:

    def __init__(self):
        self.inStack = []   # push karne ke liye
        self.outStack = []  # pop/peek ke liye

    def push(self, x: int) -> None:
        # hamesha naya element inStack me daal do
        self.inStack.append(x)

    def pop(self) -> int:
        # agar outStack khali hai to inStack se sab transfer karo
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())
        # ab outStack se pop karo
        return self.outStack.pop()

    def peek(self) -> int:
        # agar outStack khali hai to inStack se sab transfer karo
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())
        # ab outStack ka top element return karo
        return self.outStack[-1]

    def empty(self) -> bool:
        # dono stacks agar khali hain to queue bhi khali hai
        return not self.inStack and not self.outStack
