"""
Problem Description >> 

Given a string A consisting of lowercase characters.
You have to find the number of substrings in A which starts with vowel and end with consonants or vice-versa.
Return the count of substring modulo 109 + 7.

"""
#Optimized Approach

A = input()
vowels = ["a" , "e" , "i" , "o" , "u"]
curr_index = 0 
cou_vow = 0
cou_cons = 0
for a in A:
    if a in vowels:
        cou_vow += 1
        curr_index += cou_cons
    else:
        cou_cons += 1
        curr_index += cou_vow
curr_index %= 1000000007
print(curr_index)
