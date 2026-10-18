# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode | None) -> ListNode | None:

        if head is None or head.next is None:
            return head

        odd=head
        even=head.next
        join=even

        while even is not None and even.next is not None:
            odd.next=odd.next.next
            even.next=even.next.next

            odd=odd.next
            even=even.next


        odd.next=join

        return head