class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        answer = set()
        for word in words:
            word_morse = ''
            for i in word:
                word_morse += morse[ord(i) - 97]
            answer.add(word_morse)
        return len(answer)

# words = ["gin","zen","gig","msg"] # Output: 2
# words = ["a"] # Output: 1
# Solution().uniqueMorseRepresentations(words)
