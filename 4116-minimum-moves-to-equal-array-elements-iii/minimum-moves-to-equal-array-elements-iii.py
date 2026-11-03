class Solution:
    def minMoves(self, nums: List[int]) -> int:
        mx=max(nums)
        ans=0
        for i in range(len(nums)):
            ans+=mx-nums[i]

        return ans