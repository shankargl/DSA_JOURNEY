class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pre=0
        for i in nums:
            pre+=i
        now=0
        for j in range(len(nums)):
            if now==pre-now-nums[j]:
                return j
            now+=nums[j]
        return -1