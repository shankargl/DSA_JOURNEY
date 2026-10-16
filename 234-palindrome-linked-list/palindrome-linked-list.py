# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        if head is None:
            return False
        
        slow=head
        fast=head

        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next

        temp=slow
        pre=None
        while temp:
            new=temp.next
            temp.next=pre
            pre=temp
            temp=new

        ans1=head
        ans2=pre
        while ans2:
            if ans1.val!=ans2.val:
                return False

            ans1=ans1.next
            ans2=ans2.next

        return True