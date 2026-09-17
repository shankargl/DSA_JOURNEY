# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr=[]
        temp=head
        while temp:
            arr.append(temp.val)
            temp=temp.next
        stack=[]
        for i in range(len(arr)):
            while stack and stack[-1]<arr[i]:
                stack.pop()
            stack.append(arr[i])
        dummy=ListNode(0)
        temp=dummy
        for j in stack:
            temp.next=ListNode(j)
            temp=temp.next
        dummy=dummy.next
        return dummy