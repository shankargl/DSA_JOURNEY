class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        ans=0
        N=len(nums)
        for i in range(N):
            arr=set()
            for j in range(i,N):
                arr.add(nums[j])
                ans+=len(arr)*len(arr)

        return ans