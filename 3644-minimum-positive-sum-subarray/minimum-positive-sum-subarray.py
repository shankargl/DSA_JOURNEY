class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        ans=float('inf')
        N=len(nums)
        for i in range(N):
            arr=[]
            for j in range(i,N):
                arr.append(nums[j])
                if len(arr)>=l and len(arr)<=r:
                    if sum(arr)>0:
                        ans=min(ans,sum(arr))

                elif len(arr)>r:
                    break

        return -1 if ans==float('inf') else ans