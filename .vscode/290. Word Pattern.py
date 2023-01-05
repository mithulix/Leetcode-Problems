class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        array = s.split()
        if len(array) != len(pattern):
            return False
        
        for i in range(len(array)):
            if pattern.find(pattern[i]) != array.index(array[i]):
                return False
        return True