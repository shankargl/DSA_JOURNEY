class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)

        first = 0
        second = 0
        count1 = 0
        count2 = 0

        for i in range(n):
            if i < n // 2:
                if num[i] == '?':
                    count1 += 1
                else:
                    first += int(num[i])

            else:
                if num[i] == '?':
                    count2 += 1
                else:
                    second += int(num[i])

        if count1 == 0 and count2 == 0:
            return first != second

        if count1 == count2:
            return first != second

        new = count1 + count2

        if new % 2 == 1:
            return True

        return 2 * (first - second) != 9 * (count2 - count1)