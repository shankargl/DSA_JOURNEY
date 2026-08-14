class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        mp={}
        ans=0
        l=0
        for i in range(len(s)):
            mp[s[i]]=mp.get(s[i],0)+1
            while mp[s[i]]>2:
                mp[s[l]]-=1
                if mp[s[l]]==0:
                    del mp[s[l]]
                l+=1
            ans=max(ans,i-l+1)
        return ans
