class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {}

        for ch in s:
            if ch not in seen:
                seen[ch] = 1
            else:
                seen[ch] += 1
        
        for ch in t:
            if ch not in seen:
                return False
            
            seen[ch] -= 1

            if seen[ch] < 0:
                return False
        
        for ch in seen:
            if seen[ch] > 0:
                return False
        
        return True