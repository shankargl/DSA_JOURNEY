class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        n=len(s)
        mp={}
        for i, j in knowledge:
            mp[i]=j
        ans=""
        q=deque()
        ok=0
        for i in range(n):
            if s[i]=='(':
                ok=1
                continue
            elif s[i]==')':
                new=''
                while q:
                    new+=q.popleft()
                ok=0
                if new not in mp:
                    ans+='?'
                else:
                    ans+=mp[new]
                continue
            if ok==1:
                q.append(s[i])
            else:
                ans+=s[i]
        return ans

            