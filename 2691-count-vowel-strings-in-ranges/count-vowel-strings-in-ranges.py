class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        N=len(words)
        prefix=[0]*(N+1)
        seen={'a','e','i','o','u'}

        for i in range(N):
            word=words[i]
            if word[0] in seen and word[-1] in seen:
                prefix[i+1]=prefix[i]+1

            else:
                prefix[i+1]=prefix[i]

        ans=[]
        for que in queries:
            a,b=que
            ans.append(prefix[b+1]-prefix[a])

        return ans
