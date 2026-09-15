class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        ans=0
        n=len(s)
        if k==1:
            return n
        l=0
        while l<=n-k:
            for d in (k,k+1):
                if l+d<=n and s[l:d+l]==s[l:d+l][::-1]:
                    ans+=1
                    l+=d
                    break
            else:
                l+=1
        return ans
