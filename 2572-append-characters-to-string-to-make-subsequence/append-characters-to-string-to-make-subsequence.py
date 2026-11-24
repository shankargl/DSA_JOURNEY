class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        N=len(s)
        n=len(t)
        i=0
        l=0
        while l<N and i<n:
            if s[l]==t[i]:
                i+=1
            l+=1

        if i==n:
            return 0
        if i==0:
            return len(t)

        else:
            return len(t)-i