class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        sumi=0
        digit=0
        for i in nums:
            sumi+=i
            digit+=sum([int(j) for j in str(i)])
        print(sumi)
        return sumi-digit