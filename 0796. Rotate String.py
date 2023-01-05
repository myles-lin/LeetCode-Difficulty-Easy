class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i in range(0, len(s)):
            shift_s = s[i:] + s[:i]
            if shift_s == goal:
                return True
        return False

# s, goal = "abcde", "cdeab" # Output: true
# s, goal = "abcde", "abced" # Output: false
# Solution().rotateString(s, goal)
