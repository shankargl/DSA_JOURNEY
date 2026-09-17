class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        N=len(arr)
        mp=[float('inf')]*N
        l=0
        cur=0
        ans=float('inf')
        for i in range(N):
            cur+=arr[i]
            while cur>target:
                cur-=arr[l]
                l+=1
            if cur==target:
                length=i-l+1
                if l>0 and mp[l-1]!=float('inf'):
                    ans=min(ans,length+mp[l-1])
            if i>0:
                mp[i]=mp[i-1]
            if cur==target:
                mp[i]=min(mp[i],i-l+1)
        return -1 if ans==float('inf ') else ans