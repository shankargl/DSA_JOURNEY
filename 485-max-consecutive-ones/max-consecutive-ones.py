class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans=0
        l=0
        for i in range(len(nums)):
            if nums[i]==0:
                l=i+1
            else:
                ans=max(ans,i-l+1)
        return ans
                