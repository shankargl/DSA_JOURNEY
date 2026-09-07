class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atmost(k):
            ans = 0
            l = 0
            mp = {}

            for i in range(len(nums)):

                mp[nums[i]] = mp.get(nums[i], 0) + 1

                while len(mp) > k:
                    mp[nums[l]] -= 1

                    if mp[nums[l]] == 0:
                        del mp[nums[l]]

                    l += 1

                
                ans += i - l + 1

            return ans

        return atmost(k) - atmost(k - 1)