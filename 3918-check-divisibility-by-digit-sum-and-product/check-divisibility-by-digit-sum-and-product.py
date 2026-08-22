class Solution:
    def checkDivisibility(self, n: int) -> bool:
        sumi=0
        pro=1
        w=n
        while w:
            digit=w%10
            sumi+=digit
            pro*=digit
            w//=10
        return n%(sumi+pro)==0