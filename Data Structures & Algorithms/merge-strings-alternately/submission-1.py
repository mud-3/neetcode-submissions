class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        position = 0
        merged = ""

        while position < len(word1) and position < len(word2):
            merged += word1[position] + word2[position]
            position += 1
        
        merged += word1[position:] or word2[position:]
        
        return merged