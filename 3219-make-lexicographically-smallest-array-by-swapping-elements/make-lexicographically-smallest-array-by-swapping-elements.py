from collections import defaultdict

class DSU:

    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):

        if self.parent[x] == x:
            return x

        self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, a, b):

        rootA = self.find(a)
        rootB = self.find(b)

        if rootA == rootB:
            return

        if self.size[rootA] < self.size[rootB]:
            rootA, rootB = rootB, rootA

        self.parent[rootB] = rootA
        self.size[rootA] += self.size[rootB]


class Solution:
    def lexicographicallySmallestArray(self, nums, limit):

        n = len(nums)

        dsu = DSU(n)

        arr = []

        for i in range(n):
            arr.append((nums[i], i))

        arr.sort()
        for i in range(1, n):

            if arr[i][0] - arr[i - 1][0] <= limit:
                dsu.union(arr[i][1], arr[i - 1][1])

        
        groups = defaultdict(list)

        for i in range(n):
            root = dsu.find(i)
            groups[root].append(i)

        ans = nums[:]

        for indices in groups.values():

            values = [nums[i] for i in indices]

            indices.sort()
            values.sort()

            for i in range(len(indices)):
                ans[indices[i]] = values[i]

        return ans
        