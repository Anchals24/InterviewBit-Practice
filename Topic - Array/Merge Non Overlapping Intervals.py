"""
Problem Statement :
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
You may assume that the intervals were initially sorted according to their start times.

Example 1:
Given intervals [1,3],[6,9] insert and merge [2,5] would result in [1,5],[6,9].

Example 2:
Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] would result in [1,2],[3,10],[12,16].
"""

def insert(self, intervals, new_interval):
        intervals.append(new_interval)
        intervals.sort(key = lambda i:i.start)
        merged = []
        merged.append(intervals[0])
        for j in range(1 , len(intervals)):
            if intervals[j].start > merged[-1].end:
                merged.append(intervals[j])
            else:
                merged[-1].end = max(intervals[j].end , merged[-1].end)
        return merged

#TC : O(nlogn)
