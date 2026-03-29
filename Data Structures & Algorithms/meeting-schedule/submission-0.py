class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        # sort all intervals by start time and then end time
        intervals.sort(key=lambda i:i.start)

        prevStart, prevEnd = intervals[0].start, intervals[0].end

        for i in range(1, len(intervals)):
            currStart, currEnd = intervals[i].start, intervals[i].end
            if currStart < prevEnd :
                return False
            prevStart, prevEnd = intervals[i].start, intervals[i].end
        return True