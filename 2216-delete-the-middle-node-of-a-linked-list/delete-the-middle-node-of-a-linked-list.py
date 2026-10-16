# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: ListNode | None) -> ListNode | None:
        
        if head is None or head.next is None:
            return None

        slow=head
        fast=head
        pre=None

        while fast is not None and fast.next is not None:
            pre=slow
            slow=slow.next
            fast=fast.next.next

        pre.next=slow.next

        return head

