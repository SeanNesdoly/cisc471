# The Partial Digest Problem
#
# Given all pairwise distances between points on a line, reconstruct the
# positions of those points.
#
# input:	the multiset of pairwise distances L, containing (n choose 2)
#			integers
# output:	a set X of n integers such that the pairwise distances computed
#			from X is equal to the set L
#
# CISC471
# Sean Nesdoly
# 2017-09-26

from pairwise_distances import *

width = -1 # width of entire DNA string

def partial_digest(L):
	global width
	width = max(L)
	L.remove(width)
	X = [0, width]

	# recursively construct the order of restriction fragments
	place(L, X) 

	# here, the pairwise distances of X equals set L
	return X 


# construct the set X such that the pairwise distances of X form
# the set L; this is analagous to placing restriction fragments
# in their correct order to construct the original DNA string
def place(L, X):
	if len(L) == 0:
		X.sort()
		print X
		return

	y = max(L)

	# CASE 1: place fragment on left
	D = distances(y, X)
	if set(D).issubset(set(L)):
		X.append(y)
		for d in D:
			L.remove(d)

		place(L, X)

		X.remove(y)
		for d in D:
			L.append(d)
	
	# CASE 2: place fragment on right
	D = distances(width - y, X)
	if set(D).issubset(set(L)):
		X.append(width - y)
		for d in D:
			L.remove(d)

		place(L, X)

		X.remove(width - y)
		for d in D:
			L.append(d)

	return



# computes the distances between an 
# integer x and all elements in the set S
def distances(x, S):
	D = list()
	for i in range(len(S)):
		D.append(abs(x - S[i]))

	return D



# sample run
L = [2,2,3,3,4,5,6,7,8,10] 
partial_digest(L) # -->  [0, 3, 6, 8, 10], [0, 10, 2, 7, 4]
