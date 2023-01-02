class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for i in s:
            if i in brackets.keys():
                stack.append(i)
            elif len(stack) == 0:
                return False
            elif i == brackets[stack[-1]]:
                stack.pop(-1)
            else:
                return False

        if len(stack) == 0:
            return True

        return False

# s = "()[]{}" # True
# s = "(]" # False
# s = "(])" # False
# Solution().isValid(s)
