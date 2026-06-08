class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = {}
        left = 0
        length = 0
        for right in range(len(s)):
            character = s[right]
            if character in substring:
                left = max(left, substring[character] + 1)
            substring[character] = right
            length = max(length, right - left + 1)
        return length