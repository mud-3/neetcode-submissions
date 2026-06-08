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

        last_end = intervals[0].start

        for interval in intervals:
            if last_end > interval.start:
                return False
            last_end = interval.end

        return True