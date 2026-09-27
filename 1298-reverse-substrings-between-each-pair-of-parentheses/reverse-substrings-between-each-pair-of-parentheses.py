class Solution:
    def reverseParentheses(self, s: str) -> str:
        ans=[]
        stack=[]
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(len(ans))
                continue
            if s[i]==')':
                l=stack[-1]
                r=len(ans)-1
                while l<=r:
                    ans[l],ans[r]=ans[r],ans[l]
                    l+=1
                    r-=1
                stack.pop()
                continue
            else:
                ans.append(s[i])
        return "".join(ans)