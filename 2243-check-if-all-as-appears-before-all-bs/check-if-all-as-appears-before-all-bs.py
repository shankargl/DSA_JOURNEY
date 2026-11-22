class Solution:
    def checkString(self, s: str) -> bool:
        N=len(s)
        start=s[0]
        is_it=False
        for i in range(1,N):
            if s[i]!=start:
                if s[i]=='a':
                    return False
                if not is_it:
                    start=s[i]
                    is_it=True
                else:
                    return False
        return True