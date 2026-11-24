class Solution:
    def maxDistance(self, arrays: list[list[int]]) -> int:
       
        N=len(arrays)
        mn=arrays[0][0]
        mx=arrays[0][-1]
        res=float('-inf')
        for i in range(1,N):
            arr=arrays[i]
            cn1=abs(arrays[i][-1]-mn)
            cn2=abs(arrays[i][0]-mx)
            res=max(res,cn1,cn2)

            mn=min(mn,arr[0])
            mx=max(mx,arr[-1])

        return res
            


          
