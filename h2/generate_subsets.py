# Given an n-element set S, generate all m-element subsets. 
#
# input:	a set of integers S and an integer m denoting the cardinality
#			of subsets generated from S
# output:	a list of tuples of all m-element subsets of S
#
# CISC471
# Sean Nesdoly
# 2017-09-26

import itertools

def generate_subsets(S, m):
	alphabet = set(S) 
	subsets = [i for i in itertools.combinations(alphabet, m)]
	return subsets
