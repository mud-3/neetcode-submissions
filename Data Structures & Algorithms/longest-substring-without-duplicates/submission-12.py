class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        hashset = set()
        longest_length = 0
        while r < len(s):
            while s[r] in hashset and l < r:
                hashset.remove(s[l])
                l += 1
            if s[r] not in hashset:
                hashset.add(s[r])
                r += 1
            longest_length = max(len(hashset), longest_length)
        return max(len(hashset), longest_length)