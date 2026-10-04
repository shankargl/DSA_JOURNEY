class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        ele1=0
        ele2=0
        count1=0
        count2=0
        for i in range(len(nums)):
            if count1==0 and nums[i]!=ele2:
                ele1=nums[i]
                count1=1
            elif count2==0 and nums[i]!=ele1:
                ele2=nums[i]
                count2=1

            elif nums[i]==ele1:
                count1+=1
            elif nums[i]==ele2:
                count2+=1
            else:
                count1-=1
                count2-=1

        ans=[]
        res1=0
        res2=0
        for num in nums:
            if num==ele1:
                res1+=1
            elif num==ele2:
                res2+=1

        if res1>(len(nums)//3):
            ans.append(ele1)
        if res2>(len(nums)//3):
            ans.append(ele2)
        return ans
        
        
            