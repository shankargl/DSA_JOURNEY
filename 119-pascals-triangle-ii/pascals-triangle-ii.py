class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        ans=[]
        for i in range(rowIndex+1):
            raw=[1]*(i+1)
            for j in range(1,i):
                raw[j]=ans[i-1][j-1]+ans[i-1][j]
            ans.append(raw)

        return ans[-1]