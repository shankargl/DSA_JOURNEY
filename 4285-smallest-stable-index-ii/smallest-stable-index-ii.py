class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n=len(nums)
        pre=[0]*n
        suf=[0]*n
        pre[0]=nums[0]
        for i in range(1,n):
            pre[i]=max(pre[i-1],nums[i])
        suf[n-1]=nums[n-1]
        for j in range(n-2,-1,-1):
            suf[j]=min(suf[j+1],nums[j])

        for i in range(n):
            if pre[i]-suf[i]<=k:
                return i
        return -1