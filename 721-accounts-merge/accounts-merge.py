class DSU:
    def __init__(self,n):
        self.parent=[i for i in range(n)]
        self.rank=[0]*n
        
    def find(self,x):
        if self.parent[x]==x:
            return x
        self.parent[x]=self.find(self.parent[x])
        return self.parent[x]

    def union(self,a,b):
        pa=self.find(a)
        pb=self.find(b)
        if pa==pb:
            return
        if self.rank[pa]<self.rank[pb]:
            self.parent[pa]=pb
        elif self.rank[pa]>self.rank[pb]:
            self.parent[pb]=pa
        else:
            self.parent[pb]=pa
            self.rank[pa]+=1 

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        N=len(accounts)
        dsu=DSU(N)
        mp={}
        for i in range(N):
            for j in range(1,len(accounts[i])):
                mail=accounts[i][j]
                if mail not in mp:
                    mp[mail]=i
                else:
                    dsu.union(i,mp[mail])
        ans=[[] for _ in range(N)]
        for mail,inx in mp.items():
            node=dsu.find(inx)
            ans[node].append(mail)
        result=[]
        for i in range(N):
            if not ans[i]:
                continue
            ans[i].sort()
            name=[accounts[i][0]]
            for j in ans[i]:
                name.append(j)
            result.append(name)
        result.sort()
        return result
        