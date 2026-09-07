class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans=0
        cur=0
        mp={}
        for i in range(len(nums)):
            cur+=nums[i]
            s=cur-k
            if s==0:
                ans+=1
            if s in mp:
                ans+=mp[s]
            mp[cur]=mp.get(cur,0)+1
        return ans