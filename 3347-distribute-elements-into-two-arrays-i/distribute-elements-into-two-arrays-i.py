class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        nums1=[nums[0]]
        nums2=[nums[1]]
        l=2
        while l<len(nums):
            if nums1[-1]>nums2[-1]:
                nums1.append(nums[l])
                l+=1
            else:
                nums2.append(nums[l])
                l+=1
        return nums1+nums2

