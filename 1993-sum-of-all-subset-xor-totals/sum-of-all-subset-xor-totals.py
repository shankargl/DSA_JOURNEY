class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans=0
        def subsets(arr, index, current):
            nonlocal ans
            if index == len(arr):
                xor=0
                for i in current:
                    xor^=i
                ans+=xor
                return
            current.append(arr[index])
            subsets(arr, index + 1, current)

            current.pop()

            subsets(arr, index + 1, current)
        subsets(nums,0,[])
        return ans