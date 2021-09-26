def mergeintervals(Arr):
    Arr = sorted(Arr, key = lambda x:x[0])
    start = -1000000
    end = -1000000
    mergedintervals = []
    for i in range(len(Arr)):
        temp = Arr[i]
        if temp[0] > end:
            if i != 0:
                mergedintervals.append([start , end])
            start = temp[0]
            end = temp[1]
        else:
            end = max(end , temp[1])
    
    if end != -1000000 and [start, end] not in mergedintervals:
        mergedintervals.append([start,end])
    print("Merged intervals are >> ")
    return mergedintervals

print(mergeintervals([[2,4] , [4,7] , [6,8] , [1,9] ]))


#Another approach

def merge(self, intervals):
    intervals.sort(key = lambda i:i.start)
    merged = []
    merged.append(intervals[0])
    for j in range(1 , len(intervals)):
        if intervals[j].start > merged[-1].end:
            merged.append(intervals[j])
        else:
            merged[-1].end = max(intervals[j].end , merged[-1].end)
    return merged
