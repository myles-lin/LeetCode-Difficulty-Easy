class Solution:
    def checkRecord(self, s: str) -> bool:
        absent = 0
        late = 0
        for i in s:
            if i == 'A':
                absent += 1
                late = 0
            elif i == 'L':
                late += 1
            else:
                late = 0

            if absent > 1 or late >= 3:
                    return False
        return True

# s = "PPALLP" # Output: true
# s = "PPALLL" #Output: false
# Solution().checkRecord(s)
