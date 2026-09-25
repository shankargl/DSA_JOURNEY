class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        ans=[]
        def subset(temp,ind):
            nonlocal ans
            if ind==len(nums):
                ans.append(temp[:])
                return
            temp.append(nums[ind])
            subset(temp,ind+1)
            temp.pop()
            subset(temp,ind+1)

        subset([],0)
        return ans