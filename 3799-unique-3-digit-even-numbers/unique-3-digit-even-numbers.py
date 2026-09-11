class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        seen=set()
        N=len(digits)
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    if i==j or j==k or i==k or digits[k]%2==1 or digits[i]==0:
                        continue
                    new=digits[i]*100+digits[j]*10+digits[k]
                    seen.add(new)
        return len(seen)