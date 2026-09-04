class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        if len(nums)==1:
            return 0
        for i in range(len(nums)):
            mx=max(nums[:i+1])
            mn=min(nums[i:])
            
            if mx-mn<=k:
                return i
        return -1