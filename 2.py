#!/usr/bin/env python
import numpy as np
from scipy import linalg
from scipy.sparse import diags
from numpy.linalg import inv

def main():
	#just for test!
	S=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
	print(S)
	S1=S[0:2,2:4]
	print(S1)
	n = 100
	k = -1*np.array([np.ones(n-1),-2*np.ones(n),1*np.ones(n-1)])
	offset = [-1,0,1]
	A = diags(k,offset).toarray()	
	print(A)

	A1=A[0:50,0:50].copy()
	d=inv(np.matrix(A1))
	print(d)

	s=(50,1)
	b1=np.ones(s)
	b2=np.ones(s)
	x1=np.ones(s)
	x2=np.ones(s)
	B1=A[50:100,0:50].copy()
	
	B2=A[0:50,50:100].copy()
	A2=A[50:100,50:100].copy()
	d2=inv(np.matrix(A2))

	s2=(100,1)
	b=np.ones(s2)
	x_asli=linalg.solve(A, b)
	print("the aswer is:",x_asli)
	err1 = np.ones((50,1))*100
	err2 = np.ones((50,1))*100
	iteration=0
	while np.max(err1) > 0 and np.max(err2):
		iteration=iteration+1
		x1n = np.dot(d,(b1 - np.dot(B1,x2)))
		err1 = abs((x1n - x1)/x1n)*100
		x1 = x1n
		x2n = np.dot(d2,(b2 - np.dot(B2,x1)))
		err2 = abs((x2n - x2)/x2n)*100
		x2 = x2n
	print("x1:",x1)
	print("x2:",x2)
	print("iteration:",iteration)
	

	




if __name__ == '__main__':
	main()
