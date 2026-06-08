class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1
        
        frequent_count = [[] for i in range(len(nums))]
        for num in count:
            frequent_count[count[num] - 1].append(num)
            
        result = []
        for i in range(len(frequent_count) - 1, -1, -1):
            if frequent_count[i] != []:
                for num in frequent_count[i]:
                    result.append(num)
                    k -= 1
                    if k == 0:
                        return result