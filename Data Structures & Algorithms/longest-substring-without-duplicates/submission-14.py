class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        hashset = set()
        longest_length = 0
        for r in range(len(s)):
            while s[r] in hashset:
                hashset.remove(s[l])
                l += 1
            if s[r] not in hashset:
                hashset.add(s[r])
            longest_length = max(len(hashset), longest_length)
        return max(len(hashset), longest_length)