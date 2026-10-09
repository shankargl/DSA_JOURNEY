class Solution:
    def minInsertions(self, s: str) -> int:
        res = 0
        st = []
        new_s = []
        
        cnt = 0
        for c in s:
            if c == '(':
                if cnt == 1:
                    new_s.append(')')
                    res += 1
                new_s.append(c)
                cnt = 0
            else:
                cnt += 1
                if cnt == 2:
                    new_s.append(')')
                    cnt = 0
        if cnt == 1:
            res += 1
            new_s.append(')')

        s = new_s
        for c in s:
            if c == ')':
                if not st:
                    res += 1
                else: st.pop()    
            else:
                st.append(c)

        return res + 2 * len(st)

