class TimeMap:

    def __init__(self):
        self.time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.time_map:
            self.time_map[key].append((value, timestamp))
        else:
            self.time_map[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map:
            return ""
            
        array = self.time_map[key]
        result = ""
        left = 0
        right = len(array) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if array[mid][1] <= timestamp:
                result = array[mid][0]
                left = mid + 1
            else:
                right = mid - 1                
        
        return result
