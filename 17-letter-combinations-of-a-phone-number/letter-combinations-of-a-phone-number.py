class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        mp={
            2:'abc',3:'def',4:'ghi',5:'jkl',6:'mno',
            7:'pqrs',8:'tuv',9:'wxyz'
        }

        ans=[]
        def check(ind,path):
            nonlocal ans
            if len(path)==len(digits):
                ans.append(''.join(path))
                return

            for ch in mp[int(digits[ind])]:
                path.append(ch)
                check(ind+1,path)
                path.pop()

        check(0,[])
        return ans