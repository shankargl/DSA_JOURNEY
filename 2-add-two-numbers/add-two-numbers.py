# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        dummy=ListNode()
        temp=dummy
        carry=0

        while l1 is not None or l2 is not None or carry:
            sum_val=0
            if l1:
                sum_val+=l1.val
                l1=l1.next

            if l2:
                sum_val+=l2.val
                l2=l2.next

            sum_val+=carry

            carry=sum_val//10

            temp.next=ListNode(sum_val%10)
            temp=temp.next

        return dummy.next