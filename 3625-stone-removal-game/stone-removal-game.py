class Solution:
    def canAliceWin(self, n: int) -> bool:
        i=10
        player='Alice'
        while n>=i:
            if n>=i:
                n-=i
                player='Bob' if player=="Alice" else "Alice"
            i-=1

        return True if player=='Bob' else False
