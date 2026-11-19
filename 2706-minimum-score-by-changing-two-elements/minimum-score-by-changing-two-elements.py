class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        # we need to choose two elements like 

        N=len(nums)
        if N==3:
            return 0
        nums.sort()
        n1=abs(nums[2]-nums[-1])
        n2=abs(nums[-3]-nums[0])
        n3=abs(nums[-2]-nums[1])
        return min(n1,n2,n3)
