class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        def check(nums,speed):
            total=0
            for i in range(len(piles)):
                total+=ceil(piles[i]/speed)
            return total
        l=1
        r=max(piles)
        ans=1
        while l<=r:
            mid=(l+r)//2
            new=check(piles,mid)
            if new<=h:
                ans=mid
                r=mid-1
            else:
                l=mid+1
        return ans
