class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        ans=0
        for i in words:
            n=len(pref)
            if i[:n]==pref:
                ans+=1
        return ans