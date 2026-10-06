class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack=[]
        count=0
        for i in s:
            if stack and i==')':
                stack.pop()
            elif i==')':
                count+=1
            else:
                stack.append(i)
        return len(stack)+count
