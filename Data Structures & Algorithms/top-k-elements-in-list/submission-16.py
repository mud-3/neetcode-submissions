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
            if bucket:
                for num in bucket:
                    if num not in results:
                        results.append(num)
                        k -= 1
            if k == 0:
                break

        return results
