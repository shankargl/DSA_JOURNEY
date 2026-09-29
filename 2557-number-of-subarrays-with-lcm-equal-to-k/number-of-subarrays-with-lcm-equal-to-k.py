class Solution:
    def subarrayLCM(self, nums: list[int], k: int) -> int:
        def gcd(a,b):
            while b>0:
                a,b=b,a%b
            return a
        ans=0
        for i in range(len(nums)):
            lcm=1
            for j in range(i,len(nums)):
                lcm=(lcm*nums[j])//gcd(lcm,nums[j])
                if lcm==k:
                    ans+=1
                if lcm>k:
                    break
        return ans