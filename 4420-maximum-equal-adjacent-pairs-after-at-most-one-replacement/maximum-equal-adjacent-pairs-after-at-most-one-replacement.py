class Solution:
    def maxEqualAdjacentPairs(self, nums: list[int]) -> int:
        N=len(nums)
        if N==2:
            return 1
        freq=defaultdict(int)
        count=0
        for i in range(N-1):
            a=nums[i]
            b=nums[i+1]
            if a>b:
                a,b=b,a
            if a==b:
                count+=1
            else:
                freq[(a,b)]+=1
        ans=count
        for fre,val in freq.items():
            ans=max(ans,count+val)
        return ans