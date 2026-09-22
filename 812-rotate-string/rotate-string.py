class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):
            return False
        i=0
        n=len(s)
        while i<n:
            s=s[1:]+s[0]
            if s==goal:
                return True
            i+=1
        return False