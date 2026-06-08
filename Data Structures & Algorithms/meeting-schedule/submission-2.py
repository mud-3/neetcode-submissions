"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
from operator import attrgetter

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True

        # 1. 排序
        intervals.sort(key=attrgetter('start'))

        # 2. 由第一個會議嘅結束時間開始紀錄
        last_end = intervals[0].end

        # 3. 由 index 1 開始比較
        for i in range(1, len(intervals)):
            # 如果下一個會議喺上一個收工之前就開始，即係撞咗
            if intervals[i].start < last_end:
                return False
            # 更新最遲收工時間
            last_end = intervals[i].end

        return True