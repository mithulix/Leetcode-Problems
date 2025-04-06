def lengthOfLongestSubstring(s: str) -> int:
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


# Test the function with some inputs
print(lengthOfLongestSubstring("abchiooohbb"))  # Output: 6
print(lengthOfLongestSubstring("bbbbbujj"))     # Output: 3
print(lengthOfLongestSubstring("pwwwwopowkew"))    # Output: 5