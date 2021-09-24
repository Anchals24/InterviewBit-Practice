#Topic : String
##Problem Statement >>
""" 
Compare two version numbers version1 and version2.

If version1 > version2 return 1,
If version1 < version2 return -1,
otherwise return 0.
You may assume that the version strings are non-empty and contain only digits and the . character.

The . character does not represent a decimal point and is used to separate number sequences.

For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

Here is an example of version numbers ordering:

0.1 < 1.1 < 1.2 < 1.13 < 1.13.4
"""

def comparison(A , B):
	A = A.split(".")
	B = B.split(".")
	la = len(A)
	lb = len(B)
	maxi = max(la , lb)
	mini = min(la , lb)
	if maxi == la:
		largearr = A
	else:
		largearr = B
	ans = 0
	for a in range(maxi):
		if a < mini:
			if int(A[a]) > int(B[a]):
				return 1
			elif int(A[a]) < int(B[a]):
				return -1
			elif int(A[a]) == int(B[a]):
				ans = 0
		elif a >= mini:
			if largearr == A:
				if int(largearr[a]) > 0:
					return 1
				elif int(largearr[a]) == 0:
					ans = 0
			elif largearr == B:
				if int(largearr[a]) > 0:
					return -1
				elif int(largearr[a]) == 0:
					ans = 0
	return ans
print(comparison(input() , input()))
