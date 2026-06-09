class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26

        for letter in s:
            count[ord(letter) - ord('a')] += 1
        
        for letter in t:
            if count[ord(letter) - ord('a')] == 0:
                return False
            count[ord(letter) - ord('a')] -= 1

        return count == [0] * 26