class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        result = False
        n = len(word)
        if n == 1:
            return True

        if word[0] == word[0].upper():
            if word[1:] == word[1:].upper() or word[1:] == word[1:].lower():
                result = True
        elif word[0] == word[0].lower():
            if word[1:] == word[1:].lower():
                result = True

        return result

# word = "USA" # True
# word = "FlaG" # False
# word = "FooFo" # False
# Solution().detectCapitalUse(word)
