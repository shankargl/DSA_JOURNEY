# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        ans=[]
        i=2
        temp=head
        pre=None
        while temp.next:
            if pre:
                if pre.val<temp.val>temp.next.val:
                    ans.append(i)
                    i+=1
                elif pre.val>temp.val<temp.next.val:
                    ans.append(i)
                    i+=1
                else:
                    i+=1
            pre=temp
            temp=temp.next
        if len(ans) < 2:
            return [-1, -1]

        mini = float('inf')

        for j in range(1, len(ans)):
            mini = min(mini, ans[j] - ans[j - 1])

        maxi = ans[-1] - ans[0]

        return [mini, maxi]