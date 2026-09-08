class Solution:
    def countCommas(self, n: int) -> int:
        if n==100000:
            return 99001
        if len(str(n))<4:
            return 0
        w=len(str(n))//3
        total=n-1000
        return w*total+1