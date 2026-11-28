class Solution:
    def partitionString(self, s: str) -> int:
        N=len(s)
        ans=0
        seen=set()     #O(n)-space
        for i in range(N):   #O(n)-time
            if s[i] not in seen:
                seen.add(s[i])
            else:
                ans+=1
                seen.clear()
                seen.add(s[i])
            #print(seen,ans)
        if len(seen)>0:
            ans+=1
        return ans