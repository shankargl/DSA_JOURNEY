class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        value=sum(nums2)-sum(nums1)
        return value//len(nums1)