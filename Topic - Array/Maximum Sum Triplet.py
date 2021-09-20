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
import math
A =  [ 18468, 6335, 26501, 19170, 15725, 11479, 29359, 26963, 24465, 5706, 28146, 23282, 16828, 9962, 492, 2996, 11943, 4828, 5437, 32392, 14605 ]
K = [0] * len(A) #K = suffix Aay
l = len(A) - 1 
for i in range(l):
    maxi = max(A[i : l+1])
    if maxi > A[i]:
        K[i] = maxi
    else:
        K[i] = -1
K[-1] = -1
#print("K is >>" , K) #[9, 9, 9, 9, 9, -1]
I = [0] * len(A) 
A =  [ 18468, 6335, 26501, 19170, 15725, 11479, 29359, 26963, 24465, 5706, 28146, 23282, 16828, 9962, 492, 2996, 11943, 4828, 5437, 32392, 14605 ]
S = set()
S.add(A[0]) #18468
for j in range(1 , l):
    LS = list(S) [18468]
    print("Sorted list is >>" , LS)
    i = bisect_left(LS , A[j])
    print("Binary search i is" , i)
    I[j] = LS[i-1]
    print("Ith list is >>" , I)
    if i - 1 < 0: 
        I[j] = -1
    S.add(A[j]) 
maxi = 0
for j in range(1 , l):
    if K[j] != -1 and I[j] != -1:
        summ =  I[j] + A[j] + K[j]
        maxi = max(summ , maxi)
print(maxi)

#CORRECT SOLUTION >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

from bisect import bisect_left 
  
def BinarySearch(a, x): 
    i = bisect_left(a, x) 
    if i: 
        return (i-1) 
    else: 
        return -1
  
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A): #A = [2 , 5, 3, 1, 4, 9]
        n=len(A) #6
        K=[0]*n  #K = [0,0,0,0,0,0]
        K[n-1]=A[n-1] #K = [9,9,9,9,9,9]
        for i in range(n-2,-1,-1): #(4 , -1 , -1)
            #i = 2
            K[i]=max(K[i+1],A[i]) #K[2] (0) = K[3] (9) , A[2] (3)
        I=[] #[1 , 2 ,3, 5]
        maxe=0 #0
        I.append(A[0]) 
        for i in range(1,n-1): #(1 , 5) #1 , 2, 3, 4
            #i = 3
            res = BinarySearch(I, A[i]) #[2 , 3,  5] , 1 = 0
            if(res!=-1): #true
                if K[i+1] <= A[i]: #9 < = 3 #K < j : continue , basically , A[i] = j
                    continue
                ans=I[res] + A[i] + K[i+1] #I[0] + A[1] + K[2]  >> 2 + 3 + 9 = 14
                maxe=max(maxe,ans) #maxe = 16
            I.insert(res+1,A[i]) #
        return maxe
        return 0



    
    

    








    

