class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dict = [0 for i in range(26)]
        for s in s1:
            s1_dict[ord(s) - ord("a")] += 1

        left, right, frequency = 0, len(s1), 0

        while right <= len(s2):
            for i in range(left, right):
                if s1_dict[ord(s2[i]) - ord("a")] == 0:
                    left += 1
                    right += 1
                    frequency = 0
                    s1_dict = [0 for i in range(26)]
                    for s in s1:
                        s1_dict[ord(s) - ord("a")] += 1
                    break
                else:
                    s1_dict[ord(s2[i]) - ord("a")] -= 1
                    frequency += 1

            if frequency == len(s1):
                return True

        return False