class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        N=len(nums)
        ans=[-1]*N
        stack=[]
        for i in range(N*2-1,-1,-1):
            while stack and stack[-1]<=nums[i%N]:
                stack.pop()

            if stack:
                ans[i%N]=stack[-1]

            stack.append(nums[i%N])

        return ans
            
