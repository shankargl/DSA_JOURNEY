class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<=0:
            return 0
        if len(nums)==1:
            if nums[0]<k:
                return 1
            else:
                return 0
        if len(nums)==2:
            ans=0
            if nums[0]*nums[1]<k:
                ans+=1
            if nums[0]<k:
                ans+=1
            if nums[1]<k:
                ans+=1
            return ans
                
        count=0
        prod=1
        l=0
        for i in range(len(nums)):
            prod*=nums[i]

            while prod>=k:
                prod//=nums[l]
                l+=1
            count+=(i-l+1)
        return count