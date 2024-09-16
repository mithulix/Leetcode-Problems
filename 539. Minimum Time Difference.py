from typing import List

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutesConvert = []
        for time in timePoints:
            t = time.split(":")
            minutes = int(t[0]) * 60 + int(t[1])
            minutesConvert.append(minutes)
        minutesConvert.sort()
        res = float("inf")

        left, right = 0, 1
        while right < len(minutesConvert): 
            res = min(res, minutesConvert[right] - minutesConvert[left])
            left += 1
            right += 1
        left = 0
        right = len(minutesConvert) - 1
        res = min(res, 1440 - minutesConvert[right] + minutesConvert[left])

        return res

# Sample usage
sol = Solution()
timePoints = ["23:59", "00:00", "12:34"]
print(sol.findMinDifference(timePoints))  # This will print the result
