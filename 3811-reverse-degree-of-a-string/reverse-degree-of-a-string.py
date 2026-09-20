class Solution:
    def reverseDegree(self, s: str) -> int:
        ch=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

        ans=0
        for i in range(len(s)):
            ans+=(26-ch.index(s[i])) * (i+1)
        return ans