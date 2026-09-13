class Solution:
    def maxProduct(self, words: List[str]) -> int:
        arr = []
        
        for word in words:
            arr.append((len(word), Counter(word), word))
        
        ans = 0
        
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if not (arr[i][1].keys() & arr[j][1].keys()):
                    ans = max(ans, arr[i][0] * arr[j][0])
        
        return ans