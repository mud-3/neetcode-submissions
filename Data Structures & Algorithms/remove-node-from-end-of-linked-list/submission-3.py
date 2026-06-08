# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def print_list(node):
            while node:
                print(node.val, end=" ")
                node = node.next
            print()

        right = head
        left = head
        head = previous = ListNode(0, head)

        for i in range(n):
            right = right.next

        while right:
            previous = left
            left = left.next
            right = right.next
            print("left:", end=" ")
            print_list(left)
            print("right:", end=" ")
            print_list(right)
            print("previous:", end=" ")
            print_list(previous)

        print_list(left.next)
        previous.next = left.next

        return head.next