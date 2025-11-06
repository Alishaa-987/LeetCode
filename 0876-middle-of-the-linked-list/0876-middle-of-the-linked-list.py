class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        # Step 1: find total length of list
        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next

        # Step 2: move to middle node
        middle = length // 2
        current = head
        for _ in range(middle):
            current = current.next

        # Step 3: return middle node
        return current
