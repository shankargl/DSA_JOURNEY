class Solution:
    def countTasks(self, tasks: List[int], shifts: List[int]) -> List[int]:
        prefix = []
        total = 0
        for task in tasks:
            total += task
            prefix.append(total)

        def upper_bound(completed: int) -> int:
            left = 0
            right = len(prefix) - 1
            ans = len(prefix)

            while left <= right:
                mid = left + (right - left) // 2

                if prefix[mid] > completed:
                    ans = mid
                    right = mid - 1
                else:
                    left = mid + 1

            return ans

        completed = 0
        ans = []

        for shift in shifts:
            completed += shift

            if completed >= prefix[-1]:
                ans.append(0)
                completed = 0        
                continue

            finished = upper_bound(completed)
            ans.append(len(tasks) - finished)

        return ans
