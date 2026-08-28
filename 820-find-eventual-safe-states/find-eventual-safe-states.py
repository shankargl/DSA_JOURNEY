class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n=len(graph)
        def topo(n,edge):
            new=[[] for i in range(n)]
            inde=[0]*n
            for j in range(n):
                for k in edge[j]:
                    new[k].append(j)
                    inde[j]+=1
            q=deque()
            for i in range(n):
                if inde[i]==0:
                    q.append(i)

            ans=[]
            while q:
                node=q.popleft()
                ans.append(node)
                for nei in new[node]:
                    inde[nei]-=1
                    if inde[nei]==0:
                        q.append(nei)
            return sorted(ans)
        return topo(n,graph)
