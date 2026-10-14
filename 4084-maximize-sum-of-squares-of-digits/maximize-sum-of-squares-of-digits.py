class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if num*9<sum:
            return ""
        if sum<9:
            zeros=num-1
            ans=str(sum)
            for _ in range(zeros):
                ans+='0'

            return ans
        
        res=["9"]
        total=9
        num-=1
        while num>0:
            new=sum-total
            if new==0:
                res.append(str(0))
            elif new<9:
                res.append(str(new))
                total+=new
            else:
                res.append(str(9))
                total+=9

            num-=1
        return "".join(res)