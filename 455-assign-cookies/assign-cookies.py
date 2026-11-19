class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        #greedy algorithm
        g.sort()
        s.sort()

        count=0
        i=0
        l=0
        while i<len(s):
            if l<len(g) and s[i]>=g[l]:
                count+=1
                l+=1
            i+=1

        return count
