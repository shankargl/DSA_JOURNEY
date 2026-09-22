class Solution:
    def largestOddNumber(self, num: str) -> str:
        l=0
        while int(num[l])==0:
            l+=1
        i=len(num)-1
        while i>=0 and int(num[i])%2==0:
            i-=1
        return num[l:i+1]