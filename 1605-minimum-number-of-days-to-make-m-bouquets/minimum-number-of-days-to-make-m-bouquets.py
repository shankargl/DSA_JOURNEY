class Solution:
    def minDays(self, bloom: list[int], m: int, k: int) -> int:
        if m*k>len(bloom):
            return -1
        def bloomday(day):
            count=0
            bouqu=0
            for i in range(len(bloom)):
                if bloom[i]<=day:
                    count+=1
                    if count==k:
                        bouqu+=1
                        count=0
                else:
                    count=0
            return bouqu>=m

        l=min(bloom)
        r=max(bloom)
        ans=-1
        while l<=r:
            mid=(l+r)//2
            if bloomday(mid):
                ans=mid
                r=mid-1
            else:
                l=mid+1
        return ans
