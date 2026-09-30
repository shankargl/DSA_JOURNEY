class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
    
        ans=0
        w=numBottles
        while w>=numExchange:
            new=floor(w/numExchange)
            ans+=new
            w=w-(new*numExchange)+new
        return ans+numBottles
