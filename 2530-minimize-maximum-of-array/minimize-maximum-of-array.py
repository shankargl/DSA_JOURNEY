class Solution:
    def minimizeArrayValue(self, nums: list[int]) -> int:
        N=len(nums)
        ans=nums[0]
        total=nums[0]
        for i in range(1,N):
            total+=nums[i]
            new=ceil(total/(i+1))
            ans=max(ans,new)

        return ans