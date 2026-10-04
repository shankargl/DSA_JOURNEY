class Solution:
    def checkValidString(self, s: str) -> bool:
        stack=[]
        star=[]
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(i)

            elif s[i]=='*':
                star.append(i)
            else:
                if stack:
                    stack.pop()
                elif star:
                    star.pop()
                else:
                    return False

        while stack and star:
            if stack[-1]<star[-1]:
                stack.pop()
                star.pop()
            else:
                return False
    
        return not stack