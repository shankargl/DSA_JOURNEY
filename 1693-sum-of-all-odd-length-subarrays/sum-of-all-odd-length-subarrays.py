class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        ans=0
        N=len(arr)
        for i in range(N):
            new=[]
            for j in range(i,N):
                new.append(arr[j])
                if len(new)%2==1:
                    ans+=sum(new)
        return ans