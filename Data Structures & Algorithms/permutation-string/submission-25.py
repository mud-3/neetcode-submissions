class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        window_frequency = [0] * 26
        s1_frequency = [0] * 26

        for s in s1:
            s1_frequency[ord(s) - ord("a")] += 1

        left = 0
        for right in range(len(s2)):
            window_frequency[ord(s2[right]) - ord("a")] += 1

            if right - left >= len(s1):
                window_frequency[ord(s2[left]) - ord("a")] -= 1
                left += 1

            if window_frequency == s1_frequency:
                return True

        return False