#Solution 1 : O(n***3) >> Brute - Force

import math
A = [1, 2, 3]
maxi = -math.inf
l = len(A)
for i in range(l):
    for j in range(i+1 , l):
        for k in range(j +1 , l):
            if A[i] < A[j] and A[j] < A[k]:
                s = A[i] + A[j] + A[k]
                maxi = max(maxi , s)
print(maxi)

#Solution 2: Brute-Force O(n**2)

import math
A = [1, 2, 3]
l = len(A)
D = {}
max_sum = -math.inf
for a in range(l):
    for b in range(a+1 , l):
        if A[a] < A[b]:
            D[A[a] + A[b]] = (a , b)
Key = D.keys()
Keys = list(Key)
for c in range(2 , l):
    for k in Keys:
        maxi = max(D[k])
        if c > maxi:
            if A[c] > A[D[k][1]]:
                summ = k + A[c]
                max_sum = max(max_sum , summ)
print(max_sum)

from bisect import bisect_left
def sorting(A):
    A.sort()
    return A
Arr = [2 , 5 , 3 , 1 , 4 , 9]
K = [0] * len(Arr)
l = len(Arr) - 1 
for i in range(l):
    maxi = max(Arr[i : l+1])
    if maxi > Arr[i]:
        K[i] = maxi
    else:
        I[i] = -1
I[-1] = -1
A = [2]

for j in range(l):