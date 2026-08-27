class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        def dfs(n, add_list, vis):

            vis[n] = 1

            for i in add_list[n]:

                if vis[i] == 1:
                    return True

                if vis[i] == 0:
                    if dfs(i, add_list, vis):
                        return True

            vis[n] = 2

            return False

        add_list = [[] for _ in range(numCourses)]

        for u, v in prerequisites:
            add_list[v].append(u)

        vis = [0] * numCourses

        for i in range(numCourses):

            if vis[i] == 0:

                if dfs(i, add_list, vis):
                    return False

        return True
        