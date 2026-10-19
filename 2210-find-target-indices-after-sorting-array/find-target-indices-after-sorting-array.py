class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        
        def lower():
            ans=-1
            l=0
            r=len(nums)-1
            while l<=r:
                mid=(l+r)//2

                if nums[mid]==target:
                    ans=mid
                    r=mid-1

                elif nums[mid]>target:
                    r=mid-1

                else:
                    l=mid+1

            return ans

        def upper():
            ans=-1
            l=0
            r=len(nums)-1
            while l<=r:
                mid=(l+r)//2

                if nums[mid]==target:
                    ans=mid
                    l=mid+1

                elif nums[mid]>target:
                    r=mid-1

                else:
                    l=mid+1

            return ans


        fir=lower()
        sec=upper()
        if fir==-1 and sec==-1:
            return []
        res=[]
        for i in range(fir,sec+1):
            res.append(i)

        return res