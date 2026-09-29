class Solution:
    def subarrayGCD(self, nums: list[int], k: int) -> int:

        def gcd(a,b):
            while b>0:
               a,b=b,a%b
            return a
            
        ans = 0

        for i in range(len(nums)):
            g=0
            for j in range(i, len(nums)):
                g=gcd(g,nums[j])
                if g==k:
                    ans+=1
                if g<k:
                    break
        
        return ans
