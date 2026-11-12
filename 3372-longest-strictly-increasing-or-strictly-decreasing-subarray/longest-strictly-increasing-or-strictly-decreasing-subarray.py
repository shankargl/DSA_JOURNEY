class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        N=len(nums)
        ans=float('-inf')
        for i in range(N):
            arr=[nums[i]]
            for j in range(i+1,N):
                if len(arr)==1:
                    if nums[j]!=arr[-1]:
                        arr.append(nums[j])
                    else:
                        break
                else:
                    if arr[-2]<nums[j] and arr[-1]<nums[j] and arr[-1]>arr[-2]:
                        arr.append(nums[j])
                    elif arr[-2]>nums[j] and arr[-1]>nums[j] and arr[-1]<arr[-2]:
                        arr.append(nums[j])
                    else:
                        ans=max(ans,len(arr))
                        break

            ans=max(ans,len(arr))

        return ans

                
