class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:

        ans = ''
        l = 0
        mp = {}

        for i in range(len(s)):

            mp[s[i]] = mp.get(s[i], 0) + 1

            if mp.get('1', 0) >= k:

                while mp.get('1', 0) >= k:

                    new = s[l:i+1]

                    if len(ans) == 0:
                        ans = new

                    if len(new) < len(ans):
                        ans = new

                    elif len(new) == len(ans) and new < ans:
                        ans = new

                    mp[s[l]] -= 1

                    if mp[s[l]] == 0:
                        del mp[s[l]]

                    l += 1

        return ans