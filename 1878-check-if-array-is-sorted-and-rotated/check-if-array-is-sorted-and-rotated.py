class Solution:
    def check(self, nums: list[int]) -> bool:
        N=len(nums)
        def check(count,ind):
            nonlocal N
            if ind==N:
                return True
            if nums[ind]>nums[(ind+1)%N]:
                count+=1
            if count>1:
                return False
            return check(count,ind+1)
        return check(0,0)
