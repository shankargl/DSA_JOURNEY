class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:

        def check(nums,cur):
            count=0
            for i in range(1,cur+1):
                if i not in nums:
                    count+=1
            return count
        l=1
        r=max(arr)+k
        while l<=r:
            mid=(l+r)//2
            total=check(arr,mid)
            if total<k:
                l=mid+1
            else:
                r=mid-1
        return l