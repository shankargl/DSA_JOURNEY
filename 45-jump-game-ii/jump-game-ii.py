class Solution:
    def jump(self, nums: list[int]) -> int:
        # maintane 2 pointer add seee how far you can go
        # after 2nd pointer started with first+1 
        # treversal upto n-1

        jump=0
        i=0
        l=0
        while l<len(nums)-1:
            far=float('-inf')
            for j in range(i,l+1):
                far=max(far,nums[j]+j)
            jump+=1

            i=l+1
            l=far

        return jump