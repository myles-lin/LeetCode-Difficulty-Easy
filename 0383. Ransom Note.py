class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for i in ransomNote:
            if i in magazine:
                magazine = magazine.replace(i, "", 1)
            else:
                return False
        return True

# ransomNote, magazine = "aa", "ab" # Output: False
# ransomNote, magazine = "aa", "aab" # Output: True
# Solution().canConstruct(ransomNote, magazine)
