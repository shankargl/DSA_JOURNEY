class DSU:
    def __init__(self,n):
        self.parent=[i for i in range(n)]
        self.rank=[0]*n
    def find(self,x):
        if self.parent[x]==x:
            return self.parent[x]
        self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    def union(self,a,b):
        py=self.find(a)
        pu=self.find(b)
        if py==pu:
            return 
        if self.rank[py]<self.rank[pu]:
            self.parent[py]=pu
        elif self.rank[py]>self.rank[pu]:
            self.parent[pu]=py
        else:
            self.parent[py]=pu
            self.rank[pu]+=1


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n=len(stones)
        dsu=DSU(n)

        for i in range(n):
            for j in range(i+1,n):
                if stones[i][0]==stones[j][0] or stones[i][1]==stones[j][1]:
                    dsu.union(i,j)


        connected=set()
        for i in range(n):
            connected.add(dsu.find(i))
        return n-len(connected)
