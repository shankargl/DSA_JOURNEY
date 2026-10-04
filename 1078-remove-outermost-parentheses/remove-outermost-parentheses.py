class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        N=len(s)
        ans=""
        count=0
        for ch in s:
            if ch=='(':
                count+=1
                if count>1:
                    ans+=ch
            else:
                count-=1
                if count>=1:
                    ans+=ch
        return ans


        
            