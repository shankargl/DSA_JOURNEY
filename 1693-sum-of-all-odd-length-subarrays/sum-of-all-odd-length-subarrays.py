class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:

        pre=[0]*(len(arr)+1)
        N=len(arr)
        for i in range(N):
            pre[i+1]=pre[i]+arr[i]
        
        ans=sum(arr)
        r=1
        while r+2<len(pre):
            l=r
            while l+2<len(pre):
                ans+=pre[l+2]-pre[r-1]
                l+=2
            r+=1
        return ans
