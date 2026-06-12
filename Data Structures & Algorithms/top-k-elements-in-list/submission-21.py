from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = defaultdict(int)

        for num in nums:
            frequencies[num] += 1

        buckets = [[] for _ in range(len(nums))]

        for num, frequency in frequencies.items():
            buckets[frequency - 1].append(num)

        results = []
        for bucket in reversed(buckets):
            for num in bucket:
                results.append(num)
                if len(results) == k:
                    return results
        return results