class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split()
        return len(s[-1])
    
# s = "Hello World" # answer = 5
# s = "   fly me   to   the moon  " # answer = 4
# s = "luffy is still joyboy" # answer = 6
# Solution().lengthOfLastWord(s)
