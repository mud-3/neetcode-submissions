from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = defaultdict(int)

        for num in nums:
            frequencies[num] += 1

        buckets = [[] for _ in range(len(nums) + 1)]

        for num, frequency in frequencies.items():
            buckets[frequency].append(num)

        results = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                results.append(num)
                if len(results) == k:
                    return results
        return results