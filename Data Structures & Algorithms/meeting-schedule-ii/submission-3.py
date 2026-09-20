"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        if not intervals:
            return 0

        rooms = 0
        maxRooms = 0

        start = sorted([interval.start for interval in intervals])
        end = sorted([interval.end for interval in intervals])

        s, e = 0, 0
        while s < len(intervals):
            if start[s] < end[e]:
                s += 1
                rooms += 1
                maxRooms = max(rooms, maxRooms)

            else:
                e += 1
                rooms -= 1

        return maxRooms