class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        mp={0:-1}
        pre=0
        for i in range(len(nums)):
            pre+=nums[i]
            s=pre%k
            if s in mp:
                if i-mp[s]>=2:
                    return True
            else:
                mp[s]=i
        return False