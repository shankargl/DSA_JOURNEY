class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        pre=[1]*(n+1)
        suf=[1]*(n+1)
        for i in range(len(nums)):
            pre[i+1]=pre[i]*nums[i]
        for j in range(n-1,-1,-1):
            suf[j]=suf[j+1]*nums[j]
        ans=[]
        for k in range(n):
            ans.append(suf[k+1]*pre[k])
        return ans