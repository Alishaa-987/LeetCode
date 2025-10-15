# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Detect if there is a cycle present
        slow, fast = head, head
        newhead = None
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow and slow == fast:
                # Cycle is present, cut the cycle here
                newhead = slow.next
                slow.next = None
        if not newhead:
            # When cycle is present return None
            return None

        # Find the intersection. No need to check if the intersection exists as both the section are still part of the orignal linkedlist.
        curra = head
        currb = newhead
        while curra != currb:
            if curra.next:
                curra = curra.next
            else:
                curra = newhead
            if currb.next:
                currb = currb.next
            else:
                currb = head
        return curra