class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        #  mulitple each spells with all potion
        # use binary search to find number for potions
        # sort the potions to do binary search

        n=len(spells)
        m=len(potions)

        potions.sort()
        def binary_search(spell,potions,success):
            l=0
            r=len(potions)-1
            ans=-1
            while l<=r:
                mid=(l+r)//2
                if potions[mid]*spell>=success:
                    ans=mid
                    r=mid-1

                else:
                    l=mid+1

            return ans

        res=[]
        for i in spells:
            total=binary_search(i,potions,success)
            if total==-1:
                res.append(0)
            else:
                res.append(m-total)
        return res