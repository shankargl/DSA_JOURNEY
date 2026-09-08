class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans=nums[0]
        pre=0
        suf=0
        n=len(nums)
        for i in range(n):
            if pre==0:
                pre=1
            if suf==0:
                suf=1

            pre=pre*nums[i]
            suf=suf*nums[n-i-1]
            ans=max(ans,pre,suf)
        return ans
