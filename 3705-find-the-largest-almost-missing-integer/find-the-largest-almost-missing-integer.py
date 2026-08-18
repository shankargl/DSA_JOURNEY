class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        if k==1:
            nums.sort()
            for i in range(len(nums)-1,-1,-1):
                if nums.count(nums[i])==1:
                    return nums[i]
            return -1

            
        if k==len(nums):
            return max(nums)

        first=nums[0]
        sec=nums[-1]
        count1=nums.count(first)
        count2=nums.count(sec)
        if count1==1 and count2==1:
            return max(first,sec)
        elif count1==1:
            return first
        elif count2==1:
            return sec
        else:
            return -1

        
        