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
