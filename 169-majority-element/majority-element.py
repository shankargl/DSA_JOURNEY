class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        ele=0
        count=0
        for i in range(len(nums)):
            if count==0:
                count=1
                ele=nums[i]
            elif nums[i]==ele:
                count+=1
            else:
                count-=1
        return ele

       