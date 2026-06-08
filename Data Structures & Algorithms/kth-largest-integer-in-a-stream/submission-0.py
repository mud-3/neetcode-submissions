import random

class KthLargest:
    k = 0
    stream = []

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.stream = nums

    def add(self, val: int) -> int:
        self.stream.append(val)
        print(self.stream)
        return self.quick_select(self.stream, self.k)
        
    def quick_select(self, arr, k):
        # Randomly select a pivot
        pivot = random.choice(arr)

        # For elements greater than the pivot
        leftArr = [x for x in arr if x > pivot]

        # For elements equal to the pivot
        midArr = [x for x in arr if x == pivot]

        # For elements less than the pivot
        rightArr = [x for x in arr if x < pivot]

        # Recursive selection
        if k <= len(leftArr):
            return self.quick_select(leftArr, k)
        if len(leftArr) + len(midArr) < k:
            return self.quick_select(rightArr, k - len(leftArr) - len(midArr))

        # Return pivot as the k-th largest
        return pivot    
