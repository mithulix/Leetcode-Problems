class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        # helper function to check if a given word can be formed by concatenating
        # two or more words in the input list
        def can(word, define):
            for i in range(1, len(word)):
                # check the left part of the word
                left = word[:i]
                # check the right part of the word
                right = word[i:]
                if left in define:
                    # if left part of the word is in the input set, check if the right part is in the set
                    # or can be formed by concatenating other words in the set
                    if right in define or can(right, define):
                        return True
            return False
        # initialize an empty list to store concatenated words
        res = []
        # create a set of all words from the input list to improve lookup time
        define = set(list(words))
        for word in words:
            # check if the word can be formed by concatenating other words in the set
            if can(word, define):
                # if it can, add it to the list of concatenated words
                res.append(word)

        return res
