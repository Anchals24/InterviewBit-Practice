"""
Problem Statement :
Problem Description

Given a sorted array A containing N integers both positive and negative.

You need to create another array containing the squares of all the elements in A and return it in non-decreasing order.
"""

#Approach1 :
#O(nlogn) #

def solve(self, A):
    Sq = []
    for a in A:
        square = a * a
        Sq.append(square)
    Sq.sort()
    return Sq 