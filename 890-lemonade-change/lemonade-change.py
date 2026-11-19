class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        nfive=0
        nten=0
        for i in range(len(bills)):
            if bills[i]==5:
                nfive+=1
            elif bills[i]==10:
                if nfive>=1:
                    nfive-=1
                    nten+=1
                    continue
                else:
                    return False

            else:
                if (nfive>=1 and nten>=1):
                    nfive-=1
                    nten-=1
                elif nfive>=3:
                    nfive-=3

                else:
                    return False

        return True
