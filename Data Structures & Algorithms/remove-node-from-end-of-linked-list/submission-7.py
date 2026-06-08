# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        left = right = head
        head = previous = ListNode(0, head)

        for i in range(n):
            right = right.next

        while right:
            previous = left
            left = left.next
            right = right.next

        previous.next = left.next

        return head.next