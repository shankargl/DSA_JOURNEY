class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        ans=[]
        for i in range(numRows):
            raw=[1]*(i+1)
            for j in range(1,i):
                raw[j]=ans[i-1][j-1]+ans[i-1][j]
            ans.append(raw)
        return ans