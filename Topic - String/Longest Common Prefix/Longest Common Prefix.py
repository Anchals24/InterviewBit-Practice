#Solution : 1

def longestcommonprefix(Arr):
    smallest = min(Arr) #Find the smallest element of the array
    #print(smallest)    
    lmini = len(smallest) #length of the smallest element of the array
    i = 0 
    common = ""
    while i < lmini:
        for A in Arr:
            if A[i] != smallest[i]:
                return common
        common += smallest[i]
        i += 1
    return common
print(longestcommonprefix(["aaaaaa" , "aab" , "aabvde" , "aabb"]))

#Solution : 2

def longestcommonprefix2(Arr):
    minele = min(Arr)
    maxele = max(Arr)
    count = 0
    for i in range(min(len(maxele) , len(minele))):
        if minele[i] == maxele[i]:
            count += 1
    return minele[:count]

print(longestcommonprefix2(["aa" , "aabse" , "a" ]))





