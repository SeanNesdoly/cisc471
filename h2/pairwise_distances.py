# For a set X containing numbers, compute the difference multiset of X.
# This is defined as the set of all positive differences between elements
# of X (the pairwise distances). If X contains n elements, then the difference 
# multiset of X contains (n choose 2) elements.
# 
# input:	a set X of integers
# output:	the multiset of pairwise distances from X
# 
# CISC471
# Sean Nesdoly
# 2017-09-25

import itertools

def pairwise_distances(X): 
	subsets = [i for i in itertools.combinations(X, 2)]

	distances = []
	for t in subsets:
		distances.append(abs(t[0] - t[1]))

	return distances

# sample run output: [1, 5, 4]
print(pairwise_distances([1,2,6])) 