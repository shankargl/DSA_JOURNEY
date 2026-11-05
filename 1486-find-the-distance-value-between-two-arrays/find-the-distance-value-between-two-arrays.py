class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        arr2.sort()
        def binary(val, arr2, d):
            l = 0
            r = len(arr2) - 1

            while l <= r:
                mid = (l + r) // 2

                if arr2[mid] < val - d:
                    l = mid + 1
                elif arr2[mid] > val + d:
                    r = mid - 1
                else:
                    return True

            return False

        res = 0

        for i in range(len(arr1)):
            if not binary(arr1[i], arr2, d):
                res += 1

        return res