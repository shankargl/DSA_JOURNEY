class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        ans = []
        n = len(digits)

        for i in range(n):
            if digits[i] == 0:
                continue

            for j in range(n):
                if j == i:
                    continue

                for k in range(n):
                    if k == i or k == j:
                        continue

                    temp = digits[i] * 100 + digits[j] * 10 + digits[k]

                    if temp % 2 == 0:
                        ans.append(temp)

        return sorted(set(ans))