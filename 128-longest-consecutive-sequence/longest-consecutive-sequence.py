class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        mp={}
        for i in range(len(nums)):
            mp[nums[i]]=mp.get(nums[i],0)+1

        new=dict(sorted(mp.items(),key=lambda x:x[0]))

        ans=0
        count=1
        for i,j in new.items():
            if i+1 not in mp: 
                ans=max(ans,count)
                count=1
                continue
            count+=1
        return ans
            