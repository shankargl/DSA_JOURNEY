class Solution:
    def minChanges(self, s: str) -> int:
        N=len(s)
        count=0
        for i in range(N):
            if i%2!=0:
                if s[i]!=s[i-1]:
                    count+=1

        return count
    