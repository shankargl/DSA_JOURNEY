class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        ans=0
        l=0
        mp={}
        for i in range(len(fruits)):
            mp[fruits[i]]=mp.get(fruits[i],0)+1
            while len(mp)>2:
                mp[fruits[l]]-=1
                if mp[fruits[l]]==0:
                    del mp[fruits[l]]
                l+=1
            ans=max(ans,i-l+1)
        return ans