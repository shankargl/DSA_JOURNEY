class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        count=[0]*26

        for i in s:
            new=ord(i)-ord('a')
            count[new]+=1

        for j in target:
            now=ord(j)-ord('a')
            count[now]-=1

        n=len(target)
        
        for k in range(n-1,-1,-1):
            cnt=ord(target[k])-ord('a')

            count[cnt]+=1

            if any(x<0 for x in count):
                continue
            nxt=-1
            for ch in range(cnt+1,26):
                if count[ch]:
                    nxt=ch
                    break
            if nxt==-1:
                continue

            count[nxt]-=1
            ans=list(target[:k])
            ans.append(chr(nxt+ord('a')))

            for l in range(26):
                ans.extend(chr(l+ord('a'))*count[l])
            return ''.join(ans)
        return ''
