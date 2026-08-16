# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        ans=[]
        temp=head
        while temp:
            ans.append(temp.val)
            temp=temp.next
        left-=1
        right-=1
        while left<=right:
            ans[left],ans[right]=ans[right],ans[left]
            left+=1
            right-=1
        temp=head
        i=0
        while temp:
            temp.val=ans[i]
            i+=1
            temp=temp.next
        return head