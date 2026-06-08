class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = defaultdict(int)
        left = 0
        max_frequency = 0
        anser = 0

        for right in range(len(s)):
            counts[s[right]] += 1
            max_frequency = max(max_frequency, counts[s[right]])

            while (right - left + 1) - max_frequency > k:
                counts[s[left]] -= 1
                left += 1

            anser = max(anser, right - left + 1)

        return anser