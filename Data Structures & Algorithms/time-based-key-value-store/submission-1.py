class TimeMap:

    def __init__(self):
        self.time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.time_map:
            self.time_map[key].append((value, timestamp))
        else:
            self.time_map[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        def binary_search(array, target):
            result = ""
            left = 0
            right = len(array) - 1

            while left <= right:
                mid = left + (right - left) // 2
                if array[mid][1] == target:
                    result = array[mid][0]
                    break
                elif array[mid][1] > target:
                    right = mid - 1
                else:
                    result = array[mid][0]
                    left = mid + 1
            
            return result
        
        if key not in self.time_map:
            return ""
        
        return binary_search(self.time_map[key], timestamp)
