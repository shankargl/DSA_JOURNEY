# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        arr=[]
        temp=head
        while temp:
            arr.append(temp.val)
            temp=temp.next
        i=0
        l=len(arr)-1
        ans=[]
        while len(ans)<len(arr):
            ans.append(arr[i])
            ans.append(arr[l])
            i+=1
            l-=1
        temp=head
        k=0
        while temp:
            temp.val=ans[k]
            temp=temp.next
            k+=1
            