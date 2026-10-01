class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2==1:
            return False
        stack=[]
        mp={
            '}':'{',
            ']':'[',
            ')':'('
        }
        for i in range(len(s)):
            if stack and s[i] in ['}',']',')']:
                if  stack[-1]!=mp[s[i]]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(s[i])
        if len(stack)==0:
            return True
        return False