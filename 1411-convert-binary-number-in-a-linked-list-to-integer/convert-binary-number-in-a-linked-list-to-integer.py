# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        total=[]
        temp=head
        while temp:
            total.append(temp.val)
            temp=temp.next
        total.reverse()
        ans=0
        for i in range(len(total)):    
            ans+=total[i]*(2**i)
        return ans        