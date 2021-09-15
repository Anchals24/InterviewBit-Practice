#Count and Say

"""
Problem Description

The count-and-say sequence is the sequence of integers beginning as follows: 
1, 11, 21, 1211, 111221, ...
1 is read off as one 1 or 11. 11 is read off as two 1s or 21.
21 is read off as one 2, then one 1 or 1211.

Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.
"""

def countt(s):
    c = ""
    curr_ele = s[0]
    cou = 1
    for i in range(1 , len(s)):
        if s[i] == curr_ele:
            cou += 1
        else:
            c += str(cou)
            c += str(curr_ele)
            curr_ele = s[i]
            cou = 1
    c += str(cou)
    c += str(curr_ele)
    return c

N = int(input())
Sequences = ["1" , "11"]
for i in range(2 , N):
    s = (Sequences[i-1])
    #print(type(st))
    #print("s is" , s)
    new = countt(s)
    Sequences.append(new)
print(Sequences[N-1])

