class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        maxi=max(nums)
        mini=min(nums)
        index1=nums.index(maxi)
        index2=nums.index(mini)
        ans=float('inf')
        if index1<index2:
            ans=min(ans,index2+1)
            ans=min(ans,(len(nums)-index1))
            ans=min(ans,((index1+1)+(len(nums)-index2)))
        else:
            ans=min(ans,index1+1)
            ans=min(ans,(len(nums)-index2))
            ans=min(ans,((index2+1)+(len(nums)-index1)))

        return ans