class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        xor = nums[0]

        for i in range(1, len(nums)):
            xor ^= nums[i]
        if xor > 0:
            return len(nums)

        remain = xor
        for l in range(len(nums)):
            remain = xor ^ nums[l]
            if remain > 0:
                return len(nums) - 1

        return 0