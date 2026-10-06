class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        arr=[]
        for i in range(m):
            arr.append(nums1[i])
        
        for j in range(n):
            arr.append(nums2[j])

        arr.sort()

        for k in range(len(nums1)):
            nums1[k]=arr[k]
            