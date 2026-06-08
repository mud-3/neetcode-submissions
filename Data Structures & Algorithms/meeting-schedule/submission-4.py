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

        intervals.sort(key=attrgetter('start'))

        last_end = intervals[0].end

        for i in range(1, len(intervals)):
            if intervals[i].start < last_end:
                return False

            last_end = intervals[i].end

        return True