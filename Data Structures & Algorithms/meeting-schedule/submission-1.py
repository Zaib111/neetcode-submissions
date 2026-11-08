"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda i: i.start)
        max_finish = -1
        for interval in intervals:
            start, finish = interval.start, interval.end
            if start < max_finish:
                return False
            max_finish = max(max_finish, finish)
        return True