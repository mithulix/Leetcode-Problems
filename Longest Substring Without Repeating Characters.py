class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0
        max_length = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length

# Test case
solution = Solution()
print(solution.lengthOfLongestSubstring("abchiooohbb"))  # Output: 6
print(solution.lengthOfLongestSubstring("bbbbbujj"))     # Output: 3
print(solution.lengthOfLongestSubstring("pwwwwopowkew"))    # Output: 5

