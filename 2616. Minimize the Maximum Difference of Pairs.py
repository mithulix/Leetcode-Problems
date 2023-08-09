class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p == 0:
            return 0

        nums.sort()

        def gen():
            i = 1
            while i < len(nums):
                yield nums[i] - nums[i - 1]
                i += 1

        low, high = min(gen()), max(gen())
        while low <= high:
            mid = (low + high) // 2
            i, _p = 1, p
            while i < len(nums):
                if nums[i] - nums[i - 1] <= mid:
                    if (_p := _p - 1) == 0:
                        break
                    i += 1
                i += 1
            if _p == 0:
                high = mid - 1
            else:
                low = mid + 1
    
        return low
