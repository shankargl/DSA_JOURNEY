class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def topo(n,edge):
            graph=[[] for _ in range(n)]
            indegree=[0]*n
            for u,v in edge:
                graph[v].append(u)
                indegree[u]+=1

            q=deque()
            for i in range(n):
                if indegree[i]==0:
                    q.append(i)
            ans=[]
            while q:
                node=q.popleft()
                ans.append(node)
                for nei in graph[node]:

                    indegree[nei]-=1

                    if indegree[nei]==0:
                        q.append(nei)
            if len(ans)!=n:
                return []
            return ans

        return topo(numCourses,prerequisites)