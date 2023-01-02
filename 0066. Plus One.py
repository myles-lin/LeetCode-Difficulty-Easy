class Solution:
    def plusOne(self, digits: int) -> int:
        if digits[-1] != 9:
            digits[-1] += 1
        else:
            new_digits = ''
            for i in digits:
                new_digits += str(i)
                
            digits_int = int(new_digits) + 1
            digits = [int(i) for i in str(digits_int)]
        
        return digits
    
# lst = [1, 2, 3] # answer = [1, 2, 4]
# lst = [4, 3, 2, 1] # answer = [4, 3, 2, 2]
# lst = [9, 9] # answer = [1, 0, 0]
# Solution().plusOne(lst)
