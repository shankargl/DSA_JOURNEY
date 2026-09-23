class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        total = sum(nums)
        target = total - x

        if target == 0:
            return len(nums)

        mp = {0: -1}
        pre = 0
        longest = -1

        for i in range(len(nums)):
            pre += nums[i]

            if pre - target in mp:
                longest = max(longest, i - mp[pre - target])

            if pre not in mp:
                mp[pre] = i

        if longest == -1:
            return -1

        return len(nums) - longest