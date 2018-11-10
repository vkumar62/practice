# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        import pdb
        pdb.set_trace()
        if not intervals:
            return []
        
        # Sort the intervals based on end times
        intervals.sort(key=lambda k: k.start)
        result = [intervals[0]]
        
        for i in range(1, len(intervals)):
            interval = intervals[i]
            
            if interval.start <= result[-1].end:
                result[-1] = Interval(min(result[-1].start, interval.start), max(result[-1].end, interval.end))
            else:
                result.append(interval)
        
        return result

intervals = [[2,3],[4,5],[6,7],[8,9],[1,10]]
intervals = [Interval(*interval) for interval in intervals]        
print(list(map(lambda i: (i.start, i.end), Solution().merge(intervals))))
