"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals: return 0
        intervals.sort(key=lambda j:j.start)
        rooms = []
        roomId = 0
        heapq.heappush(rooms, (intervals[0].end, roomId, 1))

        for i in range(1, len(intervals)):
            start, end = intervals[i].start, intervals[i].end
            if rooms[0][0] <= start:
                currEnd, rid, cnt = heapq.heappop(rooms)
                heapq.heappush(rooms, (end, rid, cnt+1))
            else:
                roomId += 1
                heapq.heappush(rooms, (end, roomId, 1))
        return len(rooms)
        