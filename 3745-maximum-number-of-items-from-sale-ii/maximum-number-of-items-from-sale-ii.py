class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        
        n = len(items)

        # Step 1: Count occurrences of each factor
        count = [0] * (n + 1)

        for factor, price in items:
            count[factor] += 1

        # Step 2: Calculate free item opportunities
        gain = [0] * (n + 1)

        for i in range(1, n + 1):
            total = 0

            for j in range(i, n + 1, i):
                total += count[j]

            gain[i] = total - 1

        # Step 3: Find minimum price
        min_price = min(price for factor, price in items)

        # Step 4: Build min heap
        heap = []

        for factor, price in items:
            if gain[factor] > 0 and price < 2 * min_price:
                heapq.heappush(heap, (price, gain[factor]))

        # Step 5: Greedy selection
        ans = 0

        while heap:
            price, copies = heapq.heappop(heap)

            if budget < price:
                break

            take = min(copies, budget // price)

            budget -= take * price
            ans += take * 2

        # Step 6: Buy remaining cheapest items
        ans += budget // min_price

        return ans
