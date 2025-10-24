# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        s = set(nums)
        dummy = tmp = ListNode()
        dummy.next = head
        while tmp.next:
            if tmp.next.val in s: tmp.next = tmp.next.next
            else: tmp = tmp.next
        return dummy.next