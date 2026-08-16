# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stack = []
        ans = []

        temp = head

        while temp:
            ans.append(0)

            while stack and stack[-1][1] < temp.val:
                index, value = stack.pop()
                ans[index] = temp.val

            stack.append((len(ans) - 1, temp.val))

            temp = temp.next

        return ans