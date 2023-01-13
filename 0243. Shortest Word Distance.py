class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        dist = float('inf')
        index_1, index_2 = None, None

        for i in range(len(words)):
            if words[i] == word1:
                index_1 = i
            elif words[i] == word2:
                index_2 = i
            
            if index_1 != None and index_2 != None:
                dist = min(dist, abs(index_1 - index_2))

        return dist

# words = ['practice', 'makes', 'perfect', 'coding', 'makes']
# word1, word2 = "coding", "practice" # Output: 3
# word1, word2 = "makes", "coding" # Output: 1
# Solution().shortestDistance(words, word1, word2)
