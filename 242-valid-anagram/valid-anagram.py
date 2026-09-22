class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        mp={}
        for i in range(len(s)):
            mp[s[i]]=mp.get(s[i],0)+1
        
        for j in t:
            if j not in mp:
                return False
            mp[j]-=1

            if mp[j]<0:
                return False
        return True