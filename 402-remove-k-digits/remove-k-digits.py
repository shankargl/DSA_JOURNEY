class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k>=len(num):
            return '0'

        stack=[]
        for i in range(len(num)):
            while stack and ord(stack[-1])>ord(num[i]) and k>0:
                stack.pop()
                k-=1
            stack.append(num[i])

        while stack and k>0:
            stack.pop()
            k-=1

        i=0
        while i<len(stack) and stack[i]=='0':
            i+=1
        if i==len(stack):
            return '0'

        ans=''
        while i<len(stack):
            ans+=stack[i]
            i+=1

        return ans