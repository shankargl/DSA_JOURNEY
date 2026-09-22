class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        def pali(l,r):
            if l>r:
                return True
            if not s[l].isalnum():
                return pali(l+1,r)

            if not s[r].isalnum():
                return pali(l,r-1)
                
            if s[l]!=s[r]:
                return False
            return pali(l+1,r-1)
        return pali(0,len(s)-1)
                    
