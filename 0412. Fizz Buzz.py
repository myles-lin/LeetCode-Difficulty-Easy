# Runtime 83 ms, Memory 15.1 MB
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        lst = [None] * n
        for i in range(1, n + 1):
            if i % 15 == 0:
                lst[i-1] = "FizzBuzz"
            elif i % 3 == 0:
                lst[i-1] = "Fizz"
            elif i % 5 == 0:
                lst[i-1] = "Buzz"
            else:
                lst[i-1] = str(i)
        return lst

# Runtime 75 ms, Memory 14.6 MB
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        return ("Fizz"*(i%3==0) + "Buzz"*(i%5==0) or f"{i}" for i in range(1, n+1))

# Input: n = 15
# Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
# Solution().fizzBuzz(n)
