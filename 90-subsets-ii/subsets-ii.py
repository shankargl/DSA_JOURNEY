class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans=[]
        def gen(ind,temp):
            nonlocal ans
            if ind==len(nums):
                ans.append(temp[:])
                return 
            temp.append(nums[ind])
            gen(ind+1,temp)
            temp.pop()
            w=ind+1
            while w<len(nums) and nums[w]==nums[w-1]:
                w+=1
            gen(w,temp)
        gen(0,[])
        return ans