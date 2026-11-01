class Solution:
    def minMoves(self, nums: list[int]) -> int:
        nums.sort()
        ele=nums[0]
        ans=0
        for i in range(len(nums)):
            ans+=abs(ele-nums[i])
        return ans