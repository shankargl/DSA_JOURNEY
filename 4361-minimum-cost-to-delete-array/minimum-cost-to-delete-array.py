class Solution:
    def minCost(self, nums):
        n = len(nums)

        nums[1:n-1] = sorted(nums[1:n-1])

        curr = 0
        ans = 0

        for i in range(2, n-1, 2):
            curr += nums[i] + nums[i-1]
            ans = min(ans, curr)

        return ans + nums[0] + nums[n-1]