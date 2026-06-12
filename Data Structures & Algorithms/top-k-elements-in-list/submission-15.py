from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums))]
        frequencies = defaultdict(int)

        for num in nums:
            frequencies[num] += 1
            buckets[frequencies[num] - 1].append(num)

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
