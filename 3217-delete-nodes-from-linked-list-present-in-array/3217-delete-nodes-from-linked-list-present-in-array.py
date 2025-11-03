class Solution:
    def modifiedList(self, nums: list[int], head: ListNode) -> ListNode:
        to_delete = set(nums)

        dummy = ListNode(0)
        dummy.next = head
        
        current = dummy

        while current.next:
            if current.next.val in to_delete:
                current.next = current.next.next  # delete node
            else:
                current = current.next  # move ahead

        return dummy.next
