class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        l=0
        ans=0
        cur_sum=0
        mp={}
        for i in range(len(nums)):
            mp[nums[i]]=mp.get(nums[i],0)+1
            cur_sum+=nums[i]
            while mp[nums[i]]>1:
                mp[nums[l]]-=1
                cur_sum-=nums[l]
                if mp[nums[l]]==0:
                    del mp[nums[l]]
                l+=1
            if len(mp)==k:
                ans=max(ans,cur_sum)
                mp[nums[l]]-=1
                cur_sum-=nums[l]
                if mp[nums[l]]==0:
                    del mp[nums[l]]
                l+=1
        return ans