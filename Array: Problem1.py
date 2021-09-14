#Pick from both sides!
""" 
Problem Description :

Given an integer array A of size N.
You can pick B elements from either left or right end of the array A to get maximum sum.
Find and return this maximum possible sum.

NOTE: Suppose B = 4 and array A contains 10 elements then

You can pick first four elements or can pick last four elements or can pick 1 from front and 3 from back etc . 
You need to return the maximum possible sum of elements you can pick.
"""

def solve(self, A, B):
        leng = len(A)
        #Finding the prefix first.
        prefix_sum = [0 for i in range(leng+1)]
        prefix_sum[0] = A[0]
        for a in range(1 , leng):
            prefix_sum[a] = prefix_sum[a-1] + A[a]
 
        #Finding the suffix then
        Copyy = A[:]
        Copyy.reverse()
        suffix_sum = [0 for i in range(leng+1)]
        suffix_sum[0] = Copyy[0]
        for c in range(1 , leng):
            suffix_sum[c] = suffix_sum[c-1] + Copyy[c]
 
        prefix_sum.pop()
        suffix_sum.pop()
        #print(prefix_sum)
 
        #now writing the main code...!!
        summ = prefix_sum[B-1]
        initial , last = B-1 , 1
        while initial != 1:
            if prefix_sum[initial - 1] + suffix_sum[last-1] > summ:
                summ = prefix_sum[initial - 1] + suffix_sum[last-1]
            initial -= 1
            last += 1
        if suffix_sum[B- 1] > summ:
            summ = suffix_sum[B- 1]
        return summ

def solve(self, A, B):
        arr = A[: B]
        # o/p : [5 , -2 , 3]
        val = sum(A[:B])
        #6
        maxi = val #6
        for i in range(0 , B):
            remove = arr.pop() #removing the last ele -2
            add = A.pop() #last ele of A i.e. 1
            #Remove the last element of arr and replace it with last element of A
            val = val - remove + add
            maxi = max(maxi , val)
        return maxi

