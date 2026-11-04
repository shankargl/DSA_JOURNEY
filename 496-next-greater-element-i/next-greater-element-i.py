class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        N=len(nums2)
        mp={}
        stack=[]
        for i in range(N-1,-1,-1):
            while stack and stack[-1]<nums2[i]:
                stack.pop()
            if len(stack)==0:
                mp[nums2[i]]=-1
            else:
                mp[nums2[i]]=stack[-1]
            stack.append(nums2[i])
            

        for i in range(len(nums1)):
            nums1[i]=mp[nums1[i]]

        return nums1