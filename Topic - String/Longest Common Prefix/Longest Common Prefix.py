#Longest Common Prefix.
#Arr = ["aa" , "aab" , "aabvde"]
"""
Problem Description >>

Given the array of strings A, you need to find the longest string S which is the prefix of ALL the strings in the array.
Longest common prefix for a pair of strings S1 and S2 is the longest string S which is the prefix of both S1 and S2.

For Example: longest common prefix of "abcdefgh" and "abcefgh" is "abc".
"""
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





