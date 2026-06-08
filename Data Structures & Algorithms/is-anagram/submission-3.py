class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for i in range(len(s)):
            if s[i] in t:
                pos = t.index(s[i])
                t = t[:pos] + t[pos+1:]
            else:
                return False
        return len(t) == 0