class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            nums[i]=nums[i]*nums[i]
        nums.sort()
        ans=0
        N=len(nums)
        for i in range(0,N//2):
            ans-=nums[i]
        for j in range(N//2,N):
            ans+=nums[j]
        
        return ans