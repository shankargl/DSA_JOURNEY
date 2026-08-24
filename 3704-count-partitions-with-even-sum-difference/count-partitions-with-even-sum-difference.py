class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        pre=[]
        sum=0
        for i in nums:
            sum+=i
            pre.append(sum)
        ans=0
        maxi=sum
        for j in range(len(nums)-1):
            if abs(pre[j]-(maxi-pre[j]))%2==0:
                ans+=1
        return ans
