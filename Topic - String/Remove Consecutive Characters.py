#Remove Consecutive Characters 
"""
Problem Description:

Given a string A and integer B, remove all consecutive same characters that have length exactly B.
"""

A = "aabbde"
B = 2
l = len(A)
new = ""
curr_e = A[0]
count = 1
for a in range(1 , l):
    if A[a] == curr_e:
        count += 1
    else:
        if count != B:
            new += curr_e
            curr_e = A[a]
            count = 1
if count != B:
    new += A[a]
print(new)