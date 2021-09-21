#Topic : String

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