class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        ans=0
        stack=[]
        for i in s:
            if i=='(':
                stack.append(0)
            else:
                val=stack.pop()
                if val==0:
                    val=1
                else:
                    val*=2
                if stack:
                    stack[-1]+=val
                else:
                    ans+=val
        return ans

            