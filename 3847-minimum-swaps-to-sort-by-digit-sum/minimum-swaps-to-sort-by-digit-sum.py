
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        mp = {}

        for i in range(len(nums)):
            total = 0
            temp = nums[i]

            while temp > 0:
                total += temp % 10
                temp //= 10

            mp[i] = total

        arr = sorted(mp.items(), key=lambda x: (x[1], nums[x[0]]))

        res = [(nums[arr[i][0]], arr[i][0]) for i in range(len(arr))]

        visited = [False] * len(nums)
        swap = 0

        for i in range(len(nums)):
            if visited[i] or res[i][1] == i:
                continue

            cycle_no = 0
            j = i

            while not visited[j]:
                visited[j] = True
                cycle_no += 1
                j = res[j][1]

            if cycle_no > 1:
                swap += cycle_no - 1

        return swap
