class Solution:
    def calculateScore(self, a: int, b: int) -> int:
        def check(n):
            count=0
            while n>0:
                digit=n%2
                count+=1 if digit==1 else 0
                n//=2
            return count

        s1=check(a)
        s2=check(b)

        if s1>=s2:
            return s1*s2
        else:
            return s2//s1