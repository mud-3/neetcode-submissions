# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node = head = ListNode(0)
        carry = 0

        while l1 and l2:
            value = l1.val + l2.val + carry

            if value >= 10:
                carry = value // 10
                value %= 10
            else:
                carry = 0
            
            node.next = ListNode(value)
            node = node.next

            l1 = l1.next
            l2 = l2.next
        
        remaining = l1 or l2

        if not remaining and carry:
            node.next = ListNode(carry)

        while remaining:
            value = remaining.val + carry

            if value >= 10:
                carry = value // 10
                value %= 10
            else:
                carry = 0
                
            node.next = ListNode(value)
            node = node.next

            remaining = remaining.next       
        
        if carry:
            node.next = ListNode(carry)

        return head.next