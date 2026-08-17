class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        odd=0
        even=0
        for  i in nums:
            if i<10:
                odd+=i
            else:
                even+=i
        return odd!=even