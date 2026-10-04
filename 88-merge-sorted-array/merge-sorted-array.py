class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        sum1=m-1
        sum2=n-1
        sum3=len(nums1)-1
        while sum2>=0:
            if sum1>=0 and nums1[sum1]>nums2[sum2]:
                nums1[sum3]=nums1[sum1]
                sum1-=1
            else:
                nums1[sum3]=nums2[sum2]
                sum2-=1

            sum3-=1
    
                