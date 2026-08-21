class Solution:
    def minimumSum(self, num: int) -> int:
        total=[]
        while num>0:
            total.append(num%10)
            num//=10
        total.sort()
        ans=0
        ans+=(total[0]*10)+total[2]
        ans+=(total[1]*10)+total[3]
        return ans
