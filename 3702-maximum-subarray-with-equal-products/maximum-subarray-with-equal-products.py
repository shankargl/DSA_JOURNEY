from math import gcd
class Solution:
    def maxLength(self, nums: List[int]) -> int:
        N=len(nums)
        ans=float('-inf')
        for i in range(N):
            gcdd=nums[i]
            lcm=nums[i]
            prod=nums[i]
            for j in range(i+1,N):
                    gcdd=gcd(gcdd,nums[j])
                    lcm=((lcm*nums[j])//gcd(lcm,nums[j]))
                    prod*=nums[j]

                    if prod==(gcdd*lcm):
                        ans=max(ans,j-i+1)
        return ans