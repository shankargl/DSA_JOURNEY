class DisjointSet:
    def __init__(self, n):
        self.rank = [0] * (n + 1)
        self.parent = [i for i in range(n + 1)]
        self.size = [1] * (n + 1)
    
    
    def findUPar(self, node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.findUPar(self.parent[node])
        return self.parent[node]
    
  
    def unionByRank(self, u, v):
        ulp_u = self.findUPar(u)
        ulp_v = self.findUPar(v)
        if ulp_u == ulp_v:
            return
        if self.rank[ulp_u] < self.rank[ulp_v]:
            self.parent[ulp_u] = ulp_v
        elif self.rank[ulp_v] < self.rank[ulp_u]:
            self.parent[ulp_v] = ulp_u
        else:
            self.parent[ulp_v] = ulp_u
            self.rank[ulp_u] += 1
    def unionBySize(self, u, v):
        ulp_u = self.findUPar(u)
        ulp_v = self.findUPar(v)
        if ulp_u == ulp_v:
            return
        if self.size[ulp_u] < self.size[ulp_v]:
            self.parent[ulp_u] = ulp_v
            self.size[ulp_v] += self.size[ulp_u]
        else:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_u] += self.size[ulp_v]
    
    def getSize(self, node):
        return self.size[self.findUPar(node)]

class Solution:
    delRow = [-1, 0, 1, 0]
    delCol = [0, 1, 0, -1]
 
    def isValid(self, i, j, n):

        if i < 0 or i >= n:
            return False
        if j < 0 or j >= n:
            return False
        
        return True
    
 
    def addInitialIslands(self, grid, ds, n):
       
        for row in range(n):
            for col in range(n):
                
                if grid[row][col] == 0:
                    continue
                
                for ind in range(4):
                    newRow = row + self.delRow[ind]
                    newCol = col + self.delCol[ind]
                    
                    if (self.isValid(newRow, newCol, n) and 
                        grid[newRow][newCol] == 1):

                        nodeNo = row * n + col
                        adjNodeNo = newRow * n + newCol
                        
                        ds.unionBySize(nodeNo, adjNodeNo)

    def largestIsland(self, grid):
        n = len(grid)
        
        ds = DisjointSet(n * n)

        self.addInitialIslands(grid, ds, n)
        
        ans = 0
        
        for row in range(n):
            for col in range(n):

                if grid[row][col] == 1:
                    continue
                
                components = set()
                
                for ind in range(4):
                    newRow = row + self.delRow[ind]
                    newCol = col + self.delCol[ind]
                    
                    if (self.isValid(newRow, newCol, n) and 
                        grid[newRow][newCol] == 1):
            
                        nodeNumber = newRow * n + newCol
                        components.add(ds.findUPar(nodeNumber))
                
                sizeTotal = 0
                
                for parent in components:
                    sizeTotal += ds.getSize(parent)
                
                ans = max(ans, sizeTotal + 1)
        
        for cellNo in range(n * n):
            ans = max(ans, ds.getSize(cellNo))
        
        return ans
