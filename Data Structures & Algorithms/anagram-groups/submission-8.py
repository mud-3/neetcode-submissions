class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for word in strs:
            frequency = [0] * 26
            for char in word:
                frequency[ord(char) - ord('a')] += 1
            anagrams[tuple(frequency)].append(word)

        return list(anagrams.values())
