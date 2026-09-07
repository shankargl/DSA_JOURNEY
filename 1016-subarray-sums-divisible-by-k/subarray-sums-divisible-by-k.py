class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        pre=0
        mp={}
        ans=0
        for i in range(len(nums)):
            pre+=nums[i]
            s=pre%k
            if s==0:
                ans+=1
            if s in mp:
                ans+=mp[s]
            mp[s]=mp.get(s,0)+1
        return ans